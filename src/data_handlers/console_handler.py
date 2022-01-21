import sys
from typing import Any, Dict
from data_handlers.base_handler import BaseHandler


class ConsoleHandler(BaseHandler):
    size = 0

    def __init__(self) -> None:
        super().__init__()

    def handle(self, data: Dict[str, Any]) -> None:
        for _ in range(self.size):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")

        t = data.pop("t")
        lines = [f"|\tt\t\t|\t{t}\t|"]
        for k, v in data.items():
            line = f"|\t{k}\t|\t{v}\t|"
            lines.append(line)
        
        self.size = len(lines) + 1
        out = "\n".join(lines)
        print(out, end="\n\n")
