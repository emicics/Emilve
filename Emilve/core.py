import sys, builtins, inspect, re, ctypes

def CaseSensivity(codigo):
    # Contexto del script de Emiliano
    frame = inspect.currentframe().f_back
    f_locals = frame.f_locals
    f_globals = frame.f_globals

    # Limpiamos indentación para evitar IndentationError
    codigo_limpio = inspect.cleandoc(codigo)

    while True:
        try:
            exec(codigo_limpio, f_globals, f_locals)
            break 
            
        except (NameError, AttributeError) as e:
            msg = str(e)
            
            # --- CORRECCIÓN DE ATRIBUTOS ---
            if isinstance(e, AttributeError):
                match_attr = re.search(r"attribute '([^']+)'", msg)
                if match_attr:
                    attr_erroneo = match_attr.group(1)
                    
                    # Buscamos en todos los objetos locales quién tiene ese atributo (pero con otro Case)
                    encontrado = False
                    for nombre_var, obj in list(f_locals.items()):
                        # Si el objeto tiene el atributo que buscamos (en minúsculas)
                        try:
                            mapa_attrs = {a.lower(): a for a in dir(obj)}
                            if attr_erroneo.lower() in mapa_attrs:
                                nombre_real = mapa_attrs[attr_erroneo.lower()]
                                valor_real = getattr(obj, nombre_real)
                                # Inyectamos el alias directamente
                                setattr(obj, attr_erroneo, valor_real)
                                encontrado = True
                        except: continue
                    
                    if encontrado:
                        ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(frame), ctypes.c_int(1))
                        continue 

            # --- CORRECCIÓN DE VARIABLES ---
            elif isinstance(e, NameError):
                match_var = re.search(r"name '([^']+)'", msg)
                if match_var:
                    var_erronea = match_var.group(1)
                    mapa_vars = {v.lower(): v for v in f_locals.keys()}
                    for n in dir(builtins): mapa_vars[n.lower()] = n
                    
                    if var_erronea.lower() in mapa_vars:
                        nombre_real = mapa_vars[var_erronea.lower()]
                        f_locals[var_erronea] = f_locals.get(nombre_real, getattr(builtins, nombre_real, None))
                        
                        ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(frame), ctypes.c_int(1))
                        continue 

            # Si no pudimos reparar nada, soltamos el error para no ciclar
            raise e