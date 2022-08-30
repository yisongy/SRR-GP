from exp.dependencies import *
from exp.registration import toolbox
import os
def initialGeneration():
    individuals = toolbox.population(n = 160)
    ages = np.zeros(160)
    f = xlsxwriter.Workbook("output/InitialFormula.xlsx")
    sheet1 = f.add_worksheet(u'sheet1')
    for i in range(160):
        ages[i] = 1
        sheet1.write(i, 0, i + 1)
        sheet1.write(i, 1, str(individuals[i]))
        sheet1.write(i, 2, ages[i])
    f.close()
