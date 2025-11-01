import sys

import november as nov

################################################################################
if __name__ == "__main__":
    PATH_PDB = sys.argv[1]
    PATH_XML = "november/_data/RNA.OL3.xml"

    nov.EnergyCalculator(PATH_PDB, PATH_XML) \
        .calc_energies_rna() \
        .display_energies()


################################################################################
