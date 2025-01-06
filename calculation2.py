import HF as hf
import Optimization as opt


# Calculation 2: Optimization bond length He-H

natoms, charge, labels, z, coords = hf.ReadInput('input/HeH+.input')
opt.Optimize_bond_length(natoms, charge, labels, z, coords)

