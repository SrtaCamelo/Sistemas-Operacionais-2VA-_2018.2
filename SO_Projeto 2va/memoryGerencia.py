#Projeto Sistemas Operacionais 2018.2
#Fabio e Raissa
#Gerenciamento de Memória


#Imports
from random import shuffle

#Define Functions

# exemplo de entrada print(calculadora("12+34-+"))
def calculadora(equacao):
	stack = []
	a = b = 0
	for c in equacao:
		if c == '-':
			if len(stack) != 0:
				b = stack.pop()
				a = stack.pop()
				stack.append(a-b)
		elif c == '+':
			if len(stack) != 0:
				b = stack.pop()
				a = stack.pop()
				stack.append(a+b)
		elif c == '*':
			if len(stack) != 0:
				b = stack.pop()
				a = stack.pop()
				stack.append(a*b)
		elif c == '/':
			if len(stack) != 0:
				b = stack.pop()
				a = stack.pop()
				if b != 0:
					stack.append(a/b)
		elif c == '^':
			if len(stack) != 0:
				b = stack.pop()
				a = stack.pop()
				if b != 0:
					stack.append(a**b)
		else:
			stack.append(ord(c)-48)

	return stack.pop()

#---------Open FIle-----------
"""
Abre o Arquivo txt onde estão os processos (Equações)
Retorna uma Lista de Processos aleatórizada
"""

memory = []
index = []
lista_processo = []
#size = 0
def openfile(path):
    lines = [line.rstrip('\n') for line in open(path)]
    return lines
def calculateCost(proc):
    #print(proc)
    result = ''.join([i for i in proc if not i.isdigit()])
    #print(result)
    cost = 0
    for i in result:
        if i == '+' or i =='-':
            cost += 1
        elif i == '*' or i =='/':
            cost += 3
        elif i == '^':
            cost += 5
    return cost
def inicialize_memory():
    for n in range(50):
        memory.append(0)
        index.append(0)
def cleanFromMemory(id):
    for i in range(len(memory)):
        if memory[i] == id:
            memory[i] = 0
def calculateExpressionFromID(id):
    true_id = id-1
    equation = lista_processo[true_id]
    result = calculadora(equation)
    print(equation)
    print(result)
def calculateFrommemory():
    for id in memory:
        if id != 0:
            calculateExpressionFromID(id)
            cleanFromMemory(id)
def incert_into_memory(id, cost):
    insert_with_sucess = 1
    index_start = 0
    index_fim = 0
    pointer = 0
    count = 0
    the_end = 0
    for slot in index:
        if count == cost:
            index_fim = pointer
            the_end = 1
        if the_end == 0:
            if slot == 0:
                count += 1
            else:
                count = 0
                index_start = pointer +1

            pointer += 1
            if pointer == 49 and count != cost:
                insert_with_sucess = 0
                #print("no Space")
            elif pointer == 49 and count == cost:
                index_fim = pointer

    #print(index_start,index_fim, cost)
    if insert_with_sucess == 1:
        #print("Inserted")
        for i in range(index_start,index_fim+1):
            memory[i] = id
            index[i] = 1


#----------------Main-------------
path = "equations.txt"
inicialize_memory()
lista_processo = openfile(path)
id = 1
for proc in lista_processo:
    #print(proc)
    size = calculateCost(proc)
    incert_into_memory(id, size)
    calculateFrommemory()
    id += 1
"""
index [0] = 1
index [1] = 1
index [2] = 1
index [5] = 1
index [6] = 1
index [7] = 1

memory [0] = 1
memory [1] = 1
memory [2] = 1
memory [5] = 3
memory [6] = 3
memory [7] = 3
incert_into_memory(2,5)

for i in memory:
    print(i)
"""