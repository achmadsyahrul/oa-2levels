import numpy as np
from oa.oa_2levels import construct_OA

def sphere_function(x):
    return sum(x_i ** 2 for x_i in x)

def enumerate_combination(row):
    combination = np.zeros_like(Pi)
    row = row[:len(combination)]
    for i, value in enumerate(row):
        if value == 1:
            combination[i] = Pi[i]
        else:
            combination[i] = Pn[i]
    return combination


def evaluate_oed(func):
    min_val = float('inf')
    max_val = float('-inf')
    min_combination = None
    max_combination = None
    values = []
    history = []  # Store combination and value history
    # Loop through each row of OA
    for row in OA:
        # Initialize combination array
        combination = enumerate_combination(row)

        # Calculate the value of the combination
        val = func(combination)
        values.append(val)

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
    return min_val, max_val, min_combination, max_combination, history, values

def evaluate_fa(values, func):
    factor_analysis = np.zeros([2,D])
    fa_min_combination = [0] * D 
    fa_max_combination = [0] * D
    # Compute factor_analysis values
    for i in range(2):
        for j in range(D):
            # Compute factor_analysis values based on the given formulae
            if i == 0:
                factor_analysis[i][j] = (values[i] + values[j+1]) / 2
            elif i == 1 and j == 0:
                factor_analysis[i][j] = (values[2] + values[3]) / 2
            elif i == 1 and j == 1:
                factor_analysis[i][j] = (values[1] + values[3]) / 2
            elif i == 1 and j == 2:
                factor_analysis[i][j] = (values[1] + values[2]) / 2
            if factor_analysis[0][j] < factor_analysis[i][j]:
                fa_min_combination[j] = 1
                fa_max_combination[j] = 2
            else:
                fa_min_combination[j] = 2
                fa_max_combination[j] = 1
    if np.array_equal(min_combination, enumerate_combination(np.array(fa_min_combination))):
        fa_min_value = min_val
    else:
        fa_min_value = func(enumerate_combination(np.array(fa_min_combination)))
    if np.array_equal(max_combination, enumerate_combination(np.array(fa_max_combination))):
        fa_max_value = max_val
    else:
        fa_max_value = func(enumerate_combination(np.array(fa_max_combination)))
    return fa_min_value, fa_max_value, fa_min_combination, fa_max_combination

# Example usage:
D = 3  # Number of factors
Pi = np.array([0, 2, 5])  # Level 1 combinations
Pn = np.array([5, 0, 1])  # Level 2 combinations

OA = construct_OA(D)
min_val, max_val, min_combination, max_combination, history, values = evaluate_oed(sphere_function)

fa_min_value, fa_max_value, fa_min_combination, fa_max_combination = evaluate_fa(values, sphere_function)

best_min_value = np.min([min_val, fa_min_value])
best_max_value = np.max([max_val, fa_max_value])

print("OA Best Minimum Combination:", min_combination)
print("OA Minimum Value:", min_val)
print("OA Best Maximum Combination:", max_combination)
print("OA Maximum Value: {} \n".format(max_val))

print("Best Minimum Combination Use FA:", fa_min_combination)
print("Minimum Value:", fa_min_value)
print("Best Maximum Combination Use FA:", fa_max_combination)
print("Maximum Value: {} \n".format(fa_max_value))

print("Best Minimal Value", best_min_value)
print("Best Maximal Value", best_max_value)
