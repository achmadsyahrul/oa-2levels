# Import the OA construction module
from oa.oa_2levels import construct_OA

# Example: Construct OA for D-dimensional problem with D=3
D = 3
OA = construct_OA(D)
print("Orthogonal Array with Two Levels:")
print(OA)