from udp import UDP
from typing import Dict, List, Optional, Union
from data_types import BaseType
from structs import car_info_struct, handshake_struct


class ACConnector:
    def __init__(self, ip: Optional[str] ="127.0.0.1") -> None:
        self.ac_telemetry_address = (ip, 9996)
        self.socket = UDP(ip, port=9997)
    
    @staticmethod
    def decode_response(response: bytearray, struct: Dict[str, BaseType]) -> Dict[str, Union[str, int, float, bool, List[Union[int, float, bool]]]]:
        return {k: v.decode(response) for k, v in struct.items()}

    def init_handshake(self) -> None:
        self.socket.send_msg(data=[1, 1, 0], receiver=self.ac_telemetry_address)
        response, _ = self.socket.receive_msg(size=408)
        response = self.decode_response(response, handshake_struct)
        return response

    def subscribe_to_update(self) -> None:
        self.socket.send_msg(data=[1, 1, 1], receiver=self.ac_telemetry_address)

    def dismiss(self) -> None:
        self.socket.send_msg(data=[1,1,3], receiver=self.ac_telemetry_address)
        self.socket.close()

    def start_communication(self) -> None:
        response = self.init_handshake()
        self.subscribe_to_update()

    def get_update(self) -> Dict[str, Union[str, int, float, bool]]:
        response = self.socket.receive_msg(size=322) # 328
        return self.decode_response(response, car_info_struct)

    
    def __enter__(self):
        self.start_communication
        return self
      
    def __exit__(self, *args, **kwargs) -> None:
        self.dismiss()
    
