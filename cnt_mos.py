from device_parameters import *
from formulas import *

cnt_mosfet = CNTTransistor(0.4,0.8)
copper_wire = CopperWire()

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
print("Clock period (CNT transistor):", Tclk_cnt, "ns")
print("Clock freq (CNT transistor):", Fclk_cnt, "gigaHz")
print("Leaked energy (CNT transistor):", E_lcnt,"J")
print("Dynamic energy (CNT transistor):", E_dcnt, "J")
print("Energy consumed by app (CNT transistor):", E_tcnt, "J")
