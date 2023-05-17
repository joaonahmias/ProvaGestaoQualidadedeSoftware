from MockDB import MockBD
import sys
sys.path.insert(0, '..')
from ConexaoDB import *
from queries_turma import *

class Test_turma(MockBD):

    def test_maior_media_de_turma(self):
        turma = 'TAD0203'
        r_esperado =[(10,)]
        self.assertEqual(maior_media_de_turma(self.mock_db_config.get('bd'),turma),r_esperado)
        turma2 = 'TAD0000'
        r_esperado = [(None,)]
        self.assertEqual(maior_media_de_turma(self.mock_db_config.get('bd'),turma2),r_esperado)


    def test_turmas_de_um_aluno(self):
        aluna = 'Carla'
        r_esperado = [('POO',9),('Banco de Dados',7),('Algoritmos',8)]
        self.assertEqual(turmas_de_um_aluno(self.mock_db_config.get('bd'),aluna),r_esperado)
        aluna2 = 'Giovana'
        r_esperado2 = []
        self.assertEqual(turmas_de_um_aluno(self.mock_db_config.get('bd'),aluna2),r_esperado2)
        aluna3 = 'Julia'
        r_esperado3 = []
        self.assertEqual(turmas_de_um_aluno(self.mock_db_config.get('bd'),aluna3),r_esperado3)
        
    def test_quantidade_disciplinas_aluno(self):
        aluna = 'Carla'
        r_esperado = [(3,)]
        self.assertEqual(quantidade_disciplinas_aluno(self.mock_db_config.get('bd'),aluna),r_esperado)
        aluna2 = "Giovana"
        r_esperado2 = [(0,)]
        self.assertEqual(quantidade_disciplinas_aluno(self.mock_db_config.get('bd'),aluna2),r_esperado2)
        aluna3 = 'Julia'
        r_esperado3 = [(0,)]
        self.assertEqual(quantidade_disciplinas_aluno(self.mock_db_config.get('bd'),aluna3),r_esperado3)
