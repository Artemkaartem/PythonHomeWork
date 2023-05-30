import pandas as bd
import numpy as np
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = bd.DataFrame({'whoAmI':lst})
data.head()

data['human'] = np.where(data['whoAmI'] == 'human', '1', '0')
data['robot'] = np.where(data['whoAmI'] == 'robot', '1', '0')

print(data)