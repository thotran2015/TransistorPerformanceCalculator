from device_parameters import *
from formulas import *

si_mosfet = SiTransistor(0.4,1)
graphene_wire = GrapheneWire()
gates_pipestages = 2**18 - 1
pipestages = 5
gatesNum = gates_pipestages*pipestages
app_cycles = 10**9

##print("---GRAPHENE WIRE---")
### graphene: tclock calc
Tclk_graphene = calc_tclock(si_mosfet, graphene_wire)*10**-6 #ns
Fclk_graphene = 1/Tclk_graphene 
###graphene: waste energy
E_lgrap = calc_wasteE_multigates_multicycles(si_mosfet,graphene_wire, gatesNum, app_cycles) * 10**-9 #J
###graphene: dynamic energy
E_dgrap = calc_dymE_multigates_multicycles(si_mosfet, graphene_wire, gatesNum, app_cycles) * 10**-15 #J
###graphene: total energy app consumed 
E_tgrap = E_lgrap + E_dgrap
###graphene: EDP
EDP_grap = calc_EDP(si_mosfet, graphene_wire, gatesNum)
print("Clock period (graphene):", Tclk_graphene, "ns")
print("Clock freq (graphene):", Fclk_graphene, "gigaHz")
print("Leaked energy (graphene):", E_lgrap, "J")
print("Dynamic energy (graphene):", E_dgrap, "J")
print("Energy consumed by app (graphene):", E_tgrap, "J")
print("EDP (graphene):", EDP_grap, "n^2Js")


