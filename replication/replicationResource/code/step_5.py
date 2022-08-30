from exp.getNextGeneration import *
from exp.select import *
from exp.getDeviation import *
from exp.getMetrics import *

getMetrics(True)

# determine parents.
select_()

# In our experiments, we set 0.7, 0.1, and 0.2 as the (single-point) crossover rate, mutation rate, and copy rate, respectively.
generateNextGen(0.7, 0.1, 0.2)
