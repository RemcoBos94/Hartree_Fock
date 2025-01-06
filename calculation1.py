import HF as hf
import Optimization as opt


# Calculation 1: Total Energy of H2

natoms, charge, labels, z, coords = hf.ReadInput('input/H2.input')
ETot, ET, EV, EJ, EK, ENuc, E_elec, iteration_logging = hf.HF_calculation_all(natoms, charge, labels, z, coords)

print(iteration_logging)
print("###########")
print("E_elec:", E_elec, "\n-----------")
print("ET:", ET, "\nEV:", EV, "\nEJ:", EJ, "\nEK:", EK, "\nENuc:", ENuc, "\nE_Elec + ENuc:", E_elec + ENuc, "\n>>> E(RHF):", ETot," <<<")