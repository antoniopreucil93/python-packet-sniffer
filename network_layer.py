import struct
import socket

def get_ethernet_frame_payload(raw_data):
    dest_mac, src_mac, prototype = struct.unpack('6s 6s H', raw_data[:14])
    return {
        "payload":(format_mac_address(dest_mac), format_mac_address(src_mac), prototype,),
        "data": raw_data[14:]
    }

def format_mac_address(bytes_address):
    return ':'.join('{:02x}'.format(byte) for byte in bytes_address).upper()
