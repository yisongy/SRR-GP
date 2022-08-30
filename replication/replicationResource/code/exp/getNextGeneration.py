from exp.dependencies import *
from exp.registration import *
import os
# crossover rate, copy rate, and mutation rate
def generateNextGen(cxpb, mutpb, copymutpb):
    pop = toolbox.population(n = 80)
    table = xlrd.open_workbook("output/SelectedFormula.xlsx").sheets()[0]
    path = "output/InitialFormula.xlsx"
    # if os.path.exists("output/NextGenerationFormula.xlsx"):
    agetable = xlrd.open_workbook(path).sheets()[0]
    formulaid = 0
    best = 0
    while formulaid < 80:
        pop[formulaid] = gp.PrimitiveTree.from_string(table.cell(formulaid, 1).value, pset)
        pop[formulaid].fitness = toolbox.evaluate(individual=pop[formulaid])
        if best < pop[formulaid].fitness[0]:
            best = pop[formulaid].fitness[0]
        formulaid += 1

    ages = []
    offspring = []
    matecombination = []
    mutatecombination = []
    copycombination = []
    for _ in range(160):
        op_choice = random.random()
        if op_choice < cxpb:
            while 1:
                ind1 = random.randint(0, 79)
                ind2 = random.randint(0, 79)
                equal = 0
                for i in range(len(matecombination)):
                    if (ind1 == matecombination[i][0] and ind2 == matecombination[i][1]) or (ind2 == matecombination[i][0] and ind1 == matecombination[i][1]):
                        equal = 1
                        break
                if equal == 0:
                    matecombination.append([ind1, ind2])
                    mate = toolbox.population(n=2)
                    mate[0] = gp.PrimitiveTree.from_string(str(pop[ind1]), pset)
                    mate[1] = gp.PrimitiveTree.from_string(str(pop[ind2]), pset)
                    mate1, mate2 = toolbox.mate(mate[0], mate[1])
                    offspring.append(mate1)
                    ages.append(1)
                    break
        elif op_choice < cxpb + mutpb:
            while 1:
                ind = random.randint(0, 79)
                equal = 0
                for i in range(min(len(matecombination),len(mutatecombination))):
                    if (ind == matecombination[i]):
                        equal = 1
                        break
                if equal == 0:
                    mutatecombination.append(ind)
                    mutate = toolbox.population(n=1)
                    mutate[0] = gp.PrimitiveTree.from_string(str(pop[ind]), pset)
                    mu, = toolbox.mutate(mutate[0])
                    offspring.append(mu)
                    ages.append(1)
                    break
        else:
            while 1:
                ind = random.randint(0, 79)
                equal = 0
                for i in range(len(copycombination)):
                    if (ind == copycombination[i]):
                        equal = 1
                        break
                if equal == 0:
                    copycombination.append(ind)
                    if pop[ind].fitness[0] == best:
                        op_choice = random.random()
                        if op_choice < copymutpb:
                            mutate = toolbox.population(n=1)
                            mutate[0] = gp.PrimitiveTree.from_string(str(pop[ind]), pset)
                            copy, = toolbox.mutate(mutate[0])
                        else:
                            copy = pop[ind]
                    else:
                        copy = pop[ind]
                    offspring.append(copy)
                    formulaid = 0
                    age = 1
                    while formulaid < 160:
                        if str(pop[ind]) == agetable.cell(formulaid, 1).value and age < int(
                                agetable.cell(formulaid, 2).value):
                            age = int(agetable.cell(formulaid, 2).value)
                        formulaid += 1
                    ages.append(age+1)
                    break
    f = xlsxwriter.Workbook("output/NextGenerationFormula.xlsx")
    sheet1 = f.add_worksheet(u'sheet1')
    i = 0
    while i < len(offspring):
        sheet1.write(i, 0, i + 1)
        sheet1.write(i, 1, str(offspring[i]))
        sheet1.write(i, 2, ages[i])
        i+=1
    f.close()
    os.remove("output/SelectedFormula.xlsx")
    return offspring,ages

