# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 09:58:45 2023

@author: michael
"""

import hapi as hp

# Create "data" folder for the spectral data 
hp.db_begin('QCL_Hitran_Spectral_Data')                 

# wavenumber region of the QCL laser
wavenumber_window = [2220,2250]

# The gloabl isotopolgues number for each species 
Species = {'h2o' : [1,2,3,4,5,6,129],
            'co2' : [7,8,9,10,11,12,13,14,121,15,120,122],
            'o3' : [16,17,18,19,20],
            'n2o' : [21,22,23,24,25],
            'co' : [26,27,28,29,30,31],
            'ch4' : [32,33,34,35],
            'o2' : [36,37,38],
            'no' : [39,40,41],
            'so2' : [42,43,137,138],
            'no2' : [44,130],
            'nh3' : [45,46],
            'hno3' : [47,117],
            'oh' : [48,49,50],
            'hf' : [51,110],
            'hcl' : [52,53,107,108],
            'hbr' : [54,55,111,112],
            'hi' : [56,113],
            'clo' : [57,58],
           'ocs' : [59,60,61,62,63,135],
           'h2co' : [64,65,66],
           'hocl' : [67,68],
           'n2' : [69,118],
           'hcn' : [70,71,72],
           'ch3cl' : [73,74],
           'h2o2' : [75],
           'c2h2' : [76,77,105],
           'c2h6' : [78,106],
           'ph3' : [79],
           'cof2' : [80,119],
           'sf6' : [126],
           'h2s' : [81,82,83],
           'hcooh' : [84],
           'ho2' : [85],
           'o' : [86],
           'clono2' : [127,128],
           'no_plus' : [87],
           'hobr' : [88,89],
           'c2h4' : [90,91],
           'ch3oh' : [92],
           'ch3br' : [93,94],
           'ch3cn' : [95],
           'cf4' : [96],
           'c4h2' : [116],
           'hc3n' : [109],
           'h2' : [103,115],
           'cs' : [97,98,99,100],
           'so3' : [114],
           'c2n2' : [123],
           'cocl2' : [124,125],
           'so' : [147,147,148],
           'ch3f' : [144],
           'geh4' : [139,140,141,142,143],
           'cs2' : [131,132,133,134],
           'ch3i' : [145],
           'nf3' : [136]
           }


# Loop through the Species and 'fetch' or download all the line parameters for all the isotopologues 
# in the region of the spectrum defined by nus (starting wavenumber) and nue (ending wavenumber)
no_lines = []
for name in Species:
    # try and except is if there ar eno absorption lines in the wavenumber region selected.
    try:
        hp.fetch_by_ids(name,Species[name],wavenumber_window[0],wavenumber_window[1])
    except:
        no_lines.append(name)
        continue
#    time.sleep(1)

print("The following species have no absorption in the range {nus} to {nue}: {no_lines}".
      format(nus=wavenumber_window[0], nue=wavenumber_window[1], no_lines=no_lines))




