import inspect

class Braces:
    def __init__(self, codigo_raro):
        self.codigo = codigo_raro
        self._ejecutar_magia()

    def _ejecutar_magia(self):
        lineas = self.codigo.split('\n')
        codigo_nuevo = []
        nivel_indentacion = 0
        
        for linea in lineas:
            linea_limpia = linea.strip()
            if not linea_limpia: continue
                
            if '{' in linea_limpia:
                parte_fija = linea_limpia.replace('{', ':')
                codigo_nuevo.append("    " * nivel_indentacion + parte_fija)
                nivel_indentacion += 1
            elif '}' in linea_limpia:
                nivel_indentacion -= 1
            else:
                codigo_nuevo.append("    " * nivel_indentacion + linea_limpia)

        codigo_final = "\n".join(codigo_nuevo)
        
        # Inyectamos en el frame de quien llamó
        caller_frame = inspect.stack()[2].frame 
        exec(codigo_final, caller_frame.f_globals, caller_frame.f_locals)

    @staticmethod
    def easter():
        """El mensaje secreto de Emiliano para el FBI"""
        print("Espero que el FBI no me arreste por usar llaves en python. . .")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True