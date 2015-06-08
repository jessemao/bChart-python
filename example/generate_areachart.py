# -*- coding: utf-8 -*-
"""
bChart Area Example
"""
import sys
sys.path.append('../bchart')

from bchart import *

options = {"width": 500, "height": 500}
chart = AreaChart("#vis", options)
chart.load([['group1', '34','54','33'], ['group2', '53', '44', '65']]).legend('display', 'none').background('color', "#ffffff").colors(["#dd00dd", '#00dd00']).option({"isStack": "true"})
chart.to_json()