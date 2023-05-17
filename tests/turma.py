def alunos_maior_nota(lista):
    cont = 0
    resultado=[]
    for elemento in lista:
        if(cont==0):
            maior = elemento[1]
        if(elemento[1]>maior):
            maior = elemento[1]
        cont+=1
    for elemento in lista:
        if elemento[1]==maior:
            resultado.append(elemento[0])
    return resultado

def disciplinas_a_pagar(lista_aluno,lista_disciplinas):
    disciplinas_aprovadas =[]
    resultado=[]
    for elemento in lista_aluno:
        if elemento[1]>=7:
            disciplinas_aprovadas.append(elemento[0])
    for elemento in lista_disciplinas:
        if elemento not in disciplinas_aprovadas:
            resultado.append(elemento)
    return resultado

def medias_turmas_professores(lista):
    professores = []
    medias = []
    quantidade_turmas = []
    resultado = []
    for elemento in lista:
        if elemento[1] not in professores:
            professores.append(elemento[1])
            medias.append(elemento[2])
            quantidade_turmas.append(1)
        else:
            indice = professores.index(elemento[1])
            medias[indice]+=elemento[2]
            quantidade_turmas[indice]+=1
    cont = 0
    for elemento in professores:
        resultado.append((elemento,round(medias[cont]/quantidade_turmas[cont],2)))
        cont+=1
    return resultado




