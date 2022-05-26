#Вариант 3

import random
import threading
import time

texts = ['none']

class first_thread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        while True:
            texts.append(input())

class second_thread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        troll = ['лох!!!', 'никчемный', 'очень смешно)))', 'неудачник!!!', 'удались из Интернета', 'про мать лишнее было']
        while True:
            time.sleep(random.random() * 5)
            if random.random() < 0.3:
                print(random.choice(texts) + ' - ', random.choice(troll))
            else:
                print(random.choice(troll))


first_thread().start()
second_thread().start()