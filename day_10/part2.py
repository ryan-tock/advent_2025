import utils
import time
import pulp

data = utils.fetch_input(day=10)
# data = utils.fetch_small(day=10)
# data = utils.fetch_test(day=10)
benchmark_start = time.time()

lines = data.splitlines()


total = 0
for line in lines:
    buttons = line.split(" ")[1:-1]
    buttons = [n.split("(")[1].split(")")[0].split(",") for n in buttons]
    buttons = [[int(j) for j in n] for n in buttons]

    joltages = line.split(" ")[-1]
    joltages = joltages.split("{")[1].split("}")[0].split(",")
    joltages = [int(n) for n in joltages]

    prob = pulp.LpProblem("minimise_sum", pulp.LpMinimize)
    names = [f"x{n}" for n in range(len(buttons))]
    x = {
        v: pulp.LpVariable(names[v], lowBound=0, cat="Integer")
        for v in range(len(names))
    }
    prob += sum(x[v] for v in range(len(names))), "total_sum"

    for joltage_num in range(len(joltages)):
        relevant_buttons = [n for n in range(len(buttons)) if joltage_num in buttons[n]]
        prob += sum([x[n] for n in relevant_buttons]) == joltages[joltage_num]

    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    total += sum([int(x[v].value()) for v in range(len(names))])

print(total)
print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
