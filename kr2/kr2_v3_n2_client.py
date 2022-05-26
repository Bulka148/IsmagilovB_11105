import socket
soct = socket.socket()
soct.connect(('localhost', 5000))
while True:
    soct.send(input('Введите дату и имя: ').encode('utf-8'))
    code = soct.recv(1024).decode('utf-8')
    print(code)