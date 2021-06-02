__author__ = 'Michael Rippey'
__title__ = 'socket_scanner.py'
__date__ = '01 Jun 2021'

import sys 
import socket 

def scan_for_open_ports(target_host, port_range, verbose_mode=False):
    proto_name = 'tcp'
    open_ports = []

    server = socket.gethostbyname(target_host)
    print(f'Target: {server}')

 # Removed repeated conditionals to separate if statements
    try:

        for port in range(port_range[0], port_range[1]):

            socket.setdefaulttimeout(2)

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            result = sock.connect_ex((target_host, port))

            if result == 0:
                if verbose_mode == True:
                    service_name = socket.getservbyport(port, proto_name)
             
                    try:
                        print(f'Open ports for {target_host} ({server}) \n \
                    PORT        Service \n \
                    {port}       {service_name}')

                    except socket.error:
                        print(f'Unknown/No serivce on {port}')


                elif verbose_mode == False:
                    print('Port {} Open'.format(port))
                    open_ports.append(port)

            sock.close()

    except socket.gaierror:
        print("Error: Invalid hostname")

        sys.exit(1)

    return(open_ports)

scan_for_open_ports('scanme.nmap.org', [20, 81], True)
