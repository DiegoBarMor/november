import november as nov

# //////////////////////////////////////////////////////////////////////////////
class FFBond:
    def __init__(self, k: float, length: float, type1: nov.FFAtomType, type2: nov.FFAtomType):
        self.k = k
        self.length = length
        self.type1 = type1
        self.type2 = type2

    def __repr__(self):
        return f"FFBond(k={self.k}, length={self.length}, type1={self.type1}, type2={self.type2})"


# //////////////////////////////////////////////////////////////////////////////
