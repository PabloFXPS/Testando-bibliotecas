import shutil
from pathlib import Path

# 1. Cópia simples com estrutura
# Crie um script que:
# Crie uma pasta imagens.
# Coloque 2 arquivos fictícios .png dentro dela
# Copie todos os arquivos .png da pasta imagens para uma nova pasta chamada backup.

pastanova = Path(r"Shutil\Imagens")
pastanova.mkdir(exist_ok=True)

(pastanova / "imagem.png").touch(exist_ok=True)
(pastanova / "imagem2.png").touch(exist_ok=True)

#Backup
backup = Path(r"Shutil\Backup")
backup.mkdir(exist_ok=True)

cont = 1
for imagem in pastanova.glob("*.png"):
    destino = backup / f"imagem_copiada{cont}.png"
    shutil.copy(imagem,destino)
    cont+=1

# 2. Mover e renomear arquivos automaticamente
# Crie um script que:
# Verifica se existe um arquivo chamado relatorio.txt.
# Move esse arquivo para uma pasta chamada relatorios_antigos.
# Durante a movimentação, renomeie o arquivo para relatorio_backup.txt.
atual= Path("Shutil")

for arquivos in atual.rglob("*.txt"):
    if arquivos.is_file():
        if arquivos.stem == "relatorio":
            print("arquivo encotrado")
            relatorio =arquivos
            break
        else:
            print("Não encotrado")

relatorios_pasta= Path("Shutil") / "relatorios_antigos"
relatorios_pasta.mkdir(exist_ok=True)

shutil.copy(relatorio,f"{relatorios_pasta}/{relatorio.stem}_backup{relatorio.suffix}")

# 3. Automatizando extração de arquivos
# Considerando o arquivo zip que deixei na sessão de recursos, crie um script que:
# Crie uma pasta chamada extraido/.
# Extraia o conteúdo do .zip dentro da pasta criada.
# Ao final, liste todos os arquivos extraídos.

zipado = Path("Shutil") / "arquivos_secretos.zip"
extrair = Path("Shutil") / "extraido"

shutil.unpack_archive(zipado,extrair)

for arquivos in extrair.iterdir():
    print(arquivos)