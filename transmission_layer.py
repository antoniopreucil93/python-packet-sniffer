import struct
import socket

def get_tcp_segment(raw_data):
    src_port, dest_port, seq, ack, offset_reserved_flags = struct.unpack('! H H L L H', raw_data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    return {
        "payload": (src_port, dest_port, seq, ack), "data": raw_data[offset:]
    }

def get_udp_datagram(raw_data):
    src_port, dest_port, size = struct.unpack('! H H 2x H', raw_data[:8])
    return { "payload": (src_port, dest_port, size), "data": raw_data[8:] }