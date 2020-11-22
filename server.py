import socket
from pprint import pprint

import PIL
import asyncio
from threading import Thread


class Server:

    def __init__(self):
        # создание сервера
        self.sock = socket.socket()
        self.sock.bind(("", 9999))
        self.conn = None
        self.addr = None

    def accept_conn(self):
        self.sock.listen(1)
        # ждем подключение
        while True:
            self.conn, self.addr = self.sock.accept()
            if self.conn:  # если подключение установлено, создаем отдельный поток для обработки
                print("connected:", self.addr)
                asyncio.run(self.create_thread())

    async def create_thread(self):
        while True:
            img = self.conn.recv(1024)
            if not img:
                break
        loop = asyncio.new_event_loop()
        th = Thread(target=run_background_loop, args=(loop,))
        th.start()
        result = asyncio.run_coroutine_threadsafe(process_image(loop, img), loop)
        pprint(result)


def run_background_loop(loop: asyncio.AbstractEventLoop) -> None:
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def process_image(loop, img):
    """
    Отправляет изображение в bytes ИИ, получает строку.
    :return str
    """
    return "закодированные карты"


if __name__ == '__main__':
    s = Server()
    while True:
        s.accept_conn()
