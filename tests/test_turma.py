from MockDB import MockBD
import sys
sys.path.insert(0, '..')
from ConexaoDB import *
from queries_turma import *

class Test_turma(MockBD):

    def test_medias_acima_de_9(self):
        r_esperado = [('Carla',), ('Lara',), ('Liryel',)]
        self.assertEqual(medias_acima_de_9(self.mock_db_config.get('bd')),r_esperado)
    
    def test_turmas_de_um_aluno(self):
        aluna = 'Carla'
        r_esperado = [('POO',),('Banco de Dados',),('Algoritmos',)]
        self.assertEqual(turmas_de_um_aluno(self.mock_db_config.get('bd'),aluna),r_esperado)
        aluna2 = 'Giovana'
        r_esperado2 = []
        self.assertEqual(turmas_de_um_aluno(self.mock_db_config.get('bd'),aluna2),r_esperado2)
        aluna3 = 'Julia'
        r_esperado3 = []
        self.assertEqual(turmas_de_um_aluno(self.mock_db_config.get('bd'),aluna3),r_esperado3)
        
        
    def test_alunos_de_uma_turma(self):
        turma = 'TAD0203'
        r_esperado = [('Carla',),('Lara',),('Liryel',),('Danilo',),('Fernanda',)]
        self.assertEqual(alunos_de_uma_turma(self.mock_db_config.get('bd'),turma),r_esperado)
        turma2 = 'Racicionio Logico'
        r_esperado2 = []
        self.assertEqual(alunos_de_uma_turma(self.mock_db_config.get('bd'),turma2),r_esperado2)
        turma3 = 'Autoria Web'
        r_esperado3 = []
        self.assertEqual(alunos_de_uma_turma(self.mock_db_config.get('bd'),turma3),r_esperado3)
    
    def test_quantidade_de_alunos(self):
        turma = 'POO'
        r_esperado = [(5,)]
        self.assertEqual(quantidade_de_alunos(self.mock_db_config.get('bd'),turma),r_esperado)