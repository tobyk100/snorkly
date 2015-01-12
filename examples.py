import unittest
import dpkt, os
import utilities

f = open(os.path.join('sample_pcaps', 'http.cap'), 'rb')
pcap = dpkt.pcap.Reader(f)
eth = [dpkt.ethernet.Ethernet(buf) for ts, buf in pcap]
f.close()

http = utilities.get_http_request(eth[3])
print http.uri