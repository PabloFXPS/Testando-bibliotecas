from pathlib import Path
# Exercício 1 – Criando estrutura de pastas
# Crie a seguinte estrutura:
# ├──dados/
# │  ├── entrada/
# │  └── saida/
# ├──relatorios/
# Crie todas as pastas em uma única execução do seu código.

dados = Path("Dados")
subpasta = ["Entrada","Saida"]
relatorio = Path("Relatórios")

for spasta in subpasta:
    (dados / spasta).mkdir(parents=True, exist_ok=True)
relatorio.mkdir(exist_ok=True)

# Exercício 2 – Criar vários arquivos de exemplo
# Dentro da pasta entrada/, crie 3 arquivos vazios:
# dados1.txt
# dados2.txt
# dados3.txt

cont = 1
base = Path(__file__).parent
entrada = base / "Dados" / "Entrada"

for arquivos in range(1,4):
    texto = entrada / f"Texto{cont}"
    texto.touch()
    cont += 1

# Exercício 3 – Conferindo e filtrando arquivos .txt
# Liste todos os arquivos .txt dentro de entrada/.
# Imprima apenas o nome do arquivo (sem o caminho completo).

base = Path(__file__).parent
entrada = base / "Dados" / "Entrada"

for textos in entrada.iterdir():
    print(textos.stem)