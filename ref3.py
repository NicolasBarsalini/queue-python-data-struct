'''
ENGLISH BELLOW!

Exercício 3: Intercale uma Fila
Objetivo: Dada uma fila com um número par de elementos, reorganize-a de modo
que a segunda metade esteja intercalada com a primeira metade.
Descrição:
Escreva uma função que recebe uma Fila contendo um número par de elementos.
A função deve reorganizar a fila de forma que o primeiro elemento seja seguido pelo
elemento do meio, seguido pelo segundo elemento, pelo próximo elemento do
meio, e assim por diante.
Por exemplo, para a fila 1 2 3 4 5 6, a fila reorganizada deve ser 1 4 2 5 3 6.
A função não precisa retornar um valor, mas a fila original deve estar reorganizada
ao final da execução.
Dicas:
Considere o uso de uma pilha ou recursão para ajudar a reorganizar os elementos.
Você pode precisar de uma ou mais estruturas de dados temporárias para armazenar
elementos da fila durante o processo de reorganização.

ENGLISH:
Exercise 3: Interleave a row
Objective: Given a queue with an even number of elements, rearrange it so
that the second half is interspersed with the first half.
Description:
Write a function that takes a Queue containing an even number of elements.
The function must rearrange the queue so that the first element is followed by the
middle element, followed by the second element, the next element in the
middle, and so on.
For example, for queue 1 2 3 4 5 6, the rearranged queue should be 1 4 2 5 3 6.
The function does not need to return a value, but the original queue must be reorganized
at the end of execution.
ROW
Prof. Kleber Dias (Kbça)
Exercise 3: Interleave a Row
Tips:
Consider using a stack or recursion to help rearrange elements.
You may need one or more temporary data structures to store
queue elements during the reorganization process.
'''
from Queue import Queue # importing the queue class

def reorganize_queue(queue): # defining the function to reorganize the queue
    if queue.is_empty():
        return

    width = 0
    tmp_queue = Queue()

    while not queue.is_empty(): # discovering the queue's width
        tmp_queue.push(queue.pop())
        width = width + 1

    if width % 2 != 0: # checking if the width is an even number, if it is not, raise an Exception
        raise Exception("[ERROR] The queue width must be an even number!")
    
    for _ in range(int(width/2)): 
        queue.push(tmp_queue.pop())

    while not tmp_queue.is_empty(): # pushing the elements to the queue, reorganizing it!
        queue.push(queue.pop())
        queue.push(tmp_queue.pop())
    
    while not queue.is_empty():
        print(queue.pop(), end = " ")

if __name__ == '__main__': # callig the function to reorganize and passing a queue as argument!
    queue = Queue()

    for i in range(1,7):
        queue.push(i)

    reorganize_queue(queue)

    while not queue.is_empty():
        print(queue.pop(), end=" ")