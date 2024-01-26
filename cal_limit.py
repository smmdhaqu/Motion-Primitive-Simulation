import pandas as pd

data = {}

files = ['Zero_degree', 'plus20', 'plus40', 'plus70', 'minus20', 'minus40', 'minus70']
# files = ['0']

for fl in files:
    df = pd.read_csv(f'{fl}.csv', header=[2, 5], index_col=[0, 1])
    x_max = df.xs('X', level=1, axis=1).max().max()
    x_min = df.xs('X', level=1, axis=1).min().min()
    y_max = df.xs('Y', level=1, axis=1).max().max()
    y_min = df.xs('Y', level=1, axis=1).min().min()
    z_max = df.xs('Z', level=1, axis=1).max().max()
    z_min = df.xs('Z', level=1, axis=1).min().min()

    data[fl] = [x_max, x_min, y_max, y_min, z_max, z_min]

df = pd.DataFrame(data, index=['x_max', 'x_min', 'y_max', 'y_min', 'z_max', 'z_min'])
df.to_csv('test_cal.csv')



