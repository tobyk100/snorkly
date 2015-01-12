__author__ = 'Dana'

import sys
import csv
import math

import math, string, sys, fileinput

urlList = []

bad_ips = ["61.174.50.0","61.240.144.0", "61.174.51.0", "218.77.79.0", "60.173.10.0","103.41.124.0","60.173.9.0", "122.225.97.0","193.203.61.0","222.186.31.0","188.20.178.0","109.172.2.0", "87.241.172.0", "83.219.121.0", "67.174.170.0", "122.225.109.0","208.104.0.0", "67.205.96.0"	,"60.173.11.0", "125.64.35.0"]

def urldetector( url):
    for urlEntry in urlList:
        if url in urlEntry:
            return 1
    return 0

def listLoader():
    f = open('export.csv')
    csv_f = csv.reader(f)
    for row in csv_f:
       # cd = row.split(',')
        urlList.append(row[1])
        urlList.append(row[2])

    with open("blacklist.txt") as f:
        content = f.readlines()

    for x in content:
        urlList.append(x)


def entropy(string1):

    prob = [ float(string1.count(c)) / len(string1) for c in dict.fromkeys(list(string1)) ]
    entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])
    return entropy

def ipchecker(ip_s):
    for ip in bad_ips:
        if ip[0:-2] in ip_s:
            return 1
    else:
        return 0

listLoader()
