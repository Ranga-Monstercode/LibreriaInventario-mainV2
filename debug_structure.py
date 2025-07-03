#!/usr/bin/env python3
import os
import sys

print("=== DIAGNÓSTICO DE ESTRUCTURA ===")
print(f"Directorio actual: {os.getcwd()}")
print(f"Python path: {sys.path}")
print("\n=== ARCHIVOS EN DIRECTORIO ACTUAL ===")
for item in os.listdir('.'):
    if os.path.isdir(item):
        print(f"📁 {item}/")
        if item == 'libreria':
            print("  Contenido de libreria/:")
            for subitem in os.listdir(item):
                print(f"    📄 {subitem}")
    else:
        print(f"📄 {item}")

print("\n=== INTENTANDO IMPORTAR ===")
try:
    sys.path.insert(0, '.')
    import libreria
    print("✅ libreria importado exitosamente")
    print(f"libreria.__file__ = {libreria.__file__}")
except Exception as e:
    print(f"❌ Error importando libreria: {e}")

try:
    import libreria.settings
    print("✅ libreria.settings importado exitosamente")
except Exception as e:
    print(f"❌ Error importando libreria.settings: {e}")
