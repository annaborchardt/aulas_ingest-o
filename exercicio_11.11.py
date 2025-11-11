# 'R' lê o arquivo

arquivo = open('C:\\Users\\Aluno\\Documents\\email.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

print('\n')

arquivo = open('C:\\Users\\Aluno\\Documents\\email.txt', 'r', encoding="utf-8")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

#'A' adiciona conteudo no arquivo

arquivo = open('C:\\Users\\Aluno\\Documents\\email.txt', 'a')
arquivo.write("\n Nova Linha \n")
arquivo.close()


#'W' substitui o conteudo
arquivo = open('C:\\Users\\Aluno\\Documents\\email.txt', 'w')
arquivo.write("\n Tchau Conteudo \n")
arquivo.close()


arquivo = open('C:\\Users\\Aluno\\Documents\\email.txt', 'r',  encoding="utf-8")
linha = arquivo.readline()
print(linha)
arquivo.close()

arquivo = open('C:\\Users\\Aluno\\Documents\\email.txt', 'r',  encoding="utf-8")
linha = arquivo.readline()
while linha != "":
    if "Terceira" in linha:
        print(linha)
    linha= arquivo.readline()
arquivo.close()

#Vira um dicionario

planetaTerra = {
'nome': 'Terra', 
'Luas': 1
}

print(planetaTerra.get('nome'))

dados = {'nome': 'João', 'idade': 25, 'cidade': 'Florianópolis'}

print(dados.get('idade')) 



if 'idade' in dados:
    print("A chave idade existe no dicionario")
else:
    print("A chave idade não existe no dicionario")


chuvas = {
'outubro': 3.5,
'novembro': 4.2,
'dezembro': 2.1
}

if 'dezembro' in chuvas:
    chuvas['dezembro'] = chuvas['dezembro'] + 1
else:
    chuvas['dezembro'] = 1
print(chuvas)

chuvas = {
'outubro': 3.5,
'novembro': 4.2,
'dezembro': 2.1
}

if 'Janeiro' in chuvas:
    chuvas['Janeiro'] = chuvas['Janeiro'] + 1
else:
    chuvas['Janeiro'] = 1
print(chuvas)
