import november as nov

# //////////////////////////////////////////////////////////////////////////////
class FFAngle:
    def __init__(self, k: float, angle: float, type1: nov.FFAtomType, type2: nov.FFAtomType, type3: nov.FFAtomType):
        self.k = k
        self.angle = angle
        self.type1 = type1
        self.type2 = type2
        self.type3 = type3

    def __repr__(self):
        return f"FFAngle(k={self.k}, angle={self.angle}, type1={self.type1}, type2={self.type2}, type3={self.type3})"


# //////////////////////////////////////////////////////////////////////////////
