"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
def pregunta_01():
    import pandas as pd
    import re
    # Leer el archivo
    
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    # Omitir las primeras líneas de encabezado
    data_lines = lines[4:]
    
    clusters = []
    current_cluster = None
    
    for line in data_lines:
        line = line.strip()
        if not line:
            continue
        
        parts = re.split(r'\s{2,}', line)
        
        if len(parts) >= 3 and parts[0].isdigit():
            if current_cluster:
                clusters.append(current_cluster)
            current_cluster = {
                "cluster": int(parts[0]),
                "cantidad_de_palabras_clave": int(parts[1]),
                "porcentaje_de_palabras_clave": float(parts[2].replace(',', '.').replace('%', '').strip()),
                "principales_palabras_clave": " ".join(parts[3:])
            }
        elif current_cluster:
            current_cluster["principales_palabras_clave"] += " " + " ".join(parts)
    
    if current_cluster:
        clusters.append(current_cluster)
    
    # Limpieza de las palabras clave
    for cluster in clusters:
        cluster["principales_palabras_clave"] = re.sub(r'\s*,\s*', ', ', cluster["principales_palabras_clave"]).strip().rstrip('.')

    
    df = pd.DataFrame(clusters)
    return df

# Ejecutar la función para ver el resultado
df_resultado = pregunta_01()
df_resultado.head()

