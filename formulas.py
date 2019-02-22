import math
#calc tclock
LD = 18
FO = 2
ALPHA = 0.1
def calc_tclock(transistor, wire):
    Vdd = transistor.Vdd
    Ion = transistor.Ion
    Cin = transistor.Cin
    Cout = transistor.Cout
    Cw = wire.Cw
    Rw = wire.Rw
    Ron = Vdd/Ion  #ohms
    return LD*0.5*math.log2(2)*(Ron*(Cout+Cw+FO*Cin) + Rw*(0.5*Cw+FO*Cin)) #fs

#leak energy
def calc_wasteE_per_gate_cycle(transistor, tclock):
    Vdd = transistor.Vdd
    Ioff = transistor.Ioff
    Roff = Vdd/Ioff #ohms
    P_g = (Vdd**2)/Roff #watts
    return P_g*tclock #nJ

def calc_wasteE_multigates_multicycles(transistor,wire, gatesNum, cycles):
    tclock = calc_tclock(transistor, wire)*10**-6 
    return calc_wasteE_per_gate_cycle(transistor, tclock)*gatesNum*cycles #nJ

#dynamic energy
def calc_dymE_per_gate_cycle(transistor, wire):
    Cin = transistor.Cin
    Cout = transistor.Cout
    Vdd = transistor.Vdd
    Cw = wire.Cw
    return 0.5*(Cout+Cw+FO*Cin)*Vdd**2*ALPHA#fJ
   
def calc_dymE_multigates_multicycles(transistor, wire, gatesNum, cycles):
    return calc_dymE_per_gate_cycle(transistor, wire)*gatesNum*cycles #fJ

#calc EDP
def calc_EDP(transistor, wire, gatesNum):
    Tclk = calc_tclock(transistor, wire)
    E_per_cycle = (calc_wasteE_per_gate_cycle(transistor, Tclk) + calc_dymE_per_gate_cycle(transistor, wire))*gatesNum*Tclk
    return E_per_cycle
