import math
#calc Cgate (depends on transistor)
def calc_Cgate(k, eps, W, L, d):
    A = L*W*10**3 #nm^2
    return (k*eps*A/d)*10**6 #fF

class SiTransistor:
    def __init__(self, Vt, Vdd):
        self.Vt = Vt
        self.Vdd = Vdd
        self.W = 2 #um
        self.L = 200 #nm
        self.d = 5 #nm
        self.Kon = 0.0004 #A/(um*V**2)
        self.Koff = 1 #A/um
        self.kT_q = 25 #mV
        self.k = 3.8 #relative permitivity of SiO2
        self.eps = 8.854*10**-12 #F/m
        self.Cin = calc_Cgate(self.k, self.eps, self.W, self.L, self.d) #fF
        self.Cout = self.Cin/4 #fF
        self.Ion = self.W*self.Kon*(self.Vdd-self.Vt)**2 #A
        self.Ioff = self.W*self.Koff*math.exp(-self.Vt/(self.kT_q * 10**-3)) #A

class CopperWire:
    # Copper Wire
    Cw_um = 0.15 #fF/um
    Rw_um = 20 #ohms/um
    Lw = 60 #um
    Cw = Cw_um * Lw # fF
    Rw = Rw_um * Lw #ohms

class BigCopperWire:
    # Copper Wire
    copper = CopperWire()
    Rw_copper = copper.Rw
    Cw_copper = copper.Cw
    Cw = 100*Cw_copper  # fF
    Rw = 100*Rw_copper #ohms
    
class GrapheneWire:
    copper = CopperWire()
    Rw_copper = copper.Rw
    Cw_copper = copper.Cw
    Rw = Rw_copper/100 #ohms
    Cw = 0.5*Cw_copper # fF

class CNTTransistor:
    def __init__(self, Vt, Vdd):
        self.W = 2 #um
        self.d = 5 #nm
        self.Kon_si =  SiTransistor(Vt, Vdd).Kon #A/(um*V**2)
        self.L = 40 #nm
        self.Kon = 2*self.Kon_si #A/(um*V**2)
        self.Koff = 1 #A/um
        self.Vdd = Vdd #V
        self.Vt = Vt #V
        self.k = 3.8 #relative permitivity of SiO2
        self.eps = 8.854*10**-12 #F/m
        self.Cin = calc_Cgate(self.k, self.eps, self.W, self.L, self.d)
        self.Cout = self.Cin/4 #fF
        self.Ion = self.W*self.Kon*(self.Vdd-self.Vt)**2 #A
        self.kT_q = 25 #mV
        self.Ioff = self.W*self.Koff*math.exp(-self.Vt/(self.kT_q * 10**-3)) #A
