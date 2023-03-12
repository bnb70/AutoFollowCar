import socket

def test():

    HOST = '192.168.55.100'
    PORT = 7000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        outdata = input('please input message: ')
        print('send: ' + outdata)
        s.send(outdata.encode())

        indata = s.recv(1024)
        if len(indata) == 0:  # connection closed
            s.close()
            print('server closed connection.')
            break
        print('recv: ' + indata.decode())

def main():
    test()


if __name__ == '__main__':
    print('jetson_eth')
    main()