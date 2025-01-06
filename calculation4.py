import HF as hf
import Optimization as opt


# Calculation 4: Reaction energy of reaction HeH+ + H2 => He + H3+

natoms, charge, labels, z, coords = hf.ReadInput('input/He.input')
ETot = hf.HF_calculation(natoms, charge, labels, z, coords)

print(f"Total energy of Helium: {ETot}")
print("Calculation of reaction energy in report")

