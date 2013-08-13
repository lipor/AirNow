from ftplib import FTP
import os, numpy

ftp = FTP('ftp.airnowgateway.org')
uName = input('Username: ')
pWord = input('Password: ')
ftp.login(uName,pWord)

# get list of sites from local file (taken from ftp server)
sites = []
with open('sites.dat') as file:
    for line in file:
        sites.append(line.strip())

# callback function to make the list of files in HourlyData directory
# an array of strings so we can remove the Archive folder
dataFiles = []
def flistCallback(data):
    dataFiles.append(data)
 
# get list of files in HourlyData
dataFiles = []
ftp.retrlines('NLST HourlyData', flistCallback)

# remove Archive folder
dataFiles = dataFiles[:-1]
allData = numpy.zeros((len(sites),len(dataFiles)))

# go through each file in the folder and pull ozone data
# place data into an array with locations defined by sites above
# missing data points become -999

#for ind in range(len(dataFiles)):
for ind in range(1):
    fIn = 'HourlyData/' + dataFiles[ind]
    snapshot = -999*numpy.ones(len(sites))
    
    def ftpReadFile(ftpName, filename):
        def dataCallback(data):
            if data.strip():
                dataArray = data.split('|')
                if dataArray[5] == 'OZONE':
                    dataSite = dataArray[2]
                    dataInd = sites.index(dataSite)
                    snapshot[dataInd] = dataArray[7]
        ftpName.retrlines('RETR ' + filename, dataCallback)
        
    ftpReadFile(ftp, fIn)
    allData[:,ind] = snapshot
    
ftp.quit()

# write ozone data from every file to a new column in output file
fOut = open(os.getcwd() + '/NewData.dat','wb')
numpy.savetxt(fOut,allData)
fOut.close()