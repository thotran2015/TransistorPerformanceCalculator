from device_parameters import *
from formulas import *

si_mosfet = SiTransistor(0.4,1)
copper_wire = BigCopperWire()
gates_pipestages = 2**18 - 1
pipestages = 5
gatesNum = gates_pipestages*pipestages
app_cycles = 10**9

print("---COPPER WIRE---")
##### copper: tclock calc
Tclk_copper = calc_tclock(si_mosfet, copper_wire)*10**-6 #ns
Fclk_copper = 1/Tclk_copper #gigaHz
#####copper: waste energy 
E_lcopper = calc_wasteE_multigates_multicycles(si_mosfet, copper_wire, gatesNum, app_cycles) * 10**-9 #J
#####copper: dynamic energy
E_dcopper = calc_dymE_multigates_multicycles(si_mosfet, copper_wire, gatesNum, app_cycles) * 10**-15 #J
#####copper: total energy app consumed 
E_tcopper = E_lcopper + E_dcopper
###copper: EDP
EDP_big_copper = calc_EDP(si_mosfet, copper_wire, gatesNum)
print("Clock period (big_copper):", Tclk_copper, "ns")
print("Clock freq (big_copper):", Fclk_copper, "gigaHz")
print("Leaked energy (big_copper):", E_lcopper,"J")
print("Dynamic energy (big_copper):", E_dcopper, "J")
print("Energy consumed by app (big_copper):", E_tcopper, "J")
print("EDP (big_copper):", EDP_big_copper, "n^2Js")
