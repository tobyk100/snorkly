__author__ = 'Dana'

import sys
import csv
import math
import utilities
import socket

import math, string, sys, fileinput

urlList = []

bad_ips = ["61.174.50.0","61.240.144.0", "61.174.51.0", "218.77.79.0", "60.173.10.0","103.41.124.0","60.173.9.0", "122.225.97.0","193.203.61.0","222.186.31.0","188.20.178.0","109.172.2.0", "87.241.172.0", "83.219.121.0", "67.174.170.0", "122.225.109.0","208.104.0.0", "67.205.96.0"	,"60.173.11.0", "125.64.35.0"]
bad_ips1 = []

def __init__(self):
    listLoader()

def urldetector(pack):
    url = utilities.extract_url(pack)
    for urlEntry in urlList:
        if url in urlEntry:
            return (1.0, "bad url")
    return (0.0, "okay url")

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

    with open("ipblack.txt") as fip:
        content1 = fip.readlines()

    for x1 in content1:
        bad_ips1.append(x1)


def entropy_url(pack):
    string1 = utilities.extract_url(pack)
    prob = [ float(string1.count(c)) / len(string1) for c in dict.fromkeys(list(string1)) ]
    entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])
    newent =  entropy / 4.5
    return (newent, "entropy")

def ipchecker(pack):
    ip_s = utilities.get_dns_request(pack)
    

def DNSRequest(HOST):
    result = socket.getaddrinfo(HOST, 80)
    for resolvedIP in result:
        curValue, curMsg = ipAddrchecker(resolvedIP)
        if (curValue == 0):
            return curValue, curMsg
    return 0 , 'good ip'

def ipAddrchecker(IPAddress):
    
    for ip in bad_ips:
        if ip[0:-2] in IPAddress:
            return (1.0, "bad ip")

    for ip1 in bad_ips1:
        if IPAddress == ip1:
            return (1.0, "bad ip")
    return (0.0, "good ip")

