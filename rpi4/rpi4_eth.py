import socket

def test():
    try:
        rpi4_ip = '192.168.55.100'
        ip_port = 8888
        rpi4_eth = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rpi4_eth.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        rpi4_eth.bind((rpi4_ip, ip_port))
        rpi4_eth.listen(5)

        print('server start at: %s:%s' % (rpi4_ip, ip_port))
        print('wait for connection...')

        while True:
            conn, addr = rpi4_eth.accept()
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
    except:
        rpi4_eth.close()

def main():
    test()



if __name__ == '__main__':
    print('rpi4_eth')
    main()