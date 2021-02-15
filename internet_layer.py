import struct
import socket

def get_ipc4_packets(raw_data):
    version_header_length = raw_data[0]
    header_length = version_header_length & 15 * 4
    ttl, proto, src, dest = struct.unpack("! 8x B B 2x 4s 4s", raw_data[:20])
    return (
        ttl,
        proto,
        format_ip_addres(src),
        format_ip_addres(dest),
        raw_data[header_length:],
    )

def get_icmp_packet(raw_data):
    icmp_type = struct.unpack('! B B H', raw_data[:4])
    return icmp_type, raw_data[4:]


def format_ip_addres(data):
    return '.'.join(map(str, data))