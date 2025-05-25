import requests
import pandas as pd
from bs4 import BeautifulSoup
import sqlite3
import os

class Collector:
    def __init__(self, logger):
        self.url = 'https://finance.yahoo.com/quote/MELI/history/?period1=1186752600&period2=1746847132'
        self.logger = logger
        self.ensure_directories()

    def ensure_directories(self):
        os.makedirs('src/PIV/static/data', exist_ok=True)

    def collector_data(self):
        class_name = 'Collector'
        function_name = 'collector_data'

        try:
            df = pd.DataFrame()
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(self.url, headers=headers)

            if response.status_code != 200:
                self.logger.error(class_name, function_name, f"Error al consultar la url: {response.status_code}")
                return df

            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.select_one('div[data-testid="history-table"] table')

            if table is None:
                self.logger.error(class_name, function_name, "Error al buscar la tabla data-testid=history-table")
                return df

            header_names = [th.get_text(strip=True) for th in table.thead.find_all('th')]
            rows = []

            for tr in table.tbody.find_all('tr'):
                columns = [td.get_text(strip=True) for td in tr.find_all('td')]
                if len(columns) != len(header_names):
                    continue
                rows.append(columns)

            df = pd.DataFrame(rows, columns=header_names)

            # Renombrar columnas
            df = df.rename(columns={
                'Date': 'fecha',
                'Open': 'abrir',
                'High': 'max',
                'Low': 'min',
                'CloseClose price adjusted for splits.': 'cerrar',
                'Adj CloseAdjusted close price adjusted for splits and dividend and/or capital gain distributions.': 'cierre_ajustado',
                'Volume': 'volumen'
            })
            
            df['fecha'] = pd.to_datetime(df['fecha'], format='%b %d, %Y', errors='coerce')


            # Guardar CSV
            csv_path = 'src/PIV/static/data/meli_data.csv'
            df.to_csv(csv_path, index=False)

            # Guardar en SQLite
            db_path = 'src/PIV/static/data/historical_meli.db'
            conn = sqlite3.connect(db_path)
            df.to_sql('meli_history', conn, if_exists='replace', index=False)
            conn.close()

            self.logger.info(class_name, function_name, f"Datos guardados en: {csv_path} y {db_path}")
            return df

        except Exception as error:
            self.logger.error(class_name, function_name, f"Error al obtener los datos de la url: {error}")
            return pd.DataFrame()
