import nashpy as nash
import numpy as np

row_player = np.array([[2, 8, 3, 5], [7, 3, 9, 4], [6, 4, 3, 3], [0, 1, 5, 2]])
column_player = np.array([[2, 7, 6, 0], [8, 3, 4, 1], [3, 9, 3, 5], [5, 4, 3, 2]])
game1 = nash.Game(row_player, column_player)

equilibrias = []
equilibria = game1.support_enumeration()
for eq in equilibria:
    equilibrias.append(eq)


result = sum(
    equilibrias[0][0] * column_player[0][0] * equilibrias[2][0]
    + equilibrias[0][1] * column_player[0][1] * equilibrias[2][0]
)

print(
    f"Cea mai buna strategie pentru jocul mixt este: {sum(equilibrias[0][0] * row_player[0])} cu valoarea: {result}"
)


row_player = np.array([[10, 4, -2, 4], [7, 6, 8, 5], [2, -3, -4, 1], [4, 2, 3, 2]])
column_player = np.array([[10, 7, 2, 4], [4, 6, -3, 2], [-2, 8, -4, 3], [4, 5, 1, 2]])


maxmin = row_player.min(axis=1).max()
minmax = column_player.max(axis=1).min()
if minmax == maxmin:
    print(
        f"Cea mai optima strategie este: {np.where(column_player == maxmin)[0] + 1} cu valoarea: {maxmin}"
    )
