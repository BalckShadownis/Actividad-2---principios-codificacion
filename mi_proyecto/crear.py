import os
import subprocess
import sys

estructura = [
    "src",
    "src/services",
    "src/models",
    "tests"
]

archivos = [
    "src/__init__.py",
    "src/main.py",
    "tests/__init__.py",
    "tests/test_main.py",
    "requirements.txt",
    "requirements-dev.txt",
    ".gitignore",
    "README.md",
    ".env"
]

# Crear carpetas
for carpeta in estructura:
    os.makedirs(carpeta, exist_ok=True)

# Crear archivos vacíos
for archivo in archivos:
    with open(archivo, "w", encoding="utf-8") as f:
        pass

# Crear entorno virtual (venv)
venv_dir = "venv"
if not os.path.exists(venv_dir):
    print("⚙️ Creando entorno virtual...")
    subprocess.run([sys.executable, "-m", "venv", venv_dir])
else:
    print("ℹ️ El entorno virtual ya existe")

print("✅ Proyecto inicializado con estructura básica, entorno virtual y archivos de configuración")
