#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()

def retrieve(year):
    year=str(year)
    dat="{0}0101/{0}0201/{0}0301/{0}0401/{0}0501/{0}0601/{0}0701/{0}0801/{0}0901/{0}1001/{0}1101/{0}1201".format(year)
    server.retrieve({
        "class": "ei",
        "dataset": "interim",
        "date": dat,
        "expver": "1",
        "grid": "0.75/0.75",
        "levtype": "sfc",
        "param": "151.128/165.128/166.128",
        "stream": "moda",
        "type": "an",
        "target": "data-"+year+'.nc',
        "format": "netcdf"
    })

for year in range(1998,2018):
    retrieve(year)
    
