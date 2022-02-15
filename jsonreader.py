# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 18:08:29 2022

@author: dbabrams
"""

import requests
import json
import pandas as pd
from matplotlib import pyplot as plt

# Get the feed
r = requests.get('http://aqueduct.isws.illinois.edu/data/409818.json')

# load the json file
el7 = json.loads(r.text)

#extract the well name from the dictionary
wellname = el7['properties']['name']

#load the well time and head series into a Pandas data series, convert time strings to datetime
time = pd.to_datetime(pd.Series(el7['water_levels']['t_x']))
head = pd.Series(el7['water_levels']['t_y'])

# plot the data
plt.plot(time,head)
plt.title('Hydrograph: '+wellname)
plt.ylabel('Heads (ft amsl)')
plt.xticks(rotation=45)