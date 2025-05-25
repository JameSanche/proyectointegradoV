# 📊 MercadoLibre, Inc - Histórico de MELI

Este proyecto realiza la recolección,  enriquecimineto,  transformación y almacenamiento de datos históricos de la acción de MercadoLibre (MELI) desde Yahoo Finance. Se utiliza Web Scraping para extraer los datos y se aplican técnicas de ingeniería de características, modelado predictivo y análisis de series temporales. La solución se automatiza mediante GitHub Actions.

---

## 🚀 Funcionalidad


- Recolección automatizada de datos históricos desde Yahoo Finance.
- Enriquecimiento de datos con KPIs: volatilidad, tasa de variación, media móvil, etc.
- Modelado predictivo usando Random Forest.
- Análisis y visualización de series temporales con descomposición, ACF, PACF y ARIMA.
- Almacenamiento en CSV y base de datos SQLite.
- Automatización mediante GitHub Actions (CI/CD).
- Registra logs de ejecución en archivos con timestamp en la carpeta `logs/`.


---

## 🛠️ Estructura del Proyecto

```
📁 src
├── .github/
│   └── workflows/
│       └── update_data.yml              # Workflow de GitHub Actions
├── docs/                         # Carpeta opcional para documentación
├── logs/                         # Carpeta donde se guardan los logs generados
├── src/
│   └── PIV/
│       ├── static/
│       │   └── data/
│       │       ├── meli_data_enricher.csv         # Datos enriquecidos en formato CSV
│       │       ├── historical_meli_enricher.db    # Base de datos enriquecidos SQLite
|       |       ├── meli_data.csv                  # Datos en formato CSV
│       │       └── historical_meli.db             # Base de datos SQLite
│       ├── collector.py                           # Clase encargada del scraping y guardado
│       ├── enricher.py                            # Cálculo de KPIs
│       ├── logger.py                              # Clase Logger con configuración personalizada
│       ├── main.py                                # Script principal de ejecución
│       ├── modeller.py                            # Modelado y predicción
│       └── prueba.py                              # Script alternativo para pruebas
├── models/                                        # Carpeta para modelos (opcional)
├── setup.py                                       # Configuración para instalación como paquete
├── README.md                                      # Este archivo
├── .gitignore                                     # Archivos/Carpetas ignorados por Git
```




---

## 📄 Requisitos

- Python 3.9
- pip

---

## ⚙️ Instalación y ejecución local

### 🧱 Clonar el repositorio

```bash
git clone https://github.com/JameSanche/proyectointegradoV.git
cd \ proyectointegradoV
```

### 🐍 Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate        # En Windows: .\venv\Scripts\activate
```

### 📦 Instalar dependencias

```bash
pip install -e .
```

### ▶️ Ejecutar el script

```bash
python src/PIV/main.py
```

---

### 🔁 Automatización con GitHub Actions

Cada vez que haces un push a la rama `main`, se ejecuta automáticamente:

1. Se activa un entorno virtual.
2. Se instalan las dependencias.
3. Se ejecuta el scraping (`main.py` o `prueba.py`).
4. Los archivos generados (`.csv`, `.db`, logs) se suben automáticamente si hubo cambios.

---

### 📂 Archivos generados

- `meli_data.csv`: Datos históricos crudos desde Yahoo Finance.
- `meli_data_enriquecido.csv`: Datos enriquecidos con KPIs.
- `historical_meli.db`: Mismos datos almacenados como tabla SQLite.
- `modelo_dolar.pkl`: Modelo entrenado con Random Forest.
- `historical_meli_enriched.db`: Base de datos enriquecida.

---

### 👥 Autores

**James Sánchez**  
Correo: james.sanchez@iudigital.edu.co  

**Patricia Franco**
