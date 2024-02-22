import numpy as np
from oa.oa_2levels import construct_OA

def sphere_function(x):
    return sum(x_i ** 2 for x_i in x)

def evaluate_OED(OA, Pi, Pn, sphere_func):
    min_val = float('inf')
    max_val = float('-inf')
    min_combination = None
    max_combination = None
    history = []  # Store combination and value history

    # Loop through each row of OA
    for row in OA:
        # Initialize combination array
        combination = np.zeros_like(Pi)
        for i, value in enumerate(row):
            if value == 1:
                combination[i] = Pi[i]
            else:
                combination[i] = Pn[i]

        # Calculate the value of the combination using sphere_function
        val = sphere_func(combination)

        # Update minimum value and combination if necessary
        if val < min_val:
            min_val = val
            min_combination = combination

        # Update maximum value and combination if necessary
        if val > max_val:
            max_val = val
            max_combination = combination

        # Append combination and value to history
        history.append((combination, val))

    return min_combination, min_val, max_combination, max_val, history

# Example usage:
D = 3  # Number of factors
Pi = np.array([0, 2, 5])  # Level 1 combinations
Pn = np.array([5, 0, 1])  # Level 2 combinations

OA = construct_OA(D)
best_min_combination, min_val, best_max_combination, max_val, history = evaluate_OED(OA, Pi, Pn, sphere_function)

print("Best Minimum Combination:", best_min_combination)
print("Minimum Value:", min_val)
print("Best Maximum Combination:", best_max_combination)
print("Maximum Value:", max_val)

print("\nHistory:")
for idx, (combination, val) in enumerate(history):
    print("Combination {}: {}".format(idx + 1, combination))
    print("Value: {}".format(val))