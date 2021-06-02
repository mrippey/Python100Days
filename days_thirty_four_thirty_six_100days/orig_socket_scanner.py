__author__ = 'Michael Rippey'
__title__ = 'socket_scanner.py'
__date__ = '10 Aug 2020'

import socket
import sys

# Update to use argparse and prompt for URL, port range, verbose mode options

def get_open_ports(target, port_range, verbose_mode=False):
    protocol_name = 'tcp'
    open_ports = []

    server = socket.gethostbyname(target)
    print('Target: {}'.format(server))
    
    try:

        for port in range(port_range[0], port_range[1]):

            socket.setdefaulttimeout(2)
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            result = sock.connect_ex((target, port))

            if result == 0 and verbose_mode == True:
                service_name = socket.getservbyport(port, protocol_name)
                while True:
                    try:
                        print(f'Open ports for {target} ({server}) \n \
                            PORT        Service \n \
                            {port}       {service_name}')
                    
                    except socket.error:
                        print(f'Unknown/No serivce on {port}')
    

            elif result == 0 and verbose_mode == False:
                print('Port {} Open'.format(port))
                open_ports.append(port)

            sock.close()

    except socket.gaierror:
        print("Error: Invalid hostname")

        sys.exit(1)

    return(open_ports)

get_open_ports('scanme.nmap.org', [20, 81], True)
