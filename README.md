# ci-bank-python

## Archivos y directorios principales
- `src/`
  - `__init__.py`: archivo vacío, pero necesario para que src sea un paquete (`find_packages` lo detecta).
  - `pagos.py`: archivo principal con las funciones de `verificar_saldo_en_banco` y `procesar_pago`.
- `tests/`
  - `test_pagos.py`: pruebas que simulan diferentes saldos disponibles utilizando *mock*.
- `.flake8`: archivo de configuración de *flake8* para evitar errores.
- `requirements.txt`: contiene las dependencias del proyecto.
- `setup.py`: define la configuración del paquete que se utilizará para importar funciones de `src/` (convierte el proyecto en un paquete instalable).
- `.github/workflows`
  -  `ci.yml`: flujo de trabajo para implementar el CI en GitHub Actions.

## Cómo Ejecutar el proyecto localmente
### 1) Clonar el repositorio
`git clone https://github.com/nicomellaor/ci-bank-python.git`

`cd ci-bank-python/`
### 2) Crear entorno virtual
`python3 -m venv venv`

`source venv/bin/activate` (Linux)

`source venv/Scripts/activate` (Windows)

### 3) Instalar dependencias
`pip install -r requirements.txt`

### 4) Modo desarrollo / Instalación editable
Crea un enlace simbólico para detectar paquetes en la estructura de carpetas (como `src/`)

`pip install -e .`

### 5) Ejecutar pruebas
`pytest`
