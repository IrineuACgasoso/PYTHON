# Declaração de lista
lista_nomes = []

nome = input()

# Adiciona o valor
lista_nomes.append(nome)

print(nome)

# Print de lista
print(lista_nomes)

# Print sem colchetes + caracteres da aspa
# .join retira os colchetes e adiciona o caractere entre aspas entre cada indice
print(", ".join(lista_nomes))

# Loop com append
numero_pessoas = int(input())

for pessoa in range (numero_pessoas):
    nome = input()
    lista_nomes.append(nome)

    print(", ".join(lista_nomes))


# Indexação

# Ex.: Tipo "nome - idade - cidade - profissao"
# .split separa a variavel pelo parametro adicionado

# lista = [13, caio, 3.14, 3, 67,  5]
#          [0]  [1]  [2]  [3] [4] [5]
pessoas = []
idades = []
cidades = []
profissoes = []

numero_entrevistados = int(input())

for entrevstado in range(numero_entrevistados):
    entrada = input().split(" - ")
    pessoas.append(entrada[0])
    idades.append(entrada[1])
    cidades.append(entrada[2])
    profissoes.append(entrada[3])
# 19, 35, 76, 51                     76
indice_mais_velho = idades.index(max(idades))

print(f"O mais velho é {pessoas[indice_mais_velho]}")

    
# Slicing

lista_2 = [0, 1, 2, 3, 4, 5]

# Ex.: Quero só até o 3:

lista_ate_o_3 = lista_2[0:3]
# [0, 1, 2, 3]



# Pop
# Ex.: Deixar só int
lista_3 = [0, 1, 2, "caio", 3, "4", 5, "penis"]

# len(lista) = numero de elementos da lista

for elemento in range(0, len(lista_3)):
    if lista_3[elemento] is not int:
        lista_3.pop(elemento)

# Extras

# [0, 1, 2, 3, 5]

# lista = [a, b, c]
# lista[0] = d
# lista = [d, b, c]

# string = aaaaaaaaaplsisanaaaaaaaaaaaaafbssoaajsnssn -> ache o f
# for letra in string:
#   if letra == 'f'...
#       






