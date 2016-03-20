#!/usr/bin/python2

import pandas as pd

import matplotlib.dates as dates
import matplotlib.pyplot as plt

tempest_df = pd.read_csv('graphs/tempest_plugins.dat', sep =' ')
tempest_df = tempest_df.set_index('time')
devstack_df = pd.read_csv('graphs/devstack_plugins.dat', sep=' ')
devstack_df = devstack_df.set_index('time')
grenade_df = pd.read_csv('graphs/grenade_plugins.dat', sep=' ')
grenade_df = grenade_df.set_index('time')


plt.figure()
plt.title('QA Project Plugin Counts')
plt.ylabel('Number of Plugins')
fig, ax = plt.subplots(1)
fig.autofmt_xdate()
xfmt = dates.DateFormatter("%b %d %Y")
ax.xaxis_date()
ax.xaxis.set_major_formatter(xfmt)

plt.plot(tempest_df.index, tempest_df['number'], label='Tempest',
         linewidth=3.0)
plt.plot(devstack_df.index, devstack_df['number'], label='Devstack',
         linewidth=3.0)
plt.plot(grenade_df.index, grenade_df['number'], label='Grenade',
        linewidth=3.0)

plt.legend()
plt.savefig('plugins.png', dpi=900)
