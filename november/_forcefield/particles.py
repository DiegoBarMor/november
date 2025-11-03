# //////////////////////////////////////////////////////////////////////////////
class FFAtomType:
    def __init__(self, atom_class: str, element: str, mass: float, name: str):
        self.atom_class = atom_class
        self.element = element
        self.mass = mass
        self.name = name

    def __repr__(self): return f"<FFAtomType {self.atom_class}>"


# //////////////////////////////////////////////////////////////////////////////
class FFAtom:
    def __init__(self, name: str, charge: float, atom_type: FFAtomType):
        self.name = name
        self.charge = charge
        self.atom_type = atom_type

    def __repr__(self):
        return f"FFAtom(name={self.name}, charge={self.charge}, type={self.atom_type})"


# //////////////////////////////////////////////////////////////////////////////
class FFResidue:
    def __init__(self, name: str, atoms: list[FFAtom], atom_names: list[str]):
        self.name = name

        assert len(atoms) == len(atom_names)
        self._map_atom_names = {name: i for i, name in enumerate(atom_names)}
        self._atoms = atoms


    # --------------------------------------------------------------------------
    def get_by_name(self, name: str) -> FFAtom | None:
        idx = self._map_atom_names.get(name, None)
        if idx is None: return
        return self._atoms[idx]


# //////////////////////////////////////////////////////////////////////////////
