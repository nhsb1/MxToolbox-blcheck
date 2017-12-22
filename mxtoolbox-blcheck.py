#!/usr/bin/env python
import json
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3() #fixes for python 2.7x
import certifi
import urllib3
import datetime
from dateutil import parser

'''
MxToolbox Blacklist Checker beta
Description: Checks mxtoolbox.com's REST API for blacklist updates on a single monitored IP
URL to find your API: https://mxtoolbox.com/User/Dashboard/Monitors.aspx
Dependency: Must have registered and added the IP in question as a Monitored IP

Usage: mxtoolbox-blcheck.py 
Notes: Replace the URL string with the REST API link available at the above URL
'''

date_format = "%m/%d/%y"
now = datetime.datetime.now()
now = now.strftime(date_format)
#print type(now)

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
url = 'https://mxtoolbox.com/api/v1/monitor/?authorization=...' #Replace the URL with the link to your REST API provided here: https://mxtoolbox.com/User/Dashboard/Monitors.aspx'
r = http.request('GET', url)
d = json.loads(r.data)

for i in d:

    lastchecked =  str(i['LastChecked'])
    lastchecked = lastchecked.split("T")
    lastchecked = str(lastchecked[0])
    dt = parser.parse(lastchecked)
    now = parser.parse(now)
    
    print i['Name']
    print "----------"
    status = i['StatusSummary']
    #print dt
    # now = "2017-12-23 00:00:00" #testing date difference
    # now = parser.parse(now)
    diff = now - dt
    print "Status: " + str(status)
    print "Days since last update: " + str(diff)