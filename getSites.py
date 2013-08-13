# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:44:15 2013

@author: lipor
"""

from ftplib import FTP
import os

ftp = FTP('ftp.airnowgateway.org')
uName = input('Username: ')
pWord = input('Password: ')
ftp.login(uName,pWord)

# callback function to make the list of files in HourlyData directory
# an array of strings so we can remove the Archive folder
dataFiles = []
def callback(data):
    dataFiles.append(data)
    
# get full list of data sites
ftp.retrlines('RETR Locations/monitoring_site_locations.dat',callback)
dataFiles = dataFiles[::2]
sites = []
for line in dataFiles:
    siteNum = line[0:9]
    sites.append(siteNum)
len(sites)
sites = list(set(sites))        # remove duplicate sites
len(sites)

fOut = open(os.getcwd() + '/sites.dat','wb')
for item in sites:
    item = item + '\n'
    fOut.write(item.encode())
fOut.close()