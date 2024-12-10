import numpy as np
import pandas as pd

#1
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
data2 = pd.Series(np.array([0.25, 0.5, 0.75, 1.0]), index=['a', 'b', 'c', 'd'])
print(data,'\n')
print(data2,'\n')

population_dict = {'California': 38332521.1,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
population.index.name = 'State'
population.name = 'Population in States'
print(population,'\n')

#2
print(data.isin(data2))