# NOVEMBER
**November** (implemeNtatiOn of VErbose aMBER) is a custom implementation of the AMBER forcefield, inspired by [OpenMM](https://github.com/openmm/openmm)'s C++ source. November's aim is not to be performant, but rather to be compact and easy to modify/customize. It also provides by default the option to obtain verbose outputs, i.e. the energies of every singular molecular interaction in arrays (instead of their sum).

* Current outputs supported:
    * Bonded energies
    * Angle energies
    * Dihedral (Torsion) energies
    * LennardJones energies
    * Coulomb energies

* Current forcefield formats supported:
    * XML

* Current forcefields packed along November (at `november/_data`):
    * `RNA.OL3.xml`


# TODO
* remove OpenMM dependency
* improve `bond_graphs`'s graph data structure
