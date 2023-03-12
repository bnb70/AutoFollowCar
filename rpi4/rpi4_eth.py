import socket

def test():

    HOST = '192.168.55.100'
    PORT = 7000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)

    print('server start at: %s:%s' % (HOST, PORT))
    print('wait for connection...')

    while True:
        conn, addr = s.accept()
        print('connected by ' + str(addr))

        while True:
            indata = conn.recv(1024)
            if len(indata) == 0:  # connection closed
                conn.close()
                print('client closed connection.')
                break
            print('recv: ' + indata.decode())

            outdata = 'echo ' + indata.decode()
            conn.send(outdata.encode())
    s.close()

def main():
    test()



if __name__ == '__main__':
    print('rpi4_eth')
    main()