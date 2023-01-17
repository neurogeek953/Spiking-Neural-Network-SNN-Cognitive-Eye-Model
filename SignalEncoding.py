#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 15:52:59 2017

@author: TEB
"""

from WaveletWrapper import WaveWrap, pywt, np, plt

class TimeSeries:
    
    def __init__(self):
        
        self.timeSeriesSet = None
        self.maxTimeSerie = []
        self.minTimeSerie = []
        self.MaxTss = None
        self.MinTss = None
        self.scaledMaxTimeSerie = []
        self.scaledMinTimeSerie = []
        
    def create_timeSeriesSet(self, time_series_data):
        
        self.timeSeriesSet = []
        
        for i in range(0, len(time_series_data)):
        
            self.timeSeriesSet.append(time_series_data[i])
        
        return self.timeSeriesSet
    
    def find_maxTimeSerie(self, time_series_data):
        
        if self.timeSeriesSet is None:
            
            self.create_timeSeriesSet(time_series_data)
        
        for i in range(0, len(self.timeSeriesSet)):
            
            self.maxTimeSerie.append(max(self.timeSeriesSet[i]))
        
        return self.maxTimeSerie
    
    def find_minTimeSerie(self, time_series_data):
        
        if self.timeSeriesSet is None:
            
            self.create_timeSeriesSet(time_series_data)
        
        for i in range(0, len(self.timeSeriesSet)):
            
            self.minTimeSerie.append(min(self.timeSeriesSet[i]))
        
        return self.minTimeSerie
    
    def find_scalers(self, time_series_data):
        
        if len(self.minTimeSerie) == 0:
            
            self.find_minTimeSerie(time_series_data)
        
        if len(self.maxTimeSerie) == 0:
            
            self.find_maxTimeSerie(time_series_data)
        
        self.MinTss = min(self.minTimeSerie)
        self.MaxTss = max(self.maxTimeSerie) + abs(self.MinTss)
        return self.MaxTss, self.MinTss
    
    def find_scaledMinTimeSerie(self, time_series_data):
        
        if self.MaxTss == None or self.MinTss == None:
            
            self.find_scalers(time_series_data)
        
        for i in range(0, len(self.minTimeSerie)):
            
            self.scaledMinTimeSerie.append((self.minTimeSerie[i] + abs(self.MinTss))/self.MaxTss)
        
        return self.scaledMinTimeSerie
    
    def find_scaledMaxTimeSerie(self, time_series_data):
        
        if self.MaxTss == None or self.MinTss == None:
            
            self.find_scalers(time_series_data)
        
        for i in range(0, len(self.maxTimeSerie)):
            
            self.scaledMaxTimeSerie.append((self.maxTimeSerie[i] + abs(self.MinTss))/self.MaxTss)
        
        return self.scaledMaxTimeSerie
        
        


if __name__ == "__main__" :
    
    """Encoding the aero image into time series containing the strongest intensities of the image."""
    
    # load and inspect data
    data = pywt.data.aero()
    wave = WaveWrap()
    coefs = wave.twod_multilevel_wavelet_decomposition(data) 
    
    # create time series
    ts1 = TimeSeries()
    ts2 = TimeSeries()
    ts3 = TimeSeries()
    ts4 = TimeSeries()
    
    # create stimuli time series
    stim1max = ts1.find_scaledMaxTimeSerie(coefs[0]) # Max trends.
    stim2max = ts2.find_scaledMaxTimeSerie(coefs[1][0]) # Max horizontal details.
    stim3max = ts3.find_scaledMaxTimeSerie(coefs[1][1]) # Max vertical details.
    stim4max = ts4.find_scaledMaxTimeSerie(coefs[1][2]) # Max diagonal details.
    stim1min = ts1.find_scaledMinTimeSerie(coefs[0]) # Min trends.
    stim2min = ts2.find_scaledMinTimeSerie(coefs[1][0]) # Min horizontal details.
    stim3min = ts3.find_scaledMinTimeSerie(coefs[1][1]) # Min vertical details.
    stim4min = ts4.find_scaledMinTimeSerie(coefs[1][2]) # Min diagonal details.
    
    #  Plotting the stimulus 1 enveloppe.
    plt.figure()
    plt.plot(stim1max)
    plt.plot(stim1min)
    plt.show()
    
    # Plotting the stimulus 2 enveloppe.
    plt.figure()
    plt.plot(stim2max)
    plt.plot(stim2min)
    plt.show()
    
    # Plotting the stimulus 3 enveloppe.
    plt.figure()
    plt.plot(stim3max)
    plt.plot(stim3min)
    plt.show()
    
    # Plotting the stimulus 4 enveloppe.
    plt.figure()
    plt.plot(stim4max)
    plt.plot(stim4min)
    plt.show()
    
    """Encoding the camera image into time series containing the strongest intensities of the image."""
    
    # load and inspect data
    data = pywt.data.camera()
    print(np.shape(data))
    wave = WaveWrap()
    coefs = wave.twod_multilevel_wavelet_decomposition(data) 
    
    # create time series
    ts1 = TimeSeries()
    ts2 = TimeSeries()
    ts3 = TimeSeries()
    ts4 = TimeSeries()
    
    # create stimuli time series
    stim1max = ts1.find_scaledMaxTimeSerie(coefs[0]) # Max trends.
    stim2max = ts2.find_scaledMaxTimeSerie(coefs[1][0]) # Max horizontal details.
    stim3max = ts3.find_scaledMaxTimeSerie(coefs[1][1]) # Max vertical details.
    stim4max = ts4.find_scaledMaxTimeSerie(coefs[1][2]) # Max diagonal details.
    stim1min = ts1.find_scaledMinTimeSerie(coefs[0]) # Min trends.
    stim2min = ts2.find_scaledMinTimeSerie(coefs[1][0]) # Min horizontal details.
    stim3min = ts3.find_scaledMinTimeSerie(coefs[1][1]) # Min vertical details.
    stim4min = ts4.find_scaledMinTimeSerie(coefs[1][2]) # Min diagonal details.
    
    #  Plotting the stimulus 1 enveloppe.
    plt.figure()
    plt.plot(stim1max)
    plt.plot(stim1min)
    plt.show()
    
    # Plotting the stimulus 2 enveloppe.
    plt.figure()
    plt.plot(stim2max)
    plt.plot(stim2min)
    plt.show()
    
    # Plotting the stimulus 3 enveloppe.
    plt.figure()
    plt.plot(stim3max)
    plt.plot(stim3min)
    plt.show()
    
    # Plotting the stimulus 4 enveloppe.
    plt.figure()
    plt.plot(stim4max)
    plt.plot(stim4min)
    plt.show()
    
    
    