import os
import sys
import subprocess

def _activar_monitor(): # Le ponemos un guion bajo para indicar que es interna
    def handle_exception(exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, ModuleNotFoundError):
            try:
                module_name = str(exc_value).split("'")[1]
            except IndexError:
                return sys.__excepthook__(exc_type, exc_value, exc_traceback)
            
            print(f"\n[Emilve] ModuleNotFoundError: '{module_name}' is not installed.")
            choice = input(f"Do you want to install it? (y/n): ").lower()
            
            if choice == 'y':
                print(f"Installing {module_name} via pip...")
                try:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
                    print(f"\n[✓] '{module_name}' installed successfully. Restarting script...\n")
                    os.execv(sys.executable, [f'"{sys.executable}"', f'"{sys.argv[0]}"'] + sys.argv[1:])
                except Exception as e:
                    print(f"[!] Error installing module: {e}")
                    sys.__excepthook__(exc_type, exc_value, exc_traceback)
            else:
                sys.__excepthook__(exc_type, exc_value, exc_traceback)
        else:
            sys.__excepthook__(exc_type, exc_value, exc_traceback)

    sys.excepthook = handle_exception

# LA MAGIA: Esto hace que se active SOLITO al importar
_activar_monitor()