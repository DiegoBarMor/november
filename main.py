import sys

import november as nov

################################################################################
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_pdb> [<folder_output>]")
        sys.exit(1)

    PATH_PDB = sys.argv[1]
    PATH_XML = "november/_data/RNA.OL3.xml"

    calc = nov.EnergyCalculator(PATH_PDB, PATH_XML).calc_energies_rna()

    if len(sys.argv) >= 3:
        FOLDER_OUTPUT = sys.argv[2]
        calc.save_energy_arrays(FOLDER_OUTPUT)

    else:
        calc.display_energies()


################################################################################
