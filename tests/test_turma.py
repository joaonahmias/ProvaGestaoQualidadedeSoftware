from MockDB import MockBD
import sys
sys.path.insert(0, '..')
from ConexaoDB import *
from queries_turma import *

class Test_turma(MockBD):
    #def test_alunos_de_uma_turma(self):
        #r_esperado = [('Carla',), ('Lara',), ('Liryel',)]
        #self.assertEqual(alunos_de_uma_turma(self.mock_db_config.get('bd')),r_esperado)

    def test_medias_acima_de_9(self):
        r_esperado = [('Carla',), ('Lara',), ('Liryel',)]
        self.assertEqual(medias_acima_de_9(self.mock_db_config.get('bd')),r_esperado)
    
    def test_turmas_de_um_aluno(self):
        r_esperado = [("POO",),('Banco de Dados',),('Raciocinio Logico',)]
        aluna = 'Carla'
        self.assertEqual(turmas_de_um_aluno(self.mock_db_config.get('bd'),aluna),r_esperado)
        
    def test_alunos_de_uma_turma(self):
        r_esperado = [('Carla',),('Lara',),('Liryel',),('Danilo',),('Fernanda',)]
        self.assertEqual(alunos_de_uma_turma(self.mock_db_config.get('bd')),r_esperado)
