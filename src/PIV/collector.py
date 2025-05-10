import requests
import pandas as pd
from bs4 import BeautifulSoup
from logger import Logger
import os


class Collector:
    def __init__(self, logger):
        self.url = 'https://finance.yahoo.com/quote/MELI/history/?period1=1186752600&period2=1746847132'
        self.logger = logger

    def collector_data(self):
        try:
            df = pd.DataFrame()
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            response = requests.get(self.url, headers=headers)
            if response.status_code != 200:
                self.logger.error("Error al consultar la url : {}".format(response.status_code))
                return df
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.select_one('div[data-testid="historical-prices"] table')
            if table is None:
                self.logger.error("Error al buscar la tabla data-testid=historical-prices")
                return df
            

            self.logger.info("Iniciando la recolección de datos".format(df.shape))
        except Exception as error:
            self.logger.error("Error al obtener los datos de la url {error}")
            return pd.DataFrame()
        
        Logger = Logger()
        coll = Collector(Logger())
        coll.collector_data()


