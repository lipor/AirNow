The included files are intended for those using the AirNow gateway for environmental data.
http://airnowgateway.org/
To access the gateway, a username and password are required.

The file ftpFullDirectory.py scans the Hourly Data folder on the ftp data feed and places all
ozone data in a .dat file. Each row of the file contains readings for a different sensor over
time. From a research perspective, one can think of the data as a matrix, where the rows are
different sensors and the columns are snapshots.

There are numerous missing data points, because each sensor doesn't actually take a measurement
at each hourly interval. I've set it up to fill in missing points with -999.