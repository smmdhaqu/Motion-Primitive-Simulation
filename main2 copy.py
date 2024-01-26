from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import pandas as pd
import numpy as np
import time

start = time.time()

def update_lines(frame, d ,ls, tx, ax):
    ls.set_segments(d[:, :(frame[0]+1), :])
    tx.set_text(frame[1])
    return ls

files = ['m20', 'm40', 'm70']

for fl in files:

    df = pd.read_csv(f'{fl}.csv', header=[2, 5], index_col=[0, 1])

    lim_ref = pd.read_csv('test_cal.csv')

    # l = df[['RigidBody:Marker1', 'RigidBody:Marker2', 'RigidBody:Marker3']]
    l = df
    segs = np.array([l[a].to_numpy() for a in l.columns.unique(0)])

    fig = plt.Figure(figsize=(12, 8))
    ax = fig.add_subplot(projection='3d')
    ax.set_xlim(lim_ref[fl][1], lim_ref[fl][0])
    ax.set_ylim(lim_ref[fl][3], lim_ref[fl][2])
    ax.set_zlim(lim_ref[fl][5], lim_ref[fl][4])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    line_segments = Line3DCollection(segs[:, :1, :], linestyles='solid', colors=colors)

    ax.add_collection3d(line_segments)
    txt = ax.text(0, 0, lim_ref[fl][5] + ((lim_ref[fl][4] - lim_ref[fl][5]) * 70 / 100), '', fontsize=15)
    ani = animation.FuncAnimation(
        fig, update_lines, l.index[l.index.levels[0] % 8 == 0], fargs=(segs, line_segments, txt, ax), interval=(1000/15), blit=True)
    # plt.show()

    ani.save(f'{fl}.mp4', fps=15, dpi=300)

    end = time.time()

    print(f'took {end - start} seconds')
