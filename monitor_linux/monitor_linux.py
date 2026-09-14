#!/usr/bin/env python3
"""
Script de Monitoramento de Rotinas Operacionais no Linux
Monitora: CPU, Memória, Disco, Processos e Serviços
"""

import psutil
import subprocess
import time
import os
import sys
from datetime import datetime
from collections import defaultdict

class MonitorLinux:
    def __init__(self):
        self.historico = defaultdict(list)
        self.limite_cpu = 80  # % de alerta
        self.limite_memoria = 85  # % de alerta
        self.limite_disco = 90  # % de alerta
        
    def limpar_tela(self):
        """Limpa a tela do terminal"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def monitorar_cpu(self):
        """Monitora o uso da CPU"""
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        
        print(f"📊 CPU: {cpu_percent}% utilizado")
        print(f"   Núcleos: {cpu_count}")
        
        if cpu_percent > self.limite_cpu:
            print(f"⚠️  ALERTA: CPU acima de {self.limite_cpu}%!")
        
        return cpu_percent
    
    def monitorar_memoria(self):
        """Monitora o uso de memória RAM"""
        memoria = psutil.virtual_memory()
        
        print(f"💾 Memória RAM:")
        print(f"   Total: {memoria.total / (1024**3):.2f} GB")
        print(f"   Usado: {memoria.used / (1024**3):.2f} GB ({memoria.percent}%)")
        print(f"   Disponível: {memoria.available / (1024**3):.2f} GB")
        
        if memoria.percent > self.limite_memoria:
            print(f"⚠️  ALERTA: Memória acima de {self.limite_memoria}%!")
        
        return memoria.percent
    
    def monitorar_disco(self):
        """Monitora o uso do disco"""
        particoes = psutil.disk_partitions()
        
        print("💿 Discos:")
        for particao in particoes:
            try:
                uso = psutil.disk_usage(particao.mountpoint)
                print(f"   {particao.device} montado em {particao.mountpoint}")
                print(f"   Total: {uso.total / (1024**3):.2f} GB")
                print(f"   Usado: {uso.used / (1024**3):.2f} GB ({uso.percent}%)")
                print(f"   Livre: {uso.free / (1024**3):.2f} GB")
                
                if uso.percent > self.limite_disco:
                    print(f"⚠️  ALERTA: Disco {particao.mountpoint} acima de {self.limite_disco}%!")
                print()
            except PermissionError:
                continue
    
    def monitorar_processos(self, top_n=5):
        """Lista os processos que mais consomem recursos"""
        print(f"🔝 Top {top_n} processos por CPU:")
        
        processos = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                processos.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        # Ordenar por CPU
        processos_cpu = sorted(processos, key=lambda x: x['cpu_percent'] or 0, reverse=True)[:top_n]
        
        for i, proc in enumerate(processos_cpu, 1):
            print(f"   {i}. PID {proc['pid']}: {proc['name']} - CPU: {proc['cpu_percent']:.1f}% - MEM: {proc['memory_percent']:.1f}%")
    
    def verificar_servico(self, nome_servico):
        """Verifica se um serviço está rodando"""
        try:
            resultado = subprocess.run(
                ['systemctl', 'is-active', nome_servico],
                capture_output=True,
                text=True
            )
            status = resultado.stdout.strip()
            
            if status == 'active':
                print(f"✅ Serviço {nome_servico}: ATIVO")
                return True
            else:
                print(f"❌ Serviço {nome_servico}: INATIVO")
                return False
        except Exception as e:
            print(f"⚠️  Erro ao verificar serviço {nome_servico}: {e}")
            return False
    
    def verificar_conexoes(self, porta=None):
        """Verifica conexões de rede"""
        print("🌐 Conexões de rede estabelecidas:")
        
        conexoes = psutil.net_connections(kind='inet')
        estabelecidas = [conn for conn in conexoes if conn.status == 'ESTABLISHED']
        
        if porta:
            estabelecidas = [conn for conn in estabelecidas if conn.laddr.port == porta]
        
        for conn in estabelecidas[:10]:  # Mostrar apenas 10
            print(f"   {conn.laddr.ip}:{conn.laddr.port} -> {conn.raddr.ip}:{conn.raddr.port}")
    
    def gerar_relatorio(self):
        """Gera um relatório resumido"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cpu = psutil.cpu_percent(interval=1)
        memoria = psutil.virtual_memory().percent
        
        relatorio = f"[{timestamp}] CPU: {cpu}% | Memória: {memoria}%"
        
        # Salvar em arquivo
        with open("monitoramento.log", "a") as f:
            f.write(relatorio + "\n")
        
        return relatorio
    
    def executar_monitoramento(self, servicos=None, intervalo=5):
        """
        Executa o monitoramento contínuo
        
        Args:
            servicos: Lista de serviços para monitorar
            intervalo: Intervalo entre verificações (segundos)
        """
        if servicos is None:
            servicos = ['ssh', 'cron', 'nginx', 'apache2']
        
        try:
            while True:
                self.limpar_tela()
                
                print("=" * 60)
                print(f"📈 MONITORAMENTO DE ROTINAS OPERACIONAIS")
                print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print("=" * 60)
                print()
                
                # Monitorar recursos
                self.monitorar_cpu()
                print()
                
                self.monitorar_memoria()
                print()
                
                self.monitorar_disco()
                print()
                
                self.monitorar_processos()
                print()
                
                # Verificar serviços
                print("🔧 Serviços:")
                for servico in servicos:
                    self.verificar_servico(servico)
                print()
                
                # Gerar relatório
                relatorio = self.gerar_relatorio()
                print(f"📝 Relatório: {relatorio}")
                print()
                
                print("=" * 60)
                print(f"🔄 Atualizando em {intervalo} segundos... (Ctrl+C para sair)")
                
                time.sleep(intervalo)
                
        except KeyboardInterrupt:
            print("\n\n✅ Monitoramento encerrado pelo usuário.")
            sys.exit(0)

