import HF as hf
import Optimization as opt


# Calculation 3: Optimization of H3+

natoms, charge, labels, z, coords = hf.ReadInput('input/H3+.input')
opt.Optimize_coordinates(natoms, charge, labels, z, coords)
print("Calculation of bond lengths and angle in report")