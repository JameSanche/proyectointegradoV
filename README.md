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
│       │       ├── meli_data.csv         # Datos en formato CSV
│       │       └── historical_meli.db    # Base de datos SQLite
│       ├── collector.py                  # Clase encargada del scraping y guardado
│       ├── logger.py                     # Clase Logger con configuración personalizada
│       ├── main.py                       # Script principal de ejecución
│       └── prueba.py                     # Script alternativo para pruebas
├── models/                               # Carpeta para modelos (opcional)
├── setup.py                              # Configuración para instalación como paquete
├── README.md                             # Este archivo
├── .gitignore                            # Archivos/Carpetas ignorados por Git
```




---

## 📄 Requisitos

- Python 3.9
- pip

---

## ⚙️ Instalación y ejecución local

### 🧱 Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo
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
- `historical_meli.db`: Mismos datos almacenados como tabla SQLite.

---

### 👥 Autores

**James Sánchez**  
Correo: james.sanchez@iudigital.edu.co  

**Patricia Franco**
