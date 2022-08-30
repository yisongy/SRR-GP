from exp.dependencies import *
from exp.registration import *
def Roulette(k):
    individuals = toolbox.population(n = 160)
    path = "output/InitialFormula.xlsx"
    table = xlrd.open_workbook(path).sheets()[0]
    formulaid = 0
    while formulaid < 160:
        individuals[formulaid] = gp.PrimitiveTree.from_string(table.cell(formulaid, 1).value, pset)
        individuals[formulaid].fitness = toolbox.evaluate(individual=individuals[formulaid])
        formulaid += 1
    s_inds = sorted(individuals, key = lambda pop: pop.fitness, reverse=True)
    sum_fits = 0
    for i in range(160):
        sum_fits += individuals[i].fitness[0]
    chosen = []
    for i in range(k):
        u = random.random() * sum_fits
        sum_ = 0
        for ind in s_inds:
            sum_ += ind.fitness[0]
            if sum_ > u:
                chosen.append(ind)
                break
    return chosen

def select_():
    path = "output/InitialFormula.xlsx"
    agetable = xlrd.open_workbook(path).sheets()[0]
    f = xlsxwriter.Workbook("output/SelectedFormula.xlsx")
    sheet1 = f.add_worksheet(u'sheet1')
    i = 0
    offspring = []
    while i < 80:
        while 1:
            nowselected = Roulette(160)
            equal = 0
            formulaid = 0
            age = 1
            while formulaid < 160:
                t = formulaid
                if str(nowselected[0]) == agetable.cell(formulaid, 1).value and age < int(agetable.cell(formulaid, 2).value):
                    age = int(agetable.cell(formulaid, 2).value)
                formulaid += 1
            if age >= 3 :
                continue
            for tree in offspring:
                if str(nowselected[0]) == str(tree):
                    equal = 1
                    break
            if equal == 0:
                offspring.append(nowselected[0])
                sheet1.write(i, 0, i + 1)
                sheet1.write(i, 1, agetable.cell(t, 1).value)
                sheet1.write(i, 2, int(agetable.cell(t, 2).value))
                break
        i += 1
    f.close()
    return offspring