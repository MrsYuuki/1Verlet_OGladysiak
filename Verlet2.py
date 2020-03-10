import math
import numpy as np


class ATOM:
    def __init__(self, Xn, Vn, F_wypadkowa, czy_nieruchomy=True):
        self.Xn = Xn                                                    #Lista x,y.
        self.Vn = Vn
        self.czy_nieruchomy = czy_nieruchomy
        self.F_wypadkowa = F_wypadkowa

    m = 0.1
    G = 0.01
    M = 500.0
    dt = 0.001

    def get_Xn(self):
        return self.Xn

    def get_Vn(self):
        return self.Vn

    def set_Xn(self, item):
        self.Xn = item

    def set_Vn(self, item, n):
        self.Vn[n] = item

    def policz_sile(self, X1n2, X2n2):
        r = math.sqrt((X1n2 - self.Xn[0]) ^ 2 + (X2n2 - self.Xn[1]) ^ 2)
        F = self.G * ((self.M * self.m) / (r*r))
        print (F)
        print("Wartosc sily to:", F)
        return F


class SIMUL:
    def __init__(self, atoms, dt=0.001, integration_method="E", liczba_krokow=10):
        self.atoms = atoms                                                   #Wstepnie lista 2 atomow.
        self.integration_method = integration_method
        self.dt = dt
        self.liczba_krokow = liczba_krokow

        #n = 0

    def Euler(self, m=0.1):
        F = self.atoms[0].policz_sile(self.atoms[1].get_Xn()[0], self.atoms[1].get_Xn()[1])
        Xnpx = self.atoms[0].get_Xn()[0] + self.atoms[0].get_Vn()*self.dt + (F/(2*m))*self.dt**2
        Xnpy = self.atoms[0].get_Xn()[1] + self.atoms[0].get_Vn()*self.dt + (F/(2*m))*self.dt**2
        self.atoms[0].set_Xn([Xnpx, Xnpy])
        Vnpx = self.atoms[0].get_Vn()[0] + (F/m)*self.dt
        Vnpy = self.atoms[0].get_Vn()[1] + (F/m)*self.dt
        self.atoms[0].set_Vn(Vnpx, Vnpy)

    def Verlet(self, m=0.1, krok=0):
        F = self.atoms[0].policz_sile(self.atoms[1].get_Xn()[0], self.atoms[1].get_Xn()[1])
        if krok == 0:
            r1x = self.atoms[0].get_Xn[0] + 2 * self.atoms[0].get_Vn()[0] * self.dt + (F / m) * self.dt ** 2   #To liczymy na poczatku.
            r1y = self.atoms[0].get_Xn[1] + 2 * self.atoms[0].get_Vn()[1] * self.dt + (F / m) * self.dt ** 2    #Tez warunek poczatkowy.
        else:
            

    def simulation(self):
        ruch_atomu = []                         #lista zmian w postaci atomow (mozna wybrac z niej pozniej predkosc i polozenie)
        ruch_atomu.append(atoms[0])
        iteracja = 0

        if integration_method == "E":
            while liczba_krokow != iteracja:
                SIMUL.Euler()
                iteracja += 1
                ruch_atomu.append(atoms[0])


Atom1 = ATOM([1,1], [0,0], "losowa",True)
Atom1.policz_sile(4, 4)
Atom2 = ATOM([1,1], [1,1], "losowa", True)
Atom3 = ATOM([2,2], [3,3], "losowa", True)
Simul1 = SIMUL([Atom1, Atom2, Atom3], "Verlet")
Simul1.Verlet(0.001,0.1,0.125)
print(Atom3.get_Xn())