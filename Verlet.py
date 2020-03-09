import math


class ATOM:
    def __init__(self, Xn, Vn,F_wypadkowa, czy_nieruchomy = True):
        self.Xn = Xn                                                    #jak dziala wektor zmiennych
        self.Vn = Vn
        self.czy_nieruchomy = czy_nieruchomy
        self.F_wypadkowa = F_wypadkowa

    m = 0.1
    G = 0.01
    M = 500.0
    deltat = 0.001

    def get_Xn(self):
        return self.Xn[0]

    def set_Xn(self, item):
        self.Xn[0] = item

    def set_Vn(self, item):
        self.Vn[0] = item

    def policz_sile(self, X1n2, X2n2):
        r = math.sqrt((X1n2 - self.Xn[0]) ^ 2 + (X2n2 - self.Xn[1]) ^ 2)
        F = self.G * ((self.M * self.m) / (r*r))
        print (F)
        print("Wartosc sily to:", F)
        return F

    def oblicz_XvV(self):
        SIMUL.Verlet(())
        return 0

class SIMUL:
    def __init__(self, ATOMS, integration_method):
        self.ATOMS = ATOMS
        self.integration_method = integration_method
        Atom1 = self.ATOMS[0]
        Atom2 = self.ATOMS[1]
        Atom3 = self.ATOMS[2]
        #n = 0

    def Verlet(self, dt, m, Fn):
        Atom1 = self.ATOMS[0]
        Atom2 = self.ATOMS[1]
        Atom3 = self.ATOMS[2]
        Xnp1 = 2*Atom2.get_Xn() - Atom1.get_Xn() + (Fn/m)*dt
        Atom3.set_Xn(Xnp1)
        Vnp1 = (1/(2*dt))*(Xnp1 - Atom1.get_Xn())
        Atom3.set_Vn(Vnp1)
        #self.Atom1 = ATOMS[n+1]
        #self.Atom2 = ATOMS[n+2]
        #self.Atom3 = ATOMS[n+3]
        #self.n+=1

Atom1 = ATOM([1, 1], [0, 0],"losowa", True)
Atom1.policz_sile(4, 4)
Atom2 = ATOM([1,1],[1,1], "losowa", True)
Atom3 = ATOM([2,2],[3,3], "losowa", True)
Simul1 = SIMUL([Atom1, Atom2, Atom3], "Verlet")
Simul1.Verlet(0.001,0.1,0.125)
print(Atom3.get_Xn())