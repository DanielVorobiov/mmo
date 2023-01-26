from pulp import *

print("Problema de tip inchis")
deposits = ["D1", "D2", "D3", "D4", "D5", "D6"]
availability = {"D1": 800, "D2": 400, "D3": 500, "D4": 400, "D5": 600, "D6": 700}
factories = ["F1", "F2", "F3", "F4", "F5", "F6"]
demand = {"F1": 800, "F2": 600, "F3": 700, "F4": 500, "F5": 400, "F6": 400}

costs = [
    [5, 4, 8, 3, 6, 7],
    [4, 3, 5, 4, 6, 2],
    [8, 7, 4, 3, 6, 5],
    [8, 7, 4, 6, 4, 3],
    [6, 7, 6, 5, 8, 4],
    [7, 5, 3, 6, 5, 6],
]

costs = makeDict([deposits, factories], costs, 0)
prob = LpProblem("Material Supply Problem", LpMinimize)
Routes = [(w, b) for w in deposits for b in factories]
vars = LpVariable.dicts("Route", (deposits, factories), 0, None, LpInteger)

prob += (
    lpSum([vars[w][b] * costs[w][b] for (w, b) in Routes]),
    "Sum_of_Transporting_Costs",
)

for d in deposits:
    prob += (
        lpSum([vars[d][b] for b in factories]) <= availability[d],
        "Sum_of_Products_out_of_warehouses_%s" % d,
    )

for f in factories:
    prob += (
        lpSum([vars[w][f] for w in deposits]) >= demand[f],
        "Sum_of_Products_into_projects%s" % f,
    )


prob.solve()

for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Value of Objective Function = ", value(prob.objective))

print("\n\n")
print("Problema de tip deschis")
deposits = ["D1", "D2", "D3", "D4", "D5", "D6", "D7"]
availability = {
    "D1": 600,
    "D2": 400,
    "D3": 500,
    "D4": 400,
    "D5": 600,
    "D6": 700,
    "D7": 200,
}
factories = ["F1", "F2", "F3", "F4", "F5", "F6"]
demand = {"F1": 800, "F2": 600, "F3": 700, "F4": 500, "F5": 400, "F6": 400}

costs = [
    [5, 4, 8, 3, 6, 7],
    [4, 3, 5, 4, 6, 2],
    [8, 7, 4, 3, 6, 5],
    [8, 7, 4, 6, 4, 3],
    [6, 7, 6, 5, 8, 4],
    [7, 5, 3, 6, 5, 6],
    [0, 0, 0, 0, 0, 0],
]
costs = makeDict([deposits, factories], costs, 0)
prob = LpProblem("Material Supply Problem", LpMinimize)
Routes = [(w, b) for w in deposits for b in factories]
vars = LpVariable.dicts("Route", (deposits, factories), 0, None, LpInteger)

prob += (
    lpSum([vars[w][b] * costs[w][b] for (w, b) in Routes]),
    "Sum_of_Transporting_Costs",
)

for d in deposits:
    prob += (
        lpSum([vars[d][b] for b in factories]) <= availability[d],
        "Sum_of_Products_out_of_warehouses_%s" % d,
    )

for f in factories:
    prob += (
        lpSum([vars[w][f] for w in deposits]) >= demand[f],
        "Sum_of_Products_into_projects%s" % f,
    )

prob.solve()

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("Value of Objective Function = ", value(prob.objective))
