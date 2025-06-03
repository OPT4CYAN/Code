# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 13:06:16 2025

@author: gmart
"""
import datetime 
def doytodate(dayofyear):
    year            = int(dayofyear / 1000)
    day             = int(dayofyear % 1000)
    date            = datetime.datetime(year, 1, 1) + datetime.timedelta(days=int(day)-1)
    return date.strftime("%Y-%m-%d")

def datetodoy(date_str):
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    year = date.year
    day_of_year = date.timetuple().tm_yday
    return year * 1000 + day_of_year