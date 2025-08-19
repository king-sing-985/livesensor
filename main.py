from sensors.exception import SensorException
import os
import sys
from sensors.logger import logging

def test_exception():
    try:
        logging.info("ki yaha pe bhaiya ek error aayegi division by zero wali error")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)


if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)