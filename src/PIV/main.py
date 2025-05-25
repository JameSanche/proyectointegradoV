from logger import Logger
from collector import Collector
from enricher import Enricher
from modeller import Modeller
import pandas as pd

def main():
    logger = Logger()
    logger.info('Main', 'main', 'Inicializar clase Logger')

    # Recolección de datos
    collector = Collector(logger=logger)
    df = collector.collector_data()

    # Enriquecimiento de datos con KPIs
    enricher = Enricher(logger=logger)
    df_enriched = enricher.calcular_kpi(df)

    print("Primeras filas del dataframe enriquecido:")
    print(df_enriched.head())

    # Modelado y predicción
    modeller = Modeller(logger=logger)
    df_model, ok = modeller.preparar_df(df_enriched)

    if ok:
        df_model, ok = modeller.entrenar_df(df_model)
        if ok:
            _, _, valor_predicho, fecha_pred, fila = modeller.predecir_df(df_enriched)
            print(f"Prediccion para la fecha {fecha_pred}: {valor_predicho:.2f}")
        else:
            print("Fallo el entrenamiento del modelo.")
    else:
        print("Fallo la preparación del dataframe para el modelo.")

if __name__ == "__main__":
    main()
