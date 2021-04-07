#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import statistics as stat
import math
import statistics

def efficiency_gap(data):
    
    wasteD = sum(data['d_wasted'])
    wasteR = sum(data['r_wasted'])
    
    return  (wasteD - wasteR) / len(data)


def partisan_bias(data):    
    total_votes_d = sum(data['d_votes'])
    total_votes_r = sum(data['r_votes'])
    
    shift = (total_votes_d - total_votes_r) / (2 * len(data))
    
    data['d_wasted'] = data['d_wasted'] - shift
    data['r_wasted'] = data['r_wasted'] - shift
    
    return efficiency_gap(data)

def mean_median_difference(data):

    total_votes_d = sum(data['r_votes'])  # The value will not change even if we consider d_votes
    average = total_votes_d / len(data)
    med = statistics.median(data['r_votes'])

    return (med - average) / len(data)

def fairness_metric(data) : 
  
    eg = efficiency_gap(data)
    pb = partisan_bias(data)
    mmd = mean_median_difference(data)
    value = -0.2231 * (eg * eg + pb * pb + mmd * mmd) / (0.0861 * 0.0861)
  
    return math.exp(value)

