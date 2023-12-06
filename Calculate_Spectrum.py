# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 12:58:29 2023

@author: michael
"""

import numpy as np
import hapi as hp
import matplotlib.pyplot as plt
import time

from scipy.fft import rfft, rfftfreq, irfft, fft, fftfreq, ifft
from scipy import signal

# Folder which includes the spectral data saved by the Fetch_Data.py function
hp.db_begin('QCL_Hitran_Spectral_Data')


def Hapi_Spectrum(T,P,L,OmegaRange,WavenumberStep,ConcDict):
    '''
    Using Hitran's API 'hapi,' simulate a transmission spectrum
    Given:
        T = temperature (Kelvin)
        P = atmospheric pressure (atm)
        L = path length of absorption (cm)
        OmegaRange = wavenumber range to model (cm^-1) ie. [2230:2240]
        WavenumberStep = Spectral resolution
        ConcDict = dictionary of gas concentrations in the form:
            ConcDict = {'n2o':333E-9, 'co2':450E-6}
            format of dictionary keys must be the same as the format they were 
            saved in, in the Fetch_Data.py script
    Returns:
        nu = array of wavenumbers 
        trans = array of transmission coefficients at the wavenumbers, nu
    '''
    ConcDictList = list(ConcDict.keys())

    r = hp.tableList().__repr__()
    species = np.array(r[25:-3].split("', '"))
    
    Components = []

    hitran_dict = hp.ISO_ID
    for i in range(len(hitran_dict)):
        try:        
            if hitran_dict[i+1][-1].lower() in ConcDictList:
                comp = (
                    hitran_dict[i+1][0],
                    hitran_dict[i+1][1], 
                    ConcDict[hitran_dict[i+1][-1].lower()]*hitran_dict[i+1][3]
                )
                Components.insert(-1,comp)
        except KeyError:
            continue
        
    nu,coef = hp.absorptionCoefficient_HT(
        SourceTables=species.tolist(),
        Environment={'T': T, 'p': P},
        Components=Components,
        OmegaRange=OmegaRange,
        WavenumberStep=WavenumberStep,
        HITRAN_units=False
    )
    nu,trans = hp.transmittanceSpectrum(nu,coef,Environment={'T': T, 'l': L})    

    return nu,trans


L = 1500
P = 1.0
T = 293
ConcDict = dict({})
ConcDict['n2o'] = 333E-9
ConcDict['h2o'] = 0.02
ConcDict['co2'] = 450E-6
ConcDict['co'] = 100E-9
ConcDict['ch4'] = 2E-6
OmegaRange= [2230,2240]
WavenumberStep = 0.001


nu,trans = Hapi_Spectrum(T,P,L,OmegaRange,WavenumberStep,ConcDict)



