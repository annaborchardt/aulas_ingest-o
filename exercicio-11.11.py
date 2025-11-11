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
