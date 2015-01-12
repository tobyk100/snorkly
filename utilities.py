import dpkt
import socket


# Returns parsed request if this is http request, otherwise None
# If this is a http response, also returns None
def get_http_request(packet):
    ip = packet.data
    tcp = ip.data

    if tcp.dport == 80 and len(tcp) > 0:
        http = dpkt.http.Request(tcp.data)
        return http


def extract_url(packet):
    http = get_http_request(packet)
    if http is not None:
        uri = http.headers['host'] + http.uri
        return uri


def extract_dest_ip(packet):
    dest = packet.data.dst
    return socket.inet_ntoa(ip.dst)

def get_dns_request(packet):
	ip = packet.data
	udp = ip.data
	if (udp.dport == 53 and len(udp) > 0):
		dns = dpkt.dns.DNS(udp.data)
		return dns