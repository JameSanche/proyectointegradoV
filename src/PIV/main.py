from logger import Logger
from collector import Collector
import pandas as pd

def main():
    logger = Logger()
    logger.info('Main', 'main', 'Inicializar clase Logger')

    collector = Collector(logger=logger)

    df = collector.collector_data()
    


if __name__ == "__main__":
    main()
