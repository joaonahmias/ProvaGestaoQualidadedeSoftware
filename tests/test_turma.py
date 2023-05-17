from turma import *
import unittest

class Test_turma(unittest.TestCase):
    def test_alunos_maior_nota(self):
        lista = [('Carla', 9.7),('Danilo', 6.7), ('Daniel', 3.4), ('Alice', 9.7), ('Flávio',5.7), ('Silvia', 4.4)]
        r_esperado = [('Carla'),('Alice')]
        lista2 = [('Carla', 9.0),('Danilo', 6.7), ('Daniel', 3.4), ('Alice', 10), ('Flávio',5.7), ('Silvia', 4.4)]
        r_esperado2 = [('Alice')]
        self.assertEqual(alunos_maior_nota(lista),r_esperado)
        self.assertEqual(alunos_maior_nota(lista2),r_esperado2)
    
    def test_disciplinas_a_pagar(self):
        lista_disciplinas = [('TAD0055'), ('TAD0010'),('TAD0002'), ('TAD0001'), ('TAD1002'), ('TAD0100'), ('TAD0027'), ('TAD0105'),('TAD0202'), ('TAD2030')]
        lista_aluno = [('TAD0055',9.7), ('TAD0010', 6.7), ('TAD0105', 3.4), ('TAD0105', 4.4),('TAD0105', 7.1), ('TAD0027', 9.7), ('TAD0202', 5.7), ('TAD0001',4.4)]
        r_esperado = [('TAD0010'),('TAD0002'),('TAD0001'),('TAD1002'),('TAD0100'),('TAD0202'),('TAD2030')]
        lista_aluno2 = [('TAD0055',7), ('TAD0010',7),('TAD0002',7), ('TAD0001',7), ('TAD1002',7), ('TAD0100',7), ('TAD0027',7), ('TAD0105',7),('TAD0202',7), ('TAD2030',7)]
        r_esperado2 = []
        self.assertEqual(disciplinas_a_pagar(lista_aluno,lista_disciplinas),r_esperado)
        self.assertEqual(disciplinas_a_pagar(lista_aluno2,lista_disciplinas),r_esperado2)
                           
    def test_medias_turmas_professores(self):
        lista = [('TAD0055', 1, 9.7), ('TAD0010', 2, 6.7), ('TAD0105', 3, 3.4), ('TAD0105', 1, 4.4), ('TAD0105', 2, 7.1), ('TAD0027', 2, 9.7), ('TAD0202', 3, 5.7), ('TAD0001', 3, 4.4)]
        r_esperado =  [(1, 7.05), (2, 7.83), (3,4.5)]
        lista2 = []
        r_esperado2 =  []
        self.assertEqual(medias_turmas_professores(lista),r_esperado)
        self.assertEqual(medias_turmas_professores(lista2),r_esperado2)
                           


