# Exercicios em aula

#exercicio 1

print("Mensagem de Texto ")

idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você é um adulto")
else: 
    print("Você é menor de idade")

#exercicio 2

contador= 10

while contador >= 1:
    print("O contador é: ", contador)
    contador = contador - 1

#exercicio 3

# A contagem da lista começa com zero

L = [3, 'abacate', 9.7 , [5,6,3], 'Python', (3, 'j')] 

print(L)
print (L[3])
print (L[2:5]) #onde começa  e onde termina
print (L[2:]) #onde começa
print (L[:2]) #onde termina
print (L[::2]) # de quanto em quanro ele vai pular

print(len(L)) #quantidade de coisas que tenho na minha lista

L1= [10,44,30]
print (sum(L1))

print (sum(L1) / len(L1))

print (3 in L) # irá retornar true porque 3 é um valor da lista

print (10 in L) # irá retornar false porque não é um valor da lista

#Exercicio 4

letra = input("Digite o status do aluno (A ou B): ")

if letra == "A" :
    print("Aprovado")
elif letra == "B":
    print("Reprovado")
else:
    print("Letra Invalida")

#Exercicio 5

nomes = ['Clara', 'Giorgian', 'Laís']

for n in nomes:
    print(n)

for n in nomes:
    print(n)
else:
    print("Todos os itens foram exibidos com sucesso")

letras = ['P', 'y', 't', 'h', 'o', 'n']

for  n in letras:
    print (n)

for caracter in 'Python': #ele entende que uma string é uma lista
    print(caracter)

#Exercicio 6

# Range, função utilizada para criar um intervalo de valores 

lista= list(range(10))
print(lista)

lista= list(range(5,21))
print(lista)

lista= list(range(100,201, 5))
print(lista)

#Exercicio 7

nome=input("Digite o seu nome: ")

def saudacao(nome):
 print("Olá, " + nome + "! Como você está hoje?")

sudacao(nome)

