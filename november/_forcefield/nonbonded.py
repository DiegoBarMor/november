import november as nov

### [AS DEFINED IN] platforms/reference/include/SimTKOpenMMRealType.h
M_PI = 3.14159265358979323846
E_CHARGE = (1.602176634e-19)
AVOGADRO = (6.0221367e23)
EPSILON0 = (1e-6*8.8541878128e-12/(E_CHARGE*E_CHARGE*AVOGADRO)) # (e^2 Na/(kJ nm)) == (e^2/(kJ mol nm))


# //////////////////////////////////////////////////////////////////////////////
class FFNonBonded:
    ONE_4PI_EPS0 = 1/(4*M_PI*EPSILON0) # 138.935456

    def __init__(self, epsilon: float, sigma: float, atom_type: nov.FFAtomType):
        self.epsilon = epsilon
        self.sigma = sigma
        self.type = atom_type

    def __repr__(self):
        return f"FFNonBonded(epsilon={self.epsilon}, sigma={self.sigma}, type={self.type})"


# //////////////////////////////////////////////////////////////////////////////
