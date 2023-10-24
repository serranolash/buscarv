import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Si deseas que la aplicación tenga una interfaz de ventana en Windows

executables = [Executable("comparar.py", base=base)]

setup(
    name="nombre_de_tu_aplicacion",
    version="0.1",
    description="Descripción de tu aplicación",
    options={"build_exe": {"packages": ["openpyxl"], "include_files": []}},
    executables=executables
)