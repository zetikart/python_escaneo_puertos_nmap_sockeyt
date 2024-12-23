Network Scanner Tool 🌐🔍
Descripción 📝
Esta herramienta en Python 🐍 permite escanear puertos y dispositivos en una red. Utiliza nmap 📡 para realizar los escaneos y netifaces 🔌 para obtener información de las interfaces de red. Proporciona un menú interactivo 🗂️ con varias opciones para diferentes tipos de escaneos. 🕵️‍♂️

Requisitos 📋
Python 3.6+

Librerías:

python-nmap

netifaces

Puedes instalar las dependencias necesarias usando pip:

bash
pip install python-nmap netifaces
Uso ▶️
Clona este repositorio y ejecuta el script analisis_de_red.py:

bash
git clone https://github.com/zetikart/python_escaneo_puertos_nmap_sockeyt.git
cd python_escaneo_puertos_nmap_sockeyt
python3 analisis_de_red.py
Funciones Principales 🛠️
get_interface_ip(interface='eth0')
Obtiene la dirección IP de una interfaz de red específica. 📡

get_mac_address(interface='eth0')
Obtiene la dirección MAC de una interfaz de red específica. 🔒

get_network_range(interface='eth0')
Calcula el rango de IP de la red basado en la dirección IP y la máscara de subred de una interfaz de red. 🌍

scan_my_ports(interface='eth0')
Escanea los puertos abiertos en la IP local. 🚪

Muestra la IP, dirección MAC, estado del host y detalles de los puertos abiertos (estado, servicio, producto, versión y extra información). 🛡️

scan_network_devices(interface='eth0')
Escanea la red para encontrar dispositivos conectados. 📡

Muestra los dispositivos conectados y sus direcciones MAC. 🔒

scan_ports(ip)
Escanea los puertos abiertos de una IP específica. 🚪

Muestra el estado del host, dirección MAC y detalles de los puertos abiertos. 🛡️

main_menu()
Proporciona un menú interactivo 📊 que permite al usuario elegir entre:

Escanear los propios puertos de la máquina. 🖥️

Ver los dispositivos conectados en la red. 🌍

Escanear los puertos de una IP específica. 🔍

Salir del programa. 👋

Ejemplo de Ejecución 📸
Al ejecutar el script, verás el siguiente menú interactivo:

plaintext
Menú Principal
1. Escanear mis propios puertos
2. Ver dispositivos conectados en la red
3. Escanear puertos de cierta IP
0. Salir
Elige una opción:
Selecciona una opción e ingresa los datos requeridos para realizar el escaneo correspondiente. ✅
