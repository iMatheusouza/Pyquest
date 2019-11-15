masculino = int(input("Digite o número de alunos do sexo masculino: "))
feminino = int(input("Digite o número de alunas do sexo feminino: "))
aprovados = int(input("Digite o número de alunos da turma aprovados: "))
total = masculino + feminino
print((masculino/total)*100,"% de meninos")
print((feminino/total)*100,"% de meninas")
print((aprovados/total)*100,"% foram aprovados")