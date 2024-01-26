from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.collections import LineCollection
import pandas as pd
import numpy as np
import time

start = time.time()

# def update_lines(frame, d ,ls, tx, ax):
def update_lines(frame, d ,ls, ax):
    ls.set_segments(d[:, :(frame[0]+1), :2])
    # tx.set_text(frame[1])
    # ax.view_init(azim=frame[0] / 24)
    return ls

files = ['Zero_degree', 'plus20', 'plus40', 'plus70', 'minus20', 'minus40', 'minus70']

for fl in files:

    df = pd.read_csv(f'{fl}.csv', header=[2, 5], index_col=[0, 1])

    lim_ref = pd.read_csv('test_cal.csv')

    # l = df[['RigidBody:Marker1', 'RigidBody:Marker2', 'RigidBody:Marker3']]
    l = df
    segs = np.array([l[a].to_numpy() for a in l.columns.unique(0)])

    fig = plt.Figure(figsize=(12, 8))
    ax = fig.add_subplot()
    ax.set_xlim(lim_ref[fl][1], lim_ref[fl][0])
    ax.set_ylim(lim_ref[fl][3], lim_ref[fl][2])
    # ax.set_zlim(lim_ref[fl][5], lim_ref[fl][4])
    ax.set_xlabel('x (cm)')
    ax.set_ylabel('y (cm)')
    # ax.set_zlabel('z')

    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    line_segments = LineCollection(segs[:, :1, :2], linestyles='solid', colors=colors)

    ax.add_collection(line_segments)
    # txt = ax.text((lim_ref[fl][0] + lim_ref[fl][1]) / 2, lim_ref[fl][2], '', fontsize=15)
    ani = animation.FuncAnimation(
        # fig, update_lines, l.index[l.index.levels[0] % 8 == 0], fargs=(segs, line_segments, txt, ax), interval=(1000/15), blit=True)
        fig, update_lines, l.index[l.index.levels[0] % 8 == 0], fargs=(segs, line_segments, ax), interval=(1000/15), blit=True)
    # plt.show()

    ani.save(f'{fl}_XY_2d.mp4', fps=15, dpi=300)

    end = time.time()

    print(f'took {end - start} seconds')

