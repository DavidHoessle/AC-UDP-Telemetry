from socket import socket, AF_INET, SOCK_DGRAM
from typing import List, Optional, Tuple


class UDP:
    def __init__(self, ip: Optional[str] ="127.0.0.1", port: Optional[int] =9997) -> None:
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind((ip, port))

    def send_msg(self, data: List[int], receiver: Tuple[str, int] = ("127.0.0.1", 9996)) -> None:
        bdata = bytearray(data)
        self.socket.sendto(bdata, receiver)

    def receive_msg(self, size: int = 1024) -> Tuple[bytearray, Tuple[str, int]]:
        response, addr = self.socket.recvfrom(size)
        return response, addr

    def close(self) -> None:
        self.socket.shutdown()
