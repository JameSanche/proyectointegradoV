import numpy as np
import pandas as pd
import os
import sqlite3

class Enricher:
    def __init__(self, logger):
        self.logger = logger
        self.data_dir = 'src/PIV/static/data'
        os.makedirs(self.data_dir, exist_ok=True)

    def calcular_kpi(self, df=pd.DataFrame()):
        try:
            df = df.copy()
            df = df.sort_values('fecha')

            for col in df.columns:
                if col != "fecha":
                    df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '.', regex=False), errors='coerce')

            df['volatilidad'] = df['cerrar'].rolling(window=5).std().fillna(0)
            df['tasa_variacion'] = df['cerrar'].pct_change(fill_method=None).fillna(0)
            df['media_movil_7d'] = df['cerrar'].rolling(window=7).mean().bfill()
            df['retorno_acumulado'] = (1 + df['tasa_variacion']).cumprod() - 1
            df['desviacion_total'] = df['cerrar'].std()

            # Guardar CSV
            csv_path = os.path.join(self.data_dir, 'meli_data_enriquecido.csv')
            df.to_csv(csv_path, index=False)

            # Guardar SQLite
            db_path = os.path.join(self.data_dir, 'historical_meli_enriched.db')
            conn = sqlite3.connect(db_path)
            df.to_sql('meli_history_enriched', conn, if_exists='replace', index=False)
            conn.close()

            self.logger.info('Enricher', 'calcular_kpi', f'DataFrame enriquecido guardado en: {csv_path} y {db_path}')
            return df

        except Exception as errores:
            self.logger.error('Enricher', 'calcular_kpi', f'Error al enriquecer el df: {errores}')
            return pd.DataFrame()

