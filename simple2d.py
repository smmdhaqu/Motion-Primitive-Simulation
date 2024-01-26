from matplotlib import pyplot as plt
from matplotlib import animation
import pandas as pd
import numpy as np
import time

start = time.time()

def update_lines(frame, lines, ldd):
    for i, line in enumerate(lines):
        line.set_data(ldd[i].loc[:frame, 'X'], ldd[i].loc[:frame, 'Z'])
    return lines

files = ['Zero_degree', 'plus20', 'plus40', 'plus70', 'minus20', 'minus40', 'minus70']

# files = ['0', 'p20', 'p40', 'p70', 'm20', 'm70']
# files = ['0', 'p20']
# files = ['0']

ini = pd.read_csv('Zero_degree.csv', header=[2, 5], index_col=[0, 1])

ld = []
for fl in files:
    df = pd.read_csv(f'{fl}.csv', header=[2, 5], index_col=[0, 1])
    apap = (ini.loc[0, 'RigidBody:Marker1'] - df.loc[0, 'RigidBody:Marker1']).to_numpy() + df['RigidBody:Marker1']
    ld.append(apap)

lim_ref = pd.read_csv('test_cal.csv')

min_row = np.max([m.shape[0] for m in ld])
min_row_l_i = np.argmax([m.shape[0] for m in ld])
min_row_l = ld[min_row_l_i]

fig = plt.Figure(figsize=(12, 8))
ax = fig.add_subplot()
ax.set_xlim(-2500, 6000)
ax.set_ylim(-2500, 6000)
ax.set_xlabel('x (cm)')
ax.set_ylabel('z (cm)')

lines = []
for i, ll in enumerate(ld):
    line, = ax.plot(ll.loc[0, 'X'], ll.loc[0, 'Z'], label=f'{files[i]}')
    lines.append(line)

ax.legend()
ani = animation.FuncAnimation(
    fig, update_lines, min_row_l.index[min_row_l.index.levels[0] % 8 == 0], fargs=(lines, ld), interval=(1000/15), blit=True)

# plt.show()
ani.save('all_2d_same_start.mp4', fps=15, dpi=300)

end = time.time()

print(f'took {end - start} seconds')


