#!/usr/bin/env python
# it has to run either sudo root on any Unix or with windows admin right. 
# author email: pythonrocks@gmail.com. 
import dpkt, pcap
import re
import sys
import numpy

def test_module(pkt):
    return .5, "test message"

def test_module2(pkt):
    return .2, "test2 message"

def __packet_processor(ts,pkt,d):
    
    #configure feature modules here
    modules = [RunHTTPReqInspect, test_module2]

    tcpPkt=dpkt.tcp.TCP(pkt)

    messages = []
    scores = []
    
    for module in modules:
        message, score = module(tcpPkt)
        messages.push(message)
        scores.push(score)

    final_message = ", ".join(messages)
    final_score = numpy.mean(scores)
    report_output(tcpPkt, final_score, final_message)

    print "src: %s, dest: %s, score: %f, message: %s", src_ip(pkt), dst_ip(pkt), final_score, final_message


pc = pcap.pcap()
pc.setfilter('tcp and dst port 80')
print 'listening on %s: %s' % (pc.name, pc.filter)
pc.loop(__packet_processor)
