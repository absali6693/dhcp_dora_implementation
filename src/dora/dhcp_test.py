import struct
import socket
import sys
sys.path.append("./src")
from dchp_message_generator import dhcp_message

## DHCP request
def dhcp_test():
    dhcp_msg = dhcp_message(operation_code = 1,
                            hardware_type = 1,
                            hardware_address_length = 6,
                            transaction_identifier=1206,
                            client_IP_address='0.0.0.0',
                            your_IP_address='0.0.0.0',
                            server_IP_address='0.0.0.0',
                            gateway_IP_address='0.0.0.0',
                            client_hardware_address='fe:1d:20:1c:f6:8d'
                            )
    client_hardware_address='fe:1d:20:1c:f6:8d'
    print('dhcp message length: {0} bytes'.format(len(dhcp_msg)))
    _mac = []
    for i in range(-16,-10):
        _mac.append(hex(struct.unpack('B',dhcp_msg[i:i+1])[0]))
    _mac  = ':'.join(_mac).replace('0x','')
    print('HW MAC check (1): ', client_hardware_address == _mac)