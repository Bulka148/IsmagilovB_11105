#Вариант 3
import socket
soct = socket.socket()
soct.bind(('localhost', 5000))
soct.listen(1) # количество людей
client, _ = soct.accept() # согласие с клиентом
print('я подключен')
bd = {}
while True:
    date, name = client.recv(1024).decode('utf-8').split(': ')

    people = ''
    if bd.get(date) is not None:
        people = ', '.join([n for n in bd[date]])

    if people:
        client.send(f'в этот день родились ещё {people}'.encode('utf-8'))
    else:
        client.send('никто другой пока ещё не родился в этот день'.encode('utf-8'))

    if bd.get(date) is None:
        bd[date] = [name]
    else:
        bd[date].append(name)

