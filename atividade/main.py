import os
from moldels.pessoa import Pessoa
from moldels.enums.sexo import Sexo

os.system("cls || clear")

aluno = Pessoa("Marta", 22, Sexo.FEMININO)
print(aluno)