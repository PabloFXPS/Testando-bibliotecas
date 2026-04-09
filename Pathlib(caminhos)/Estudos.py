from pathlib import Path
#Relativos / absolutos
#Relativo: Busca da pasta atual que seria "pathlib(caminho)" até a onde esta a pasta.
caminho = Path("test.txt")

print(caminho)

#Absoluto: Faz uma busca a partir da primeira pasta do pc. Tipo "C:\Users\pablo\Documents"
caminho_absoluto = Path(r"C:\Users\pablo\OneDrive\Área de Trabalho\Estudos\Testes\Pathlib(caminhos)\test.txt")
print(caminho_absoluto)

#Relativos para absoluto
print("Conversão:",caminho.absolute())

#Se assiste ou não
if caminho.exists():
    print("Existe")
else:
    print("Nao existe")

#Verificação
if caminho.is_file():
    print("É um arquivo")
elif caminho.is_dir():
    print("É uma pasta")

#Criação/deletar pasta
nova_pasta = Path("Nova Pasta")
nova_pasta.mkdir(exist_ok=True)

#caminho.unlink() #Deleta arquivos
nova_pasta.rmdir() #Apaga só pasta, nao arquivos.

#escrever arquivos (não indicado)
caminho.write_text("Uma frase aí",encoding="utf-8") #Encoding para aceitar í

#Mostrar oque tem dentro da pasta
pasta = Path()#pega a pasta atual

for arquivos in pasta.iterdir():#da para filtrar com o .glob("*.txt")
    print(arquivos)

#informações
print(caminho.name)#nome + sufix
print(caminho.stem)#só o nome
print(caminho.suffix)#só o sufix

#Criar arquivos vazios
arquivo_criado = Path("arquivo_criado.txt")
arquivo_criado.touch()