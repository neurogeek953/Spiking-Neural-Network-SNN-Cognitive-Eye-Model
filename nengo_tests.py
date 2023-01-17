#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 16:07:25 2017

@author: TEB
"""

import numpy as np
import matplotlib.pyplot as plt
import nengo
from WaveletWrapper import WaveWrap, pywt, np, plt
from SignalIntegralEncoding import TimeSeries
from nengo.dists import Uniform

print('Hello World!')
data = pywt.data.camera()
print(np.shape(data))
wave = WaveWrap()
coefs = wave.twod_multilevel_wavelet_decomposition(data)
rdata = wave.twod_multilevel_wavelet_reconstruction(coefs)

ts1 = TimeSeries()
ts2 = TimeSeries()
ts3 = TimeSeries()
ts4 = TimeSeries()

# stimuli
stim1max = ts1.find_maxTimeSerie(coefs[0])
stim2max = ts2.find_maxTimeSerie(coefs[1][0])
stim3max = ts3.find_maxTimeSerie(coefs[1][1])
stim4max = ts4.find_maxTimeSerie(coefs[1][2])
stim1min = ts1.find_minTimeSerie(coefs[0])
stim2min = ts2.find_minTimeSerie(coefs[1][0])
stim3min = ts3.find_minTimeSerie(coefs[1][1])
stim4min = ts4.find_minTimeSerie(coefs[1][2])

# stim 1
plt.figure()
plt.plot(stim1max)
plt.plot(stim1min)
plt.show()

#stim 2    
plt.figure()
plt.plot(stim2max)
plt.plot(stim2min)
plt.show()

# stim 3
plt.figure()
plt.plot(stim3max)
plt.plot(stim3min)
plt.show()

# stim 4    
plt.figure()
plt.plot(stim4max)
plt.plot(stim4min)
plt.show()


