from datetime import datetime
from ac_connector import ACConnector
from data_handlers import CSVHandler, ConsoleHandler, HandlerManager


def calculate_time_delta(start_time):
    if start_time:
        t = (datetime.utcnow() - start_time).microseconds
    else:
        start_time = datetime.utcnow()
        t = 0

    return t

def main():
    # csv_handler = CSVHandler("out.csv")
    console_handler = ConsoleHandler()
    handlers = [console_handler]
    
    with HandlerManager(handlers) as handler_manager:
        start_time = None
        with ACConnector(ip="127.0.0.1") as ac_connection:
            while True:
                data = ac_connection.get_update()
                data["t"] = calculate_time_delta(start_time)
                handler_manager.publish_data(data)



if __name__ == "__main__":
    main()
