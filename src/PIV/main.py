from logger import Logger
from collector import Collector
import pandas as pd
from enricher import Enricher

def main():
    logger = Logger()
    logger.info('Main', 'main', 'Inicializar clase Logger')

    collector = Collector(logger=logger)

    df = collector.collector_data()
    enricher = Enricher(logger=logger)
    df_enriched = enricher.calcular_kpi(df)

    print(df_enriched.head())
    


if __name__ == "__main__":
    main()
