#!/usr/bin/python
import os, sys


def read(filename):
    return[
        stations.strip()
        for stations
        in open(filename).readlines()]

 
# Months captures
months =["enero", "febrero", "marzo"]
# Parent Directory path 
parent_dir = "~/work_lab/getdata/"

for month in months:
    os.mkdir(month)
    for  stations in read("api_get_clima/estaciones.txt"):

        # Directory 
        station_per_mounth = month +"/"+ stations

        # Path 
        dir_create = os.path.join(parent_dir, station_per_mounth)

        # Create the station_per_mounth
        os.mkdir(dir_create) 
        print("Directory '%s' created" %station_per_mounth)

