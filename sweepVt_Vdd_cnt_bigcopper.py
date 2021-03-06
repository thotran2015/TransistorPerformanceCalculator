from device_parameters import *
from formulas import *

gates_pipestages = 2**18 - 1
pipestages = 5
gatesNum = gates_pipestages*pipestages
app_cycles = 10**9

copper_wire = BigCopperWire()

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step
print("---Sweeping Vdd and Vt for CNT Mosfet and large copper---")
cnts = []
EDP = {}
for vdd in frange (0.3,1.0,0.1):
    for vt in frange(0.1, vdd-0.1, 0.1):
        cnts.append(CNTTransistor(vt, vdd))
for cnt in cnts:
    EDP[calc_EDP(cnt, copper_wire, gatesNum)] = (cnt.Vt, cnt.Vdd)
print("best EDP, vt, vdd: ", min(EDP), "n^2Js,", EDP[min(EDP)][0], "V,", EDP[min(EDP)][1], "V")

Vt, Vdd = EDP[min(EDP)]
cnt_mosfet = CNTTransistor(Vt,Vdd)


gates_pipestages = 2**18 - 1
pipestages = 5
gatesNum = gates_pipestages*pipestages
app_cycles = 10**9
##print("---CNT Transistor---")
###cnt: tclock calc
Tclk_cnt = calc_tclock(cnt_mosfet, copper_wire) * 10**-6 #ns
Fclk_cnt = 1/Tclk_cnt
###cnt: waste energy 
E_lcnt = calc_wasteE_multigates_multicycles(cnt_mosfet, copper_wire, gatesNum, app_cycles) * 10**-9 #J
###cnt: dynamic energy
E_dcnt = calc_dymE_multigates_multicycles(cnt_mosfet, copper_wire, gatesNum, app_cycles) * 10**-15 #J
###cnt: total energy app consumed 
E_tcnt = E_lcnt + E_dcnt
print("Clock period (CNT transistor + big copper):", Tclk_cnt, "ns")
print("Clock freq (CNT transistor + big copper):", Fclk_cnt, "gigaHz")
print("Leaked energy (CNT transistor + big copper):", E_lcnt,"J")
print("Dynamic energy (CNT transistor + big copper):", E_dcnt, "J")
print("Energy consumed by app (CNT transistor + big copper):", E_tcnt, "J")
