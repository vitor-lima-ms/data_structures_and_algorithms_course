from queue import Queue
from collections import deque

q = Queue()
q.put(1) #Coloca um elemento na fila
q.put(2)
q.put(3)
print(q.get()) #Remove e exibe na saida padrao o primeiro item colocado na fila. Nesse caso, o 1
print(q.get()) #Remove e exibe na saida padrao o segundo item colocado na fila. Nesse caso, o 2
print(q.get()) #Remove e exibe na saida padrao o terceiro item colocado na fila. Nesse caso, o 3

#No Python, a queue implementa os métodos de uma dequeue. Isso pode ser constatado a partir da documentação --> ctrl + mousel no q.put --> ctrl + mousel no self._put(item) --> ctrl + mousel no self.queue.append(item) --> O self.queue.append(item) na verdade é um método da classe dequeue

#Consultando a documentação do cpython no GitHub, é possível comprovar que a dequeue é implementada a partir de uma doubly linked list --> Garante que append e pop sejam realizados apenas nos itens que estão sendo adicionados ou removidos, garantindo a complexidade O(1)