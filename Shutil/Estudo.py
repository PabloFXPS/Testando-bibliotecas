import shutil
from pathlib import Path

shutil.copy("Test.txt", "backup/test_copiado.txt") #Nome do arquivo para copiar|para onde ele vai = copia um arquivo e cola ele em outro lugar
shutil.copy2("Test.txt", "backup/test_copiado_metadados.txt")#Mesma coisa do copy, mas, ele copia tbm os metadados do arquivo ex: data de quando foi criado

#copiar uma pasta e tudo que tem dentro e deletar
shutil.copytree("pasta2","pasta_backup",dirs_exist_ok=True)#Caso ja tenha nao da erro
shutil.rmtree("pasta_backup")

#mover arquivos
test = Path("test.txt")
shutil.move(test,"backup/test_copiado")

#zipagem e descompactar
shutil.make_archive("backup","zip", "backup_zipado")
shutil.unpack_archive("backup_zipado.zip","pasta_dos_arquivos")