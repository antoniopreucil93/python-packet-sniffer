import socket

from network_layer import *
from view import View
from internet_layer import *

def main():
    interface = View()

    socket_conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))

    while True:
        hex_data, addr = socket_conn.recvfrom(65536)
        (dest_mac, src_mac, prototype, data) = get_ethernet_frame_payload(hex_data)

        if prototype == 8:
            ip_data = get_ipc4_packets(data)
            context = format_output((dest_mac, src_mac, prototype), ip_data)
            interface.add_trafic_record(context)

        interface.update()

main()