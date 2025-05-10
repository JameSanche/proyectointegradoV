# 📊 MercadoLibre, Inc - Histórico de MELI

Este proyecto realiza la recolección, transformación y almacenamiento de datos históricos de la acción de MercadoLibre (MELI) desde Yahoo Finance. Utiliza web scraping para obtener la información y la guarda tanto en formato CSV como en una base de datos SQLite.

---

## 🚀 Funcionalidad

- Obtiene datos históricos de MELI desde Yahoo Finance.
- Guarda los datos en:
  - Archivo CSV: `meli_data.csv`
  - Base de datos SQLite: `historical_meli.db`
- Registra logs de ejecución en archivos con timestamp en la carpeta `logs/`.


---

## 🛠️ Estructura del Proyecto

📦 src/
└── PIV/
├── static/
│ └── data/
│ ├── meli_data.csv
│ └── historical_meli.db
├── main.py # Punto de entrada principal
├── prueba.py # Script alternativo de ejecución
├── collector.py # Recolección de datos (scraping)
├── logger.py # Sistema de logging
└── models/ # (Reservado para modelos de datos si aplica)



---

## 📄 Requisitos

- Python 3.9
- pip

---

## ⚙️ Instalación y ejecución local

```bash
# Clonar el repositorio
git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate

# Instalar dependencias
pip install -e .

# Ejecutar el script
python src/PIV/main.py
🔁 Automatización con GitHub Actions
Cada vez que haces un push a la rama main, se ejecuta automáticamente:

Se activa un entorno virtual en GitHub Actions.

Se instalan las dependencias.

Se ejecuta el scraping (main.py o prueba.py).

Los archivos generados (.csv, .db, logs) se suben automáticamente al repositorio si hay cambios.

📂 Archivos generados
meli_data.csv: Datos históricos crudos desde Yahoo Finance.

historical_meli.db: Mismos datos pero almacenados como tabla SQLite.

logs/dolar_analysis_*.log: Logs detallados de cada ejecución.

👤 Autor
James Sánchez
Correo: james.sanchez@iudigital.edu.co