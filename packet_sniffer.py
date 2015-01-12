#!/usr/bin/env python
# it has to run either sudo root on any Unix or with windows admin right. 
# author email: pythonrocks@gmail.com. 
import dpkt
import re
import sys
import urlfeatures
import dpkt, os
import utilities

def test_module(pkt):
    return .5, "test message"

def test_module2(pkt):
    return .2, "test2 message"

def __packet_processor(pkt):
    
    #configure feature modules here
    modules = [urlfeatures.urldetector, urlfeatures.entropy_url, urlfeatures.ipchecker]

    if type(pkt.data.data) == dpkt.tcp.TCP:
        print pkt
        tcpPkt = dpkt.tcp.TCP(pkt)

        messages = []
        scores = []

        for module in modules:
            message, score = module(tcpPkt)
            messages.push(message)
            scores.push(score)

        final_message = ", ".join(messages)
        final_score = average(scores)
        #report_output(tcpPkt, final_score, final_message)

        print "dest: %s, score: %f, message: %s", utilities.extract_dest_ip(pkt), final_score, final_message

def average(scores):
    return sum(scores)/len(scores)

#pc = pcap.pcap()
#pc.setfilter('tcp and dst port 80')
#print 'listening on %s: %s' % (pc.name, pc.filter)
#pc.loop(__packet_processor)

def execute():
    f = open(os.path.join('sample_pcaps', '1e10f258de61535b194bcd10fab383298f83b096e51277cdc9d6529c33a7c489.cap'), 'rb')
    pcap = dpkt.pcap.Reader(f)
    eth = [dpkt.ethernet.Ethernet(buf) for ts, buf in pcap]

    for pkt in eth:
        __packet_processor(pkt)

    f.close()

execute()
