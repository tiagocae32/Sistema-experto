import requests

def to_int(value):
    try:
        return int(value)
    except:
        return ''

def get_interes_banco(opcion):
    tasas_interes_bancos = {
        "Banco Nacion Si " : 4.72,
        "Banco Nacion No" : 8.41,
        "Banco ICBC Si" : 9.27,
        "Banco ICBC No" : 11.02
    }

    tasa_interes = tasas_interes_bancos.get(opcion, 9.5)
    return tasa_interes
    

def verificar_situacion_crediticia(cuit: int) -> bool:
    """
    Consulta la situación crediticia de una persona mediante su CUIT.
    Retorna True si se detecta riesgo crediticio alto, False en caso contrario.
    """
    try:
        url = f"https://api.bcra.gob.ar/centraldedeudores/v1.0/Deudas/{cuit}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if not data.get("results"):
            return False  

        periodos = data["results"].get("periodos", [])
        for periodo in periodos:
            entidades = periodo.get("entidades", [])
            for entidad in entidades:
                situacion = entidad.get("situacion", 1)
                if situacion >= 3:
                    return True  

        return False  

    except requests.RequestException as e:
        print(f"Error al consultar la API del BCRA: {e}")
        return True 
