import os
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


class Modeller:
    def __init__(self, logger):
        self.logger = logger
        self.model_ruta = "src/PIV/static/models/"
        self.pkl_ruta = os.path.join(self.model_ruta, "modelo_dolar.pkl")

        if not os.path.exists(self.model_ruta):
            os.makedirs(self.model_ruta)

    def preparar_df(self, df=pd.DataFrame()):
        try:
            df = df.copy()
            df = df.dropna()

            df['year'] = df['fecha'].dt.year
            df['month'] = df['fecha'].dt.month
            df['day'] = df['fecha'].dt.day
            df['dayofweek'] = df['fecha'].dt.dayofweek

            # Usamos KPIs + variables temporales
            X = df[['abrir', 'max', 'min', 'volumen', 'volatilidad', 'tasa_variacion',
                    'media_movil_7d', 'retorno_acumulado', 'desviacion_total',
                    'year', 'month', 'day', 'dayofweek']]
            y = df['cerrar']

            return (X, y), True
        except Exception as e:
            self.logger.error('Modeller', 'preparar_df', f'Error: {str(e)}')
            return (pd.DataFrame(), pd.Series()), False

    def entrenar_df(self, data):
        try:
            X, y = data

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )

            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)

            with open(self.pkl_ruta, 'wb') as f:
                pickle.dump(model, f)

            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            self.logger.info('Modeller', 'entrenar_df', f"Modelo entrenado correctamente. MSE: {mse:.2f}, R2: {r2:.4f}")
            return model, True
        except Exception as e:
            self.logger.error('Modeller', 'entrenar_df', f"Error: {str(e)}")
            return None, False

    def predecir_df(self, df=pd.DataFrame()):
        try:
            if not os.path.exists(self.pkl_ruta):
                self.logger.error('Modeller', 'predecir_df', "Modelo no encontrado para predicción.")
                return df, False, None, None, None

            with open(self.pkl_ruta, 'rb') as f:
                model = pickle.load(f)

            df = df.copy()
            df = df.sort_values(by='fecha')
            ultima_fila = df.iloc[-1]

            nueva_fecha = ultima_fila['fecha'] + pd.Timedelta(days=1)
            nueva_fila = {
                'abrir': ultima_fila['abrir'],
                'max': ultima_fila['max'],
                'min': ultima_fila['min'],
                'volumen': ultima_fila['volumen'],
                'volatilidad': ultima_fila['volatilidad'],
                'tasa_variacion': ultima_fila['tasa_variacion'],
                'media_movil_7d': ultima_fila['media_movil_7d'],
                'retorno_acumulado': ultima_fila['retorno_acumulado'],
                'desviacion_total': ultima_fila['desviacion_total'],
                'year': nueva_fecha.year,
                'month': nueva_fecha.month,
                'day': nueva_fecha.day,
                'dayofweek': nueva_fecha.dayofweek
            }

            X_new = pd.DataFrame([nueva_fila])
            valor_predicho = model.predict(X_new)[0]

            self.logger.info('Modeller', 'predecir_df', f"Predicción para {nueva_fecha.date()}: {valor_predicho:.2f}")
            return df, True, valor_predicho, nueva_fecha.date(), df.shape[0] - 1
        except Exception as e:
            self.logger.error('Modeller', 'predecir_df', f"Error: {str(e)}")
            return df, False, None, None, None