def menu_principal():
    """Menu principal interativo"""
    monitor = MonitorLinux()
    
    while True:
        monitor.limpar_tela()
        print("=" * 50)
        print("🔍 SISTEMA DE MONITORAMENTO LINUX")
        print("=" * 50)
        print("1. Monitoramento contínuo (atualiza a cada 5s)")
        print("2. Verificação única")
        print("3. Monitorar serviço específico")
        print("4. Verificar conexões de rede")
        print("5. Ver logs de monitoramento")
        print("6. Sair")
        print("=" * 50)
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            servicos = input("Serviços para monitorar (separados por vírgula): ").split(',')
            servicos = [s.strip() for s in servicos if s.strip()]
            intervalo = input("Intervalo de atualização (segundos) [5]: ") or "5"
            monitor.executar_monitoramento(
                servicos=servicos if servicos else None,
                intervalo=int(intervalo)
            )
        
        elif opcao == '2':
            monitor.limpar_tela()
            print("📊 Verificação única do sistema\n")
            monitor.monitorar_cpu()
            print()
            monitor.monitorar_memoria()
            print()
            monitor.monitorar_disco()
            print()
            monitor.monitorar_processos()
            print()
            input("\nPressione Enter para continuar...")
        
        elif opcao == '3':
            servico = input("Nome do serviço: ")
            monitor.verificar_servico(servico)
            input("\nPressione Enter para continuar...")
        
        elif opcao == '4':
            porta = input("Porta específica (Enter para todas): ")
            monitor.verificar_conexoes(porta=int(porta) if porta else None)
            input("\nPressione Enter para continuar...")
        
        elif opcao == '5':
            try:
                with open("monitoramento.log", "r") as f:
                    logs = f.readlines()[-20:]  # Últimas 20 linhas
                    print("\n📋 Últimos logs de monitoramento:\n")
                    for log in logs:
                        print(log.strip())
            except FileNotFoundError:
                print("\nNenhum log encontrado ainda.")
            input("\nPressione Enter para continuar...")
        
        elif opcao == '6':
            print("\n✅ Saindo do sistema...")
            break
        
        else:
            print("\n❌ Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    # Verificar dependências
    try:
        import psutil
    except ImportError:
        print("❌ psutil não está instalado. Instale com:")
        print("   pip install psutil")
        sys.exit(1)
    
    # Verificar se é Linux
    if os.name != 'posix':
        print("⚠️  Este script é otimizado para Linux. Algumas funções podem não funcionar.")
    
    # Iniciar
    print("🚀 Iniciando Sistema de Monitoramento...")
    time.sleep(1)
    
    # Se argumentos forem passados, executar monitoramento contínuo
    if len(sys.argv) > 1:
        monitor = MonitorLinux()
        servicos = sys.argv[1:] if len(sys.argv) > 1 else None
        monitor.executar_monitoramento(servicos=servicos)
    else:
        menu_principal()