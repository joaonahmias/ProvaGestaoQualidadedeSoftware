from ConexaoDB import *

def maior_media_de_turma(bd,turma):
   query = "SELECT MAX(m.media) FROM media_aluno_turma m , turma t WHERE t.codigo =? AND m.id_turma=t.id"
   return ler_bd(bd, query,(turma,))

def turmas_de_um_aluno(bd,aluno):
   query = "SELECT t.nome, m.media  FROM media_aluno_turma m, aluno a, turma t WHERE a.nome = ? AND m.id_aluno = a.id AND m.id_turma = t.id "
   return ler_bd(bd, query,(aluno,))

def quantidade_disciplinas_aluno(bd,aluno):
   query = "SELECT count(m.id_turma) FROM media_aluno_turma m, aluno a, turma t WHERE a.nome = ? AND m.id_turma = t.id AND m.id_aluno=a.id"
   return ler_bd(bd,query,(aluno,))


