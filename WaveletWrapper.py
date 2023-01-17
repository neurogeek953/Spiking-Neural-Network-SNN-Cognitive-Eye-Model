#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 20:04:04 2017

@author: TEB
"""

import pywt
import numpy as np
import matplotlib.pyplot as plt

class WaveWrap:
    
    """ The class WaveWrap is designed to contain functions that make wavelet transforms easy to compute as even with PyWavelets, which makes finding wavelet transforms easy it is still a tedious process.
    This is why I created a personnaly customized wrapper, which makes the task less tedious."""
    
    def __init__(self):
        
        self.complexityLevel = None
        self.waveletName = None
        self.waveletShortName = None
        self.waveletType = None
        self.waveletObj = None
    
    def infer_waveletObj(self):
        
        self.waveletObj = pywt.Wavelet(self.waveletType)
        return self.waveletObj

    def infer_waveletType(self):
        
        if self.complexityLevel is None:
            
            self.waveletType = str(self.waveletShortName)
            self.infer_waveletObj()
        
        else:
            
            self.waveletType = str(self.waveletShortName + str(self.complexityLevel))
            self.infer_waveletObj()
        
        return self.waveletType
    
    def create_wavelet(self, wavelet_name = None, wavelet_short_name = None, complexity_level = None):
        
        if wavelet_name == "Haar" or wavelet_short_name == "haar":
            
            
            self.waveletName = "Haar"
            self.waveletShortName = "haar"
            self.complexityLevel = None
            self.waveletType = self.infer_waveletType()

        
        if wavelet_name == "Daubechies" or wavelet_short_name == "db":
        
            self.waveletName = "Daubechies"
            self.waveletShortName = "db"
            self.complexityLevel = complexity_level
            self.waveletType = self.infer_waveletType()
            
            if self.waveletType not in pywt.wavelist('db'):
                
                print ("Warning: This wavelet does not exist !")
                print ("Use one of the following:", pywt.wavelist('db'))
                return None
        
        if wavelet_name == "Symlets" or wavelet_short_name == "sym":
        
            self.waveletName = "Symlets"
            self.waveletShortName = "sym"
            self.complexityLevel = complexity_level
            self.waveletType = self.infer_waveletType()
            
            if self.waveletType not in pywt.wavelist('sym'):
                
                print ("Warning: This wavelet does not exist !")
                print ("Use one of the following:", pywt.wavelist('sym'))
                return None
        
        if wavelet_name == "Coiflets" or wavelet_short_name == "coif":
        
            self.waveletName = "Coiflets"
            self.waveletShortName = "coif"
            self.complexityLevel = complexity_level
            self.waveletType = self.infer_waveletType()
            
            if self.waveletType not in pywt.wavelist('coif'):
                
                print ("Warning: This wavelet does not exist !")
                print ("Use one of the following:", pywt.wavelist('coif'))
                return None
        
        if wavelet_name == "Biorthogonal" or wavelet_short_name == "bior":
        
            self.waveletName = "Biorthogonal"
            self.waveletShortName = "bior"
            self.complexityLevel = complexity_level
            self.waveletType = self.infer_waveletType()
            
            if self.waveletType not in pywt.wavelist('bior'):
                
                print ("Warning: This wavelet does not exist !")
                print ("Use one of the following:", pywt.wavelist('bior'))
                return None
            
        if wavelet_name == "Reverse biorthogonal" or wavelet_short_name == "rbio":
        
            self.waveletName = "Biorthogonal"
            self.waveletShortName = "bior"
            self.complexityLevel = complexity_level
            self.waveletType = self.infer_waveletType()
            
            if self.waveletType not in pywt.wavelist('bior'):
                
                print ("Warning: This wavelet does not exist !")
                print ("Use one of the following:", pywt.wavelist('rbio'))
                return None
        
        if wavelet_name == "Discrete Meyer FIR" or wavelet_short_name == "dmey":
        
            self.waveletName = "Discrete Meyer FIR"
            self.waveletShortName = "dmey"
            self.complexityLevel = None
            self.waveletType = self.infer_waveletType()
            
        
        if wavelet_name == "Gaussian" or wavelet_short_name == "gaus":
        
            self.waveletName = "Gaussian"
            self.waveletShortName = "gaus"
            self.complexityLevel = complexity_level
            self.waveletType = self.infer_waveletType()
            
            if self.waveletType not in pywt.wavelist('gaus'):
                
                print ("Warning: This wavelet does not exist !")
                print ("Use one of the following:", pywt.wavelist('gaus'))
                return None
        
        if wavelet_name == "Mexican Hat" or wavelet_short_name == "mexh":
        
            self.waveletName = "Mexican Hat"
            self.waveletShortName = "mexh"
            self.complexityLevel = None
            self.waveletType = self.infer_waveletType()

        if wavelet_name == "Morlet" or wavelet_short_name == "morl":
        
            self.waveletName = "Morlet"
            self.waveletShortName = "morl"
            self.complexityLevel = None
            self.waveletType = self.infer_waveletType()

        if wavelet_name == "Complex Gaussian" or wavelet_short_name == "cgau":
        
            self.waveletName = "Complex Gaussian"
            self.waveletShortName = "cgau"
            self.complexityLevel = complexity_level
            self.waveletType = self.infer_waveletType()
            
            if self.waveletType not in pywt.wavelist('cgau'):
                
                print ("Warning: This wavelet does not exist !")
                print ("Use one of the following:", pywt.wavelist('cgau'))
                return None
        
        if wavelet_name == "Shannon" or wavelet_short_name == "shan":
        
            self.waveletName = "Shannon"
            self.waveletShortName = "shan"
            self.complexityLevel = None
            self.waveletType = self.infer_waveletType()

        if wavelet_name == "Frequency B-Spline" or wavelet_short_name == "fbsp":
        
            self.waveletName = "Frequency B-Spline"
            self.waveletShortName = "fbsp"
            self.complexityLevel = None
            self.waveletType = self.infer_waveletType()

        if wavelet_name == "Complex Morlet" or wavelet_short_name == "cmor":
        
            self.waveletName = "Complex Morlet"
            self.waveletShortName = "cmor"
            self.complexityLevel = None
            self.waveletType = self.infer_waveletType()
        
        return self.complexityLevel, self.waveletName, self.waveletShortName

    def discrete_wavelet_transform(self, data):
        
        if self.waveletName is None or self.waveletShortName is None:
            
            self.create_wavelet(wavelet_short_name = 'db', complexity_level = 38)
        
        if self.waveletType not in pywt.wavelist(family=None, kind='discrete'):
            
            print("Warning: To use the discrete wavelet transform, your wavelet must be discrete. Choose a Discrete Wavelet! :")
            print(pywt.wavelist(family=None, kind='discrete'))
            return None
         
        trend, fluctuations = pywt.dwt(data, self.waveletType)
        return trend,fluctuations
    
    def twod_discrete_wavelet_transform(self, data, concat = True):
        
        if self.waveletName is None or self.waveletShortName is None:
            
            self.create_wavelet(wavelet_short_name = 'db', complexity_level = 38)
        
        if self.waveletType not in pywt.wavelist(family=None, kind='discrete'):
            
            print("Warning: To use the discrete wavelet transform, your wavelet must be discrete. Choose a Discrete Wavelet! :")
            print(pywt.wavelist(family=None, kind='discrete'))
            return None
        
        coefficients = pywt.dwt2(data, self.waveletType)
        trend, (horizontal_detail, vertical_detail, fluctuations) = coefficients
        
        if concat == True:
            
            return coefficients
        
        if concat == False:
            
            return trend, horizontal_detail, vertical_detail, fluctuations
    
    def inverse_discrete_wavelet_transform(self, trend, fluctuations):
        
        if self.waveletType not in pywt.wavelist(family = None, kind = 'discrete'):
            
            print("Warning: To use the discrete wavelet transform, your wavelet must be discrete. Choose a Discrete Wavelet! :")
            print(pywt.wavelist(family=None, kind='discrete'))
            return None
        
        reconstructed_data = pywt.idwt( trend, fluctuations, self.waveletType, mode='symmetric', axis=-1)
        return reconstructed_data
        
        
    
    def continuous_wavelet_transform(self, data):
        
        if self.waveletName is None or self.waveletShortName is None:
            
            self.create_wavelet(wavelet_short_name = 'gaus', complexity_level = 8)
        
        if self.waveletType not in pywt.wavelist(family=None, kind='continuous'):
            
            print("Warning: To use the continuous wavelet transform, your wavelet must be discrete. Choose a Discrete Wavelet! :")
            print(pywt.wavelist(family=None, kind='discrete'))
            return None
         
        coefficients, frequencies = pywt.cwt(data, np.arange(1,len(data)),self.waveletType)
        return coefficients, frequencies
    
    def multilevel_wavelet_decomposition(self, data, level=None):
        
        if self.waveletName is None or self.waveletShortName is None:
            
            self.create_wavelet(wavelet_short_name = 'db', complexity_level = 38)
        
        if self.waveletType not in pywt.wavelist(family=None, kind='discrete'):
            
            print("Warning: To use the discrete wavelet transform, your wavelet must be discrete. Choose a Discrete Wavelet! :")
            print(pywt.wavelist(family=None, kind='discrete'))
            return None
        
        coefficients = pywt.wavedec(data, self.waveletType, level= level)
        
        if level is None:
            
            print('Warning: The default level decomposition is the maximum level :', pywt.dwt_max_level(data_len = len(data), filter_len = self.waveletObj))
        
        return coefficients

    def twod_multilevel_wavelet_decomposition(self, data, level=None, concat = True, hl_only = False):
        
        if self.waveletName is None or self.waveletShortName is None:
            
            self.create_wavelet(wavelet_short_name = 'db', complexity_level = 38)
        
        if self.waveletType not in pywt.wavelist(family=None, kind='discrete'):
            
            print("Warning: To use the discrete wavelet transform, your wavelet must be discrete. Choose a Discrete Wavelet! :")
            print(pywt.wavelist(family=None, kind='discrete'))
            return None
        
        coefficients_list = pywt.wavedec2(data, self.waveletType, level = level)
        
        if level is None:
            
            print('Warning: The default level decomposition is the maximum level :', pywt.dwt_max_level(data_len = len(data), filter_len = self.waveletObj))
        
        return coefficients_list
        
    def multilevel_wavelet_reconstruction(self, coefficients):
        
        if self.waveletType not in pywt.wavelist(family = None, kind = 'discrete'):
            
            print("Warning: To use the discrete wavelet transform, your wavelet must be discrete. Choose a Discrete Wavelet! :")
            print(pywt.wavelist(family=None, kind='discrete'))
            return None
        
        reconstructed_data = pywt.waverec(coefficients, self.waveletType, mode='symmetric', axis=-1)
        return reconstructed_data
    
    def twod_multilevel_wavelet_reconstruction(self, coefficients_list):
        
        if self.waveletType not in pywt.wavelist(family = None, kind = 'discrete'):
            
            print("Warning: To use the discrete wavelet transform, your wavelet must be discrete. Choose a Discrete Wavelet! :")
            print(pywt.wavelist(family=None, kind='discrete'))
            return None
        
        reconstructed_data = pywt.waverec2(coefficients_list, self.waveletType, mode='symmetric', axes=(-2, -1))
        return reconstructed_data

if __name__ == "__main__" :
    
    """ Analysing the effect of 2D wavelet transforms on the aero image provided by the pywavelets data. """
    # Visualize the image.
    data = pywt.data.aero()
    plt.figure()
    plt.imshow(data, cmap='gray')
    plt.show()

    # Do 2D wavelet decomposition.
    # Compute 2D wavelet transforms with the Daubechies 38 Wavelet as it is the default value I chose and maximal decomposition level.
    # The same wavelet will be used over again throughout the code.
    wave = WaveWrap()
    coefs = wave.twod_multilevel_wavelet_decomposition(data)
    
    # Trends in the image.
    plt.figure()
    plt.imshow(coefs[0],cmap='gray')
    plt.show()
    
    # Horizontal details in the image.
    plt.figure()
    plt.imshow(coefs[1][0], cmap='gray')
    plt.show()
    
    # Vertical details in the image.
    plt.figure()
    plt.imshow(coefs[1][1], cmap='gray')
    plt.show()
    
    # Diagonal details in the image.
    plt.figure()
    plt.imshow(coefs[1][2], cmap='gray')
    plt.show()
    
    # Reconstruct the data.
    rdata = wave.twod_multilevel_wavelet_reconstruction(coefs)
    plt.figure()
    plt.imshow(rdata, cmap='gray')
    plt.show()
    
    """ Analysing the effect of 2D wavelet transforms on the camera image provided by the pywavelets data. """
    # Visualize the image.
    data = pywt.data.camera()
    plt.figure()
    plt.imshow(data, cmap='gray')
    plt.show()

    # Do wavelet decomposition.
    wave = WaveWrap()
    coefs = wave.twod_multilevel_wavelet_decomposition(data)
    
    # Trends in the image.
    plt.figure()
    plt.imshow(coefs[0],cmap='gray')
    plt.show()
    
    # Horizontal details in the image.
    plt.figure()
    plt.imshow(coefs[1][0], cmap='gray')
    plt.show()
    
    # Vertical details in the image.
    plt.figure()
    plt.imshow(coefs[1][1], cmap='gray')
    plt.show()
    
    # Diagonal details in the image.
    plt.figure()
    plt.imshow(coefs[1][2], cmap='gray')
    plt.show()
    
    # Reconstruct data.
    rdata = wave.twod_multilevel_wavelet_reconstruction(coefs)
    plt.figure()
    plt.imshow(rdata, cmap='gray')
    plt.show()
    