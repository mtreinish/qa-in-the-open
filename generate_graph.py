#!/usr/bin/env python2

import matplotlib
import matplotlib.pyplot as plt
import pandas
from pandas.tools.plotting import parallel_coordinates

Releases = ['Diablo', 'Essex', 'Folsom', 'Grizzly', 'Havana', 'Icehouse',
            'Juno', 'Kilo', 'Liberty']

tests_per_project = {

    'Diablo': {
        'glance': 44,
        'swift': 10,
        'nova': 110,
    },
    'Essex': {
        'keystone': 0,
        'horizon': 0,
        'glance': 46,
        'swift': 10,
        'nova': 151,
    },
    'Folsom': {
        'keystone': 148,
        'horizon': 0,
        'glance': 96,
        'swift': 10,
        'nova': 352,
        'cinder': 28,
        'neutron': 0,
    },
#    'Grizzly': {
#        'keystone': 0,
#        'horizon': 0,
#        'glance': 0,
#        'swift': 0,
#        'nova': 0,
#        'cinder': 0,
#        'neutron': 0,
#        'heat': 0,
#        'ceilometer': 0,
#    },
    'Havana': {
        'keystone': 216,
        'horizon': 1,
        'glance': 153,
        'swift': 51,
        'nova': 380,
        'cinder': 110,
        'neutron': 94,
        'heat': 24,
        'ceilometer': 0,
        'ironic': 0,
        'trove': 0,
        'designate': 0,
        'sahara': 0,
    },
    'Icehouse': {
        'keystone': 252,
        'horizon': 1,
        'glance': 210,
        'swift': 114,
        'nova': 1399,
        'cinder': 297,
        'neutron': 303,
        'heat': 37,
        'ceilometer': 2,
        'ironic': 60,
        'trove': 3,
        'designate': 0,
        'sahara': 6,
        'zaqar': 2,
        'barbican': 0
    },
    'Juno': {
        'keystone': 304,
        'horizon': 1,
        'glance': 216,
        'swift': 138,
        'nova': 1465,
        'cinder': 462,
        'neutron': 450,
        'heat': 60,
        'ceilometer': 14,
        'ironic': 74,
        'trove': 5,
        'designate': 0,
        'sahara': 54,
        'zaqar': 17,
        'barbican': 0
    },
    'Kilo': {
        'keystone': 153,
        'horizon': 1,
        'glance': 148,
        'swift': 136,
        'nova': 575,
        'cinder': 311,
        'neutron': 416,
        'heat': 59,
        'ceilometer': 8,
        'ironic': 71,
        'trove': 6,
        'designate': 0,
        'sahara': 40,
        'zaqar': 16,
        'barbican': 0
    },
    'Liberty': {
        'keystone': 171,
        'horizon': 1,
        'glance': 147,
        'swift': 136,
        'nova': 595,
        'cinder': 299,
        'neutron': 381,
        'heat': 46,
        'ceilometer': 11,
        'ironic': 71,
        'trove': 6,
        'designate': 0,
        'sahara': 40,
        'zaqar': 16,
        'barbican': 0
    },
}

project_names =  [
    'keystone',
    'horizon',
    'glance',
    'swift',
    'nova',
    'cinder',
    'neutron',
    'heat',
    'ceilometer',
    'ironic',
    'trove',
    'designate',
    'sahara',
    'zaqar',
    'barbican']
    
tempest_tests = [141, 192, 238, 374, 1142, 2649, 3076, 1731, 1689]
openstack_projects = [3, 5, 7, 7, 9, 10, 11, None, None]

df = pandas.DataFrame(tests_per_project)
plt.figure()

df = pandas.read_csv('i_hate_pandas.csv')

plt.ylabel('# of tests')
ax = parallel_coordinates(df, 'name')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
           ncol=3, fancybox=True, shadow=True)
plt.savefig('tests_per_proj.png', dpi=900)
