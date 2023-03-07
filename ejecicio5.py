def es_bisiesto(anio):
    """
    Determina si un año es bisiesto o no.
    
    Args:
    anio (int): El año a evaluar.
    
    Returns:
    bool: True si el año es bisiesto, False en caso contrario.
    """
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return True
    else:
        return False
print(es_bisiesto(2023))  # False
print(es_bisiesto(2024))  # True
