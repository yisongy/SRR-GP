import os
from exp.dependencies import *
def protectedDiv(left, right):
    try:
        return left / right
    except ZeroDivisionError:
        return 1

def protectedNeg(self):
    if self != 0:
        return -self
    else:
        return 0

penaty_factor = [0.85, 0.9, 0.95, 1]

# The designed fitness function in this paper is sophisticated, thus it would be a little bit complicated if it appears in a simple running example.
# For a smooth understanding and an easy replication, we give a simplified version, i.e., evalSymbReg(), to complete the whole workflow. 
def evalSymbReg(individual):
    # 1. get the metric.xls of the current formula
    # take GP19 as an example 
    table = xlrd.open_workbook('../dataset/Example/flex-A03-A12/clusterAssment/metric/OTH11_gp19_metric.xls').sheets()[0]
    # 2. calculate Total_metrics of the current formula
    Total_metrics = 0
    for i in range(1, 5):
        Total_metrics += max(table.cell(i, 1).value, table.cell(i, 2).value)
    # 3. calculate PenaltyFactor of the current formula
    vote_01 = 0
    vote_10 = 0
    for i in range(1, 5):
        if table.cell(i, 1).value > table.cell(i, 2).value:
            vote_01 += 1
        elif table.cell(i, 1).value < table.cell(i, 2).value:
            vote_10 += 1
    vote_most = max(vote_01, vote_10)
    PenaltyFactor = 1 - 0.05 * (4 - vote_most)
    
    # 4. calculate fitness of current formula
    fitness = Total_metrics * PenaltyFactor

    return fitness,

# This line will generated 4 parameters using string "MAIN". You can change the number of parameters or generate parameters by other string.
pset = gp.PrimitiveSet("MAIN", 4)

# This line will add functions you would use to generate indivituals. You can add or  rmove any of them.
pset.addPrimitive(operator.add, 2)
pset.addPrimitive(operator.sub, 2)
pset.addPrimitive(operator.mul, 2)
pset.addPrimitive(protectedDiv, 2)
pset.addPrimitive(protectedNeg, 1)
pset.addPrimitive(operator.pow, 2)
pset.addPrimitive(operator.abs, 1)
pset.addEphemeralConstant("rand101", lambda: random.randint(-1, 1))
pset.renameArguments(ARG0='l1', ARG1='l2', ARG2='l3', ARG3='l4')

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

toolbox.register("evaluate", evalSymbReg)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
