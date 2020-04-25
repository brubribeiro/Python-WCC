#Bruna Ribeiro - 28/11/2019

from abc import ABC, abstractmethod

class Poligono(ABC):

  def noofsides(self):
    pass

class Triangulo(Poligono):

  def noofsides(self):
    print('Eu tenho 3 lados!')
  
class Pentagono(Poligono):

  def noofsides(self):
    print('Eu tenho 5 lados!')

class Hexagono(Poligono):

  def noofsides(self):
    print('Eu tenho 6 lados!')

class Quadrilatero(Poligono):

  def noofsides(self):
    print('Eu tenho 4 lados!')

T = Triangulo()
T.noofsides()

P = Pentagono()
P.noofsides()

H = Hexagono()
H.noofsides()

Q = Quadrilatero()
Q.noofsides()
