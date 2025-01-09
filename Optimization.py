import numpy as np
import scipy as sp
import HF as hf

def Optimize_bond_length(natoms, charge, labels, z, coords, step=0.001):
    # first part => finding energies going up
    ETot = hf.HF_calculation(natoms, charge, labels, z, coords)
    bonding_length_ini = coords[1,2]
    print("#################################################")
    print(f"For bond length {bonding_length_ini} the Total energy is {ETot}")
    coords_up = np.copy(coords)
    coords_down = np.copy(coords)
    coords_up[1,2] = coords[1,2] + step
    coords_down[1,2] = coords[1,2] - step
    ETot_new_up = hf.HF_calculation(natoms, charge, labels, z, coords_up)
    ETot_new_down = hf.HF_calculation(natoms, charge, labels, z, coords_down)
    if (ETot_new_up > ETot and ETot_new_down < ETot):
        minimum = False
        while minimum == False:
            coords_down = np.copy(coords)
            coords_down[1,2] = coords[1,2] - step
            ETot_new_down = hf.HF_calculation(natoms, charge, labels, z, coords_down)
            if ETot_new_down > ETot:
                minimum = True
            else:
                coords = coords_down
                ETot = ETot_new_down
        print("#################################################")
        print("Minimum has been found lower than initial bond length") 
        print(f"Initial bonding length: {bonding_length_ini}")
        print(f"Optimized bonding length: {coords[1,2]}")
        print(f"Energy: {ETot}")
    elif (ETot_new_up < ETot and ETot_new_down > ETot):
        minimum = False
        while minimum == False:
            coords_up = np.copy(coords)
            coords_up[1,2] = coords[1,2] + step
            ETot_new_up = hf.HF_calculation(natoms, charge, labels, z, coords_up)
            if ETot_new_up > ETot:
                minimum = True
            else:
                coords = coords_up
                ETot = ETot_new_up
        print("#################################################")
        print("Minimum has been found higher than initial bond length") 
        print(f"Initial bonding length: {bonding_length_ini}")
        print(f"Optimized bonding length: {coords[1,2]}")
        print(f"Energy: {ETot}")
    elif (ETot_new_up > ETot and ETot_new_down > ETot):
        print("we already are in a minimum")   
    else:
        print("we are on a maximum")
    
    
def find_minimum_recursive(natoms, charge, labels, z, coords, ETot, step=0.001):
    steps = [0, step, -step]
    values = [0,1,2]
    ETot_copy = np.copy(ETot)
    for A in values:
        for B in values:
            for C in values:
                coords_new = np.copy(coords)
                coords_new[1,0] = coords[1,0] + steps[A]
                coords_new[2,0] = coords[2,0] + steps[B]
                coords_new[2,1] = coords[2,1] + steps[C]
                global counter
                global results
                counter += 1
                if (counter > 200):
                    break
                ETot_new = hf.HF_calculation(natoms, charge, labels, z, coords_new)
                if(ETot_new < ETot_copy):
                    find_minimum_recursive(natoms, charge, labels, z, coords_new, ETot_new)
                else:
                    if(results[1] > ETot_copy):
                        results = (coords_new, ETot_copy)
                        print(f"Lowest calculated energy at the moment: {results[1]}")
                        print(f"with coordinates:\n{results[0]}")
                        print("Searching for lower energies...\n")
                        counter = 0
                

def Optimize_coordinates(natoms, charge, labels, z, coords):
    ETot = hf.HF_calculation(natoms, charge, labels, z, coords)
    global results
    global counter
    counter = 0
    results = [coords, ETot]
    find_minimum_recursive(natoms, charge, labels, z, coords, ETot, step=0.001)
    print("##############################################")
    print(f"Lowest energy: {results[1]}")
    print(f"with coordinates:\n {results[0]}")