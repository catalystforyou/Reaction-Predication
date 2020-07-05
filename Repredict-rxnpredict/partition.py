import pandas as pd

df = pd.read_csv('classified.csv')
train = df.copy()
test = df.copy()
# You can split the classified data as you wish
for i in range(3960):
    if train['additive'][i] <= 14 and train['halide'][i] <= 7 and train['base'][i] <= 1 and train['ligand'][i] <= 1:
        pass
    else:
        train.drop(index=i, inplace=True)
    if test['additive'][i] > 14 and test['halide'][i] > 7 and test['base'][i] > 1 and test['ligand'][i] > 1:
        pass
    else:
        test.drop(index=i, inplace=True)
train.to_csv('train.csv')
test.to_csv('test.csv')
