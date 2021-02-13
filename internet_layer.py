import struct
import socket

def get_ipc4_packets(raw_data):
    ttl, proto, src, dest = struct.unpack("! 8x B B 2x 4s 4s", raw_data[:20])
    return (
        ttl,
        proto,
        parse_ip_addres(src),
        parse_ip_addres(dest)
    )

def parse_ip_addres(data):
    return '.'.join(map(str, data))