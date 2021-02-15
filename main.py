import socket

from network_layer import *
from view import View
from internet_layer import *

def main():
    interface = View()

    socket_conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))

    while True:
        hex_data, addr = socket_conn.recvfrom(65536)
        (dest_mac, src_mac, eth_proto_num, il_data) = get_ethernet_frame_payload(hex_data)

        if eth_proto_num == 8:
            (ttl, int_proto_num, src_ip_addres, dest_ip_address, tl_data) = get_ipc4_packets(il_data)
            # context = format_output((dest_mac, src_mac, prototype), (ttl, src_ip_addres, dest_ip_address))
            # interface.add_trafic_record(context)
            print(int_proto_num)
        # interface.update_view()

main()

