from unittest import TestCase

import sys
sys.path.insert(0, '..')
from ConexaoDB import *

BD = "TestBD.db"

class MockBD(TestCase):
    @classmethod
    def setUpClass(cls):
        con = conectar(BD)
        cursor = con.cursor()

        query_create_professor = """CREATE TABLE professor (
                                  id int NOT NULL PRIMARY KEY ,
                                  nome text NOT NULL
                                )"""
        query_create_turma = """CREATE TABLE turma (
                                  id int NOT NULL PRIMARY KEY ,
                                  nome text NOT NULL,
                                  codigo int NOT NULL
                                )"""
        query_create_aluno = """CREATE TABLE aluno  (
                                  id int NOT NULL PRIMARY KEY ,
                                  nome text NOT NULL
                                )"""
        query_create_media_aluno_turma = """CREATE TABLE Media_aluno_turma  (
                                  id int NOT NULL PRIMARY KEY ,
                                  id_turma int NOT NULL,
                                  id_aluno int NOT NULL,
                                  nota1 int NOT NULL,
                                  nota2 int NOT NULL,
                                  nota3 int NOT NULL,
                                  media int NOT NULL,
                                  FOREIGN KEY (id_turma) REFERENCES turma(id),
                                  FOREIGN KEY (id_aluno) REFERENCES aluno(id)
                                )"""
        try:
            cursor.execute(query_create_professor)
            cursor.execute(query_create_turma)
            cursor.execute(query_create_aluno)
            cursor.execute(query_create_media_aluno_turma)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")

        query_insert_professor =  """INSERT INTO professor (id, nome) VALUES
                                    (1, 'Nahmias'),
                                    (2, 'Guilherme'),
                                    (3, 'Judilena'),
                                    (4, 'Romulo')"""
        query_insert_turma = """INSERT INTO turma (id,nome,codigo) VALUES
                                    (1, 'POO', 'TAD0203'),
                                    (2, 'Banco de Dados','TAD0102'),
                                    (3, 'Raciocinio Logico','TAD0000'),
                                    (4, 'Algoritmos','TAD2222')"""
        query_insert_aluno = """INSERT INTO aluno (id,nome) VALUES
                                    (1, 'Carla'),
                                    (2, 'Lara'),
                                    (3, 'Liryel'),
                                    (4, 'Danilo'),
                                    (5, 'Fernanda'),
                                    (6, 'Julia')"""
        query_insert_media_aluno_turma = """INSERT INTO media_aluno_turma (id,id_turma,id_aluno,nota1,nota2,nota3,media) VALUES
                                    (1,1,1,9,9,9,9),
                                    (2,1,2,8.5,9,10,9.1),
                                    (3,1,3,10,10,10,10),
                                    (4,1,4,7,7,7,7 ),
                                    (5,1,5,6,6,6,6),
                                    (6,2,6,6.5,7,7.5,7),
                                    (7,2,1,7,7,7,7),
                                    (8,3,1,8,8,8,8),
                                    (9,4,5,5.5,9.5,7,7.3),
                                    (10,4,6,6,6,6,6)"""
        try:
            cursor.execute(query_insert_professor)
            cursor.execute(query_insert_turma)
            cursor.execute(query_insert_aluno)
            cursor.execute(query_insert_media_aluno_turma)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na inserção de dados:", error)
        else:
            print("Inserção dos dados: OK")

        cursor.close()

        desconectar(con)

        testconfig ={
            'bd': BD
        }
        cls.mock_db_config = testconfig

    @classmethod
    def tearDownClass(cls):
        print("TearDown")
        con = conectar(BD)
        cursor = con.cursor()

        try:
            cursor.execute("DROP TABLE professor")
            cursor.execute("DROP TABLE turma")
            cursor.execute("DROP TABLE aluno")
            cursor.execute("DROP TABLE media_aluno_turma")
            con.commit()
            cursor.close()
            print("Removeu os dados das tabelas.")
        except sqlite3.Error as error:
            print("Banco de dados não existe. Erro na remoção do BD.", error)
        finally:
            desconectar(con)



