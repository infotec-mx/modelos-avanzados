import sys
from ortools.graph import pywrapgraph

costos = {
    (0,1):6, (0,2):2, (0,4):10, 
    (1,3):3, (1,5):9,
    (2,1):3, (2,3):7, (2,4):9,
    (3,4):2, (3,5):6, 
    (4,3):1, (4,5):3
}

mcf = pywrapgraph.SimpleMinCostFlow()

for k,v in costos.items():
    mcf.AddArcWithCapacityAndUnitCost(
        k[0], k[1], sys.maxsize, v
        )
    
for i in range(6): 
    if i == 0: 
        mcf.SetNodeSupply(i, 1)
    elif i == 5:
        mcf.SetNodeSupply(i, -1)
    else: 
        mcf.SetNodeSupply(i, 0)