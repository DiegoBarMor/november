import math
import numpy as np

# //////////////////////////////////////////////////////////////////////////////
class Utils:
    @staticmethod
    def vec3_dot(vec3_0, vec3_1) -> float:
        return vec3_0.x * vec3_1.x + vec3_0.y * vec3_1.y + vec3_0.z * vec3_1.z


    # --------------------------------------------------------------------------
    @staticmethod
    def vec3_norm(vec3) -> float:
        return math.sqrt(Utils.vec3_dot(vec3, vec3))


    # --------------------------------------------------------------------------
    @staticmethod
    def vec3_cross(vec3_0, vec3_1) -> np.array:
        return np.array([
            vec3_0.y * vec3_1.z - vec3_0.z * vec3_1.y,
            vec3_0.z * vec3_1.x - vec3_0.x * vec3_1.z,
            vec3_0.x * vec3_1.y - vec3_0.y * vec3_1.x
        ])


    # --------------------------------------------------------------------------
    @staticmethod
    def combinations_proper_diheds(a0, a1, a2, a3):
        combinations = [
            (a0, a1, a2, a3),
            (a3, a2, a1, a0)
        ]
        masks = [
            (True,  True,  True,  True ),
            (True,  False, False, True ),
            (False, True,  True,  False),
        ]
        for mask in masks:
            for combo in combinations:
                yield combo, mask


    # --------------------------------------------------------------------------
    @staticmethod
    def combinations_improper_diheds(a0, a1, a2, a3):
        combinations = [
            (a0, a1, a2, a3),
            (a0, a1, a3, a2),
            (a2, a1, a0, a3),
            (a3, a1, a0, a2),
            (a2, a1, a3, a0),
            (a3, a1, a2, a0),
        ]
        masks = [
            (True,  True,  True,  True ),
            (True,  False, False, True ),
            (True,  False, True, True ),
        ]
        for mask in masks:
            for combo in combinations:
                yield combo, mask


# //////////////////////////////////////////////////////////////////////////////
