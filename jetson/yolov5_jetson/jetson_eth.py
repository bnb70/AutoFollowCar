import socket

def send_data(send_data):

    rpi4_ip = '192.168.55.100'
    ip_port = 8888
    jetson_eth = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    jetson_eth.connect((rpi4_ip, ip_port))
    print('send: ' + send_data)
    jetson_eth.send(send_data.encode())

def main():
    send_data()


if __name__ == '__main__':
    print('jetson_eth')
    main()