import struct
import socket
import sys
sys.path.append("./src")
from dchp_message_generator import dhcp_message

def discovery_check():
    operation_code = 1
    hardware_type = 1
    hardware_address_length = 6
    transaction_identifier = 1200
    client_IP_address = '0.0.0.0'
    your_IP_address = '0.0.0.0'
    server_IP_address = '0.0.0.0'
    gateway_IP_address = '0.0.0.0'
    client_hardware_address='fe:1d:20:1c:f6:8d'
    DHCPDISCOVER = dhcp_message(operation_code,
                                hardware_type,
                                hardware_address_length,
                                transaction_identifier,
                                client_IP_address,
                                your_IP_address,
                                server_IP_address,
                                gateway_IP_address,
                                client_hardware_address
                                )

    test_HLen = struct.unpack('B', DHCPDISCOVER[1:2])[0]
    print('Sanity Check: ', test_HLen == hardware_type == 1)