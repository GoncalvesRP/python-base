#!/usr/bin/env python3

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# number = range(1, 11) # start, stop

# # Iterable
# for number in number:
#     par = number % 2 == 0 
#     if par:
#          print(number)
#     else:
#         continue
         
#     print(f"mais codigo com {number}")
    
# dados = {}
# for line in open("post.txt"):
#     if line == "---\n":
#         break
#     key, valor = line.split(":")
#     dados[key] = valor.strip()
    
# print(dados)
    
original = [1, 2, 3]

# For loop / Laço for
dobrada = []
for n in original:
    dobrada.append(n * 2)
print(dobrada)

# Funcional
# List Comprehension
dobrada = [n * 2 for n in original]
print(dobrada)

# Dict Comprehension
dados = {
    line.split(":")[0]: line.split(":")[1].strip()
    for line  in open("post.txt") 
    if ":" in line
}

dados = {}
for line in open("post.txt"):
    if ":" in line:
        key, valor = line.split(":")
        dados[key] = valor.strip()

print(dados)
