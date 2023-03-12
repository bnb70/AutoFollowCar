import socket

def test():

    rpi4_ip = '192.168.55.100'
    ip_port = 8888

    jetson_eth = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    jetson_eth.connect((rpi4_ip, ip_port))

    while True:
        outdata = input('please input message: ')
        print('send: ' + outdata)
        jetson_eth.send(outdata.encode())

        indata = jetson_eth.recv(1024)
        if len(indata) == 0:  # connection closed
            jetson_eth.close()
            print('server closed connection.')
            break
        print('recv: ' + indata.decode())

def main():
    test()


if __name__ == '__main__':
    print('jetson_eth')
    main()