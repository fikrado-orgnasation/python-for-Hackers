# made with python3


import nmap

scanner = nmap.portscanner

logo = """
        / \      _-'
      _/|  \-''- _ /
 __-' { |          \
     /              \
     /       "o.  |o }
     |            \ ;
                   ',
        \_         __\
          ''-_    \.//
            / '-____'
╔═══╦╗───╔╗
║╔═╗║║───║║
║║─║║║╔══╣╚═╦══╗
║╚═╝║║║╔╗║╔╗║╔╗║
║╔═╗║╚╣╚╝║║║║╔╗║
╚╝─╚╩═╣╔═╩╝╚╩╝╚╝
──────║║
──────╚╝
"""
print("______________________________")
print(logo)
print("-------------------------------")

ip_addr = input(" Please enter ip address ")
print(" The ip you enter is:", ip_addr)
type(ip_addr)

resp = input("""\nEnter the ip address you want to scan
                  1:SYN ACK scan 
                  2:UDP scan
                  3:Super scanner \n""")
print("your option", resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("ip statu: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("open ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("ip statu: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("open ports: ", scanner[ip_addr]['udp'].keys())

elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -A -O')
    print(scanner.scaninfo())
    print("ip statu: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("open ports: ", scanner[ip_addr]['tcp'].keys())

elif resp >= '4':
    print("wrong option dude")
