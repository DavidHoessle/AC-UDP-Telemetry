import pandas as pd
from typing import Callable
from data_handlers.base_handler import BaseHandler


class CSVHandler(BaseHandler):
    
    def __init__(self, file: str) -> None:
        super().__init__()
        self.file = file

    def create_empty_df() -> pd.DataFrame:
        df = pd.DataFrame(data=[], columns=car_info_struct.keys())
        df.index.name = "t"
        return df

    def setup_csv(self):
        self.csv_file = open(self.file, "w")

        df = self.create_empty_df()
        df.to_csv(self.csv_file)

    def handle(self, data) -> None:
        # might need to reopen csv with mode a for pandas.to_csv later
        index = 0

        df = self.create_empty_df()
        for _ in range(10):


            data["t"] = index
            df.append(data)
            index += 1

            
        df.to_csv(self.csv_file, mode="a", header=False)
    
    def __enter__(self):
        self.setup_csv()
        return self
      
    def __exit__(self, *args, **kwargs) -> None:
        self.csv_file.close()
    