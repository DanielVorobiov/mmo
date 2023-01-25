from scipy.optimize import linprog, linear_sum_assignment
import numpy as np

A = np.array(
    [
        [400, 200, 150, 1, 75],
        [150, 300, 150, 50, 150],
        [100, 20, 30, 300, 75],
        [20, 125, 100, 1, 170],
        [100, 250, 175, 100, 150],
    ]
)

b = np.array([1055000, 1334000, 930000, 1100000, 1235000])
c = np.array([-80, -60, -40, -10, -30])

solution = linprog(c, A_ub=A, b_ub=b, method="simplex")
print("Problema 1")
print(
    f'Solutia pentru profit maxim este:  {np.array2string(np.round(solution.x,1), separator=",")}'
    f"\nProfitul maxim este: {abs(round(solution.fun, 1))}"
)

A2 = np.array(
    [
        [5, 4, 3, 7, 11],
        [3, 3, 4, 2, 14],
        [1, 5, 1, 3, 23],
        [4, 2, 2, 5, 15],
        [2, 1, 5, 7, 2],
        [11, 8, 9, 8, 15],
    ]
)
row_ind, optimized_assignment = linear_sum_assignment(A2)

total_cost = A2[row_ind, optimized_assignment].sum()

print("Problema 2")
print("Valorile selectate sunt: ")
for i in range(0, len(optimized_assignment)):
    print(A2[i][optimized_assignment[i]])

print(f"Costul total este: {total_cost}")


