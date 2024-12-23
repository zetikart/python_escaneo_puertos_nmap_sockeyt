import nmap
import socket
import netifaces as ni

def get_interface_ip(interface='eth0'):
    try:
        ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
        return ip
    except ValueError:
        return None

def get_mac_address(interface='eth0'):
    try:
        mac = ni.ifaddresses(interface)[ni.AF_LINK][0]['addr']
        return mac
    except (ValueError, IndexError):
        return None

def get_network_range(interface='eth0'):
    try:
        ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
        netmask = ni.ifaddresses(interface)[ni.AF_INET][0]['netmask']
        network = ip.rsplit('.', 1)[0] + '.0/24'
        return network
    except ValueError:
        return None

def scan_my_ports(interface='eth0'):
    ip = get_interface_ip(interface)
    mac = get_mac_address(interface)
    if not ip:
        print("No se pudo obtener la IP de la interfaz.")
        return
    nm = nmap.PortScanner()
    nm.scan(ip, '1-1024')  # Escanea los puertos del 1 al 1024
    if ip in nm.all_hosts():
        print(f'Mi IP: {ip}')
        print(f'MAC Address: {mac}')
        print(f'Host is {nm[ip].state()} ({nm[ip].hostnames()[0]["name"]})')
        if 'tcp' in nm[ip]:
            print("Puertos abiertos:")
            for port in nm[ip]['tcp']:
                state = nm[ip]['tcp'][port]['state']
                service = nm[ip]['tcp'][port]['name']
                product = nm[ip]['tcp'][port].get('product', '')
                version = nm[ip]['tcp'][port].get('version', '')
                extrainfo = nm[ip]['tcp'][port].get('extrainfo', '')
                print(f"PORT: {port}\tSTATE: {state}\tSERVICE: {service}\tPRODUCT: {product}\tVERSION: {version}\tEXTRA INFO: {extrainfo}")
        else:
            print("No se encontraron puertos TCP abiertos.")
    else:
        print(f"No se encontraron hosts en la IP {ip}")

def scan_network_devices(interface='eth0'):
    network = get_network_range(interface)
    if not network:
        print("No se pudo obtener el rango de la red.")
        return
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-sn')  # -sn para un escaneo de ping
    print("Dispositivos conectados en la red:")
    if nm.all_hosts():
        for host in nm.all_hosts():
            print(f"Host: {host} ({nm[host].hostname()}) - {nm[host].state()}")
            if 'mac' in nm[host]['addresses']:
                print(f"MAC Address: {nm[host]['addresses']['mac']}")
    else:
        print("No se encontraron dispositivos conectados.")

def scan_ports(ip):
    nm = nmap.PortScanner()
    nm.scan(ip, '1-1024')  # Escanea los puertos del 1 al 1024
    if ip in nm.all_hosts():
        print(f"Host is {nm[ip].state()} ({nm[ip].hostnames()[0]['name']})")
        if 'mac' in nm[ip]['addresses']:
            print(f"MAC Address: {nm[ip]['addresses']['mac']}")
        if 'tcp' in nm[ip]:
            print("Puertos abiertos:")
            for port in nm[ip]['tcp']:
                state = nm[ip]['tcp'][port]['state']
                service = nm[ip]['tcp'][port]['name']
                product = nm[ip]['tcp'][port].get('product', '')
                version = nm[ip]['tcp'][port].get('version', '')
                extrainfo = nm[ip]['tcp'][port].get('extrainfo', '')
                print(f"PORT: {port}\tSTATE: {state}\tSERVICE: {service}\tPRODUCT: {product}\tVERSION: {version}\tEXTRA INFO: {extrainfo}")
        else:
            print("No se encontraron puertos TCP abiertos.")
    else:
        print(f"No se encontraron hosts en la IP {ip}")

def main_menu():
    while True:
        print("\nMenú Principal")
        print("1. Escanear mis propios puertos")
        print("2. Ver dispositivos conectados en la red")
        print("3. Escanear puertos de cierta IP")
        print("0. Salir")
        choice = input("Elige una opción: ")

        if choice == '1':
            scan_my_ports()
        elif choice == '2':
            scan_network_devices()
        elif choice == '3':
            ip = input("Ingresa la dirección IP a escanear: ")
            scan_ports(ip)
        elif choice == '0':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main_menu()
