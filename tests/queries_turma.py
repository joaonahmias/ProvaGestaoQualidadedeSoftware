from ConexaoDB import *

def medias_acima_de_9(bd):
    return ler_bd(bd,"SELECT a.nome FROM media_aluno_turma m, aluno a WHERE media >=9 AND  m.id_aluno = a.id ")

def turmas_de_um_aluno(bd,aluno):
   query = "SELECT t.nome FROM media_aluno_turma m, aluno a, turma t WHERE a.nome = ? AND m.id_aluno = a.id AND m.id_turma = t.id "
   return ler_bd(bd, query,(aluno,))

def alunos_de_uma_turma(bd,turma):
   query = "SELECT a.nome FROM media_aluno_turma m, aluno a, turma t WHERE t.codigo = ? AND m.id_aluno = a.id AND m.id_turma= t.id  "
   return ler_bd(bd, query,(turma,))

def quantidade_de_alunos(bd,turma):
   query = "SELECT COUNT(m.id_turma) FROM media_aluno_turma m, turma t WHERE t.nome=? AND m.id_turma=t.id"
   return ler_bd(bd, query,(turma,))

#aluno por id
#aluno por nome
#media por aluno
#selecionar medias dos alunos de uma turma
#selecionar alunos, turmas e suas medias
#alunos e suas turmas
#selecionar todas as medias dos alunos de uma turma
#notas acima de 7
#todas as medias dos alunos nas turma



