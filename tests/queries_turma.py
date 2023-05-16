from ConexaoDB import *

def alunos_de_uma_turma(bd):
    return ler_bd(bd, "SELECT a.nome FROM media_aluno_turma m, turma t, aluno a WHERE t.codigo = 'TAD0203' ")

def medias_acima_de_9(bd):
    return ler_bd(bd,"SELECT a.nome FROM media_aluno_turma m, aluno a WHERE media >=9 AND  m.id_aluno = a.id ")

def turmas_de_um_aluno(bd,aluno):
   query = "SELECT t.nome FROM media_aluno_turma m, aluno a, turma t WHERE a.nome = ? AND m.id_aluno = a.id AND m.id_turma = t.id "
   return ler_bd(bd, query,(aluno,))

def alunos_de_uma_turma(bd):
   query = "SELECT a.nome FROM media_aluno_turma m, aluno a, turma t WHERE t.codigo = 'TAD0203' AND m.id_aluno = a.id AND m.id_turma= t.id  "
   return ler_bd(bd, query)



