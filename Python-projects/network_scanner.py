from scapy.all import ARP, Ether, srp, IP, TCP, sr1
import socket

# Create an ARP request packet to discover devices on the local network
well_known_ports = {
    1: "TCP Port Service Multiplexer",
    2: "Management Utility",
    3: "Compression Process",
    5: "Remote Job Entry",
    7: "Echo",
    9: "Discard",
    11: "Active Users",
    13: "Daytime",
    17: "Quote of the Day",
    18: "Message Send Protocol",
    19: "Character Generator",
    20: "FTP (File Transfer Protocol) - Data",
    21: "FTP (File Transfer Protocol) - Control",
    22: "SSH (Secure Shell)",
    23: "Telnet",
    25: "SMTP (Simple Mail Transfer Protocol)",
    37: "Time",
    42: "Host Name Server",
    49: "Login Host Protocol",
    53: "DNS (Domain Name System)",
    67: "Bootstrap Protocol Server",
    68: "Bootstrap Protocol Client",
    69: "Trivial File Transfer Protocol (TFTP)",
    70: "Gopher",
    79: "Finger",
    80: "HTTP (Hypertext Transfer Protocol)",
    88: "Kerberos",
    101: "NIC Host Name Server",
    102: "ISO-TSAP (Transport Service Access Point)",
    107: "Remote Telnet Service",
    109: "Post Office Protocol - Version 2 (POP2)",
    110: "Post Office Protocol - Version 3 (POP3)",
    111: "Portmapper",
    113: "Ident",
    117: "UUCP (Unix-to-Unix Copy Protocol) Path Service",
    118: "SQL Services",
    119: "NNTP (Network News Transfer Protocol)",
    123: "NTP (Network Time Protocol)",
    135: "MS RPC (Microsoft Remote Procedure Call)",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service",
    143: "Internet Message Access Protocol (IMAP)",
    161: "Simple Network Management Protocol (SNMP)",
    162: "Simple Network Management Protocol Trap",
    179: "Border Gateway Protocol (BGP)",
    194: "Internet Relay Chat (IRC)",
    201: "AppleTalk Routing Maintenance",
    202: "AppleTalk Name Binding",
    204: "AppleTalk Echo",
    206: "AppleTalk Zone Information",
    209: "Quick Mail Transfer Protocol",
    210: "ANSI Z39.50",
    213: "Internetwork Packet Exchange (IPX)",
    220: "Internet Message Access Protocol (IMAP3)",
    245: "LINK",
    347: "NDL-AAS",
    363: "RSVP Tunnel",
    369: "Rpc2portmap",
    371: "Clearcase",
    372: "ListProcessor",
    389: "Lightweight Directory Access Protocol (LDAP)",
    427: "Service Location Protocol (SLP)",
    434: "Mobile IP Agent",
    443: "HTTPS (HTTP Secure)",
    444: "Simple Authentication and Security Layer (SASL)",
    445: "Microsoft-DS (Directory Services)",
    464: "Kerberos (Change/Set Password)",
    497: "Dantz Retrospect",
    500: "Internet Security Association and Key Management Protocol (ISAKMP)",
    512: "rexec (Remote Execution)",
    513: "rlogin (Remote Login)",
    514: "syslog",
    515: "Line Printer Daemon (LPD)",
    520: "RIP (Routing Information Protocol)",
    524: "NetWare Core Protocol (NCP)",
    530: "RPC",
    531: "AOL Instant Messenger (AIM)",
    540: "UUCP (Unix-to-Unix Copy Protocol)",
    543: "KLogin",
    544: "KShell",
    546: "DHCPv6 Client",
    547: "DHCPv6 Server",
    548: "Apple Filing Protocol (AFP)",
    554: "Real Time Streaming Protocol (RTSP)",
    556: "Remotefs",
    563: "NNTP (Network News Transfer Protocol) over TLS/SSL",
    587: "Submission (email submission)",
    610: "NQS",
    636: "Lightweight Directory Access Protocol over TLS/SSL (LDAPS)",
    639: "MSDP (Multicast Source Discovery Protocol)",
    646: "LDP (Label Distribution Protocol)",
    648: "RRP (Registry Registrar Protocol)",
    666: "Doom",
    667: "Discard",
    668: "Mecomm",
    669: "MeRegister",
    671: "VACDSM-SWS",
    683: "CORBA IIOP",
    686: "Hardware Control Protocol",
    688: "REALM-RUSD",
    690: "Velneo Application Transfer Protocol",
    694: "Linux-HA High Availability (Heartbeat)",
    695: "IEEE-MMS-SSL",
    698: "OLSR (Optimized Link State Routing Protocol)",
    699: "Access Network",
    700: "Extensible Provisioning Protocol (EPP)",
    701: "Link Management Protocol (LMP)",
    702: "IRCS (Internet Relay Chat over TLS/SSL)",
    706: "Secure Internet Live Conferencing (SILC)",
    711: "TDP (Tag Distribution Protocol)",
    712: "TLS/SSL FTP Control",
    749: "kerberos administration",
    750: "kerberos version iv",
    751: "pump",
    752: "qrh",
    754: "tell send",
    760: "kerberos password (kpasswd)",
    765: "webster",
    767: "phonebook",
    777: "Multiling HTTP",
    782: "Conserver serial-console management server",
    783: "SpamAssassin spamd",
    808: "CCProxy",
    873: "rsync",
    992: "Telnet over TLS/SSL",
    993: "IMAPS (Internet Message Access Protocol over TLS/SSL)",
    995: "POP3S (Post Office Protocol - Version 3 over TLS/SSL)"
}


def port_scan(target_host, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        packet = IP(dst=target_host)/TCP(dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=0)

        if response and response.haslayer(TCP) and response[TCP].flags & 2:
            port_description = well_known_ports.get(port, "Unknown Service")
            open_ports.append((port, port_description))

    return open_ports


def scan(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    for sent, received in result:
        print(received.psrc, received.hwsrc)
        target_host = received.psrc
        open_ports = port_scan(target_host, start_port, end_port)
        if open_ports:
            print("\tOpen ports on", target_host, ":", open_ports)
        else:
            print("\tNo open ports found on", target_host)


# Specify the IP range to scan (e.g., 192.168.0.1/24)
start_port = 1
end_port = 2
ip_range = "10.0.15.1/24"
print("IP Address\tMAC Address")
scan(ip_range)

# Display the discovered devices
