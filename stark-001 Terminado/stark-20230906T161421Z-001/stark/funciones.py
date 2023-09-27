
def normalizar_lista(lista_personaje:list) -> None:
    """
    Normaliza los valores de 'fuerza', 'altura' y 'peso' en la lista de personajes.

    Args:
        lista_personaje (list[dict]): Una lista de diccionarios respresentando personajes

    Returns:
        None

    Modifica la lista de personajes directamente, normalizando los valores de 'fuerza', 'altura' y 'peso' 
    convirtiéndolos a tipo float.

    """

    for personaje in lista_personaje:
        personaje['fuerza'] = float(personaje['fuerza'])
        personaje['altura'] = float(personaje['altura'])
        personaje['peso'] = float(personaje['peso'])
    

#-------------------------------------------------------------
def obtener_maximo(lista_personajes:list, caracteristica:str) -> int:
    """
    Obtiene el máximo valor de una característica específica en una lista de personajes.

    Args:
        lista_personajes (list[dict]): Una lista de diccionarios representando personajes, donde cada diccionario
                                 debe contener la clave especificada en 'caracteristica'.
        caracteristica (str): La clave que se utilizará para obtener el valor máximo.

    Returns:
        int: El valor máximo de la característica especificada.
    """

    bandera_primer_entrada = True
    maximo = None

    for personaje in lista_personajes:
        if bandera_primer_entrada or personaje[caracteristica] > maximo:
            maximo = personaje[caracteristica]
            bandera_primer_entrada = False

    return maximo


def obtener_minimo(lista_personajes:list, caracteristica:str) -> int:
    """
    Obtiene el minimo valor de una caracteristica espeficifica en una lista de personajes

    Args:
        lista_personajes (list[dict]): Una lista de diccionarios representando personajes, donde cada diccionario
                                 debe contener la clave especificada en 'caracteristica'.
        caracteristica (str): La clave que se utilizará para obtener el valor minimo.

    Returns:
        int: El valor minimo de la característica especificada.
    """
    bandera_primer_entrada = True
    minimo = None

    for personaje in lista_personajes:
        if bandera_primer_entrada or personaje[caracteristica] < minimo:
            minimo = personaje[caracteristica]
            bandera_primer_entrada = False

    return minimo


def obtener_personajes_caracteristica(lista_personajes:list, valor, caracteristica: str) -> list: #aplicado b y c
    """
    Obtiene una lista de personajes que tienen una característica específica y valor.

    Args:
        lista_personajes (List[dict]): Lista de personajes representados como diccionarios.
        valor : Valor que se busca en la característica.
        caracteristica (str): Característica a evaluar.

    Returns:
        List[dict]: Lista de personajes que cumplen con la condición.
    """
    lista_salida = []

    for personaje in lista_personajes:
        if valor == personaje[caracteristica]:
            lista_salida.append(personaje)

    return lista_salida

#-------------------------------------------------------------
def calcular_promedio(lista_personajes:list, tipo_promedio:str) -> float:
    """
    Calcula el promedio de una característica específica en una lista de personajes.

    Args:
        lista_personajes (list): Lista de personajes representados como diccionarios.
        tipo_promedio (str): Característica para la cual se calculará el promedio.

    Returns:
        float: Promedio de la característica especificada.
    """

    acumulador = 0
    cantidad = 0
    promedio = 0 

    for personaje in lista_personajes:
            acumulador += personaje[tipo_promedio]
            cantidad += 1

    if cantidad != 0:
        promedio = acumulador / cantidad
        
    return promedio

#-------------------------------------------------------------
def mostrar_datos_superheroes(lista_personajes:list) -> None: #A
    """
    Imprime los datos de los personajes en un formato específico.

    Args:
        lista_personajes (list): Lista de personajes representados como diccionarios.

    Returns:
        None
    """

    for personaje in lista_personajes:
        print("\n" + '#'*40)
        print(f"\n\t{personaje['nombre'].upper()}")
        for clave, valor in personaje.items():
            if clave != 'nombre':
                print(f"{clave:20} : {valor}")
    print('')

     
def mostrar_identidad_peso_superheroe_mayor_fuerza(lista_personajes:list) -> None: #B
    """
    Muestra la identidad y peso de los superhéroes con la mayor fuerza.

    Args:
        lista_personajes (list): Lista de personajes representados como diccionarios.

    Returns:
        None
    """
        
    mensaje = "heroes con mayor fuerza:"
    personajes = obtener_personajes_caracteristica(lista_personajes, obtener_maximo(lista_personajes, 'fuerza'), 'fuerza')

    for heroe in personajes:
        mensaje += f"\nidentidad: {heroe['identidad']},  peso: {heroe['peso']}kg"
    print(mensaje)


def mostrar_nombre_identidad_superheroe_mas_bajo(lista_personajes:list) -> None: #C
    """
    Muestra el nombre y la indentidad del personaje de menor altura

    Args:
        lista_personajes (list): lista de diccioanarios que representan a los personajes

    Return:
        None
    """
    mensaje = "heroes mas bajos:"
    personajes = obtener_personajes_caracteristica(lista_personajes, obtener_minimo(lista_personajes, 'altura'), 'altura')

    for heroe in personajes:
        mensaje += f"\nidentidad: {heroe['identidad']},  nombre: {heroe['nombre']}"
    print(mensaje)


def mostrar_peso_promedio_superheroes_masculinos(lista_personajes:list) -> None: #D
    """
    Muestra el Peso Promedio de los superheroes Masculinos

    Args:
        lista_personajes(list): lista de diccionarios que representan a los personajes

    Return:
        None
    """
    lista_personajes_masculinos = obtener_personajes_caracteristica(lista_personajes, 'M', 'genero')
    promedio_peso_masculino = calcular_promedio(lista_personajes_masculinos, 'peso')
    print(f"el peso promedio de los superheroes masculinos es de: {promedio_peso_masculino:.2f}KG\n")
        

def mostrar_nombres_pesos_superheroes_superen_fuerza_promedio_femenino(lista_personajes:list) -> None: #E
    """Muestra el nombre y el peso de los superheroes que superen la fuerza promedio del genero femenino
    
    Args:
        lista_personajes (list): lista de diccionario que representan a los personajes.

    Return:
        None
    """

    lista_personajes_femeninos = obtener_personajes_caracteristica(lista_personajes, 'F', 'genero')
    promedio_fuerza_femenino = calcular_promedio(lista_personajes_femeninos, "fuerza")
    mensaje_personajes = f"\nNombre y peso de los personajes que superen el promedio de fuerza femenino: (promedio = {promedio_fuerza_femenino:.2f}KG)\n"

    for personaje in lista_personajes:
        if personaje['fuerza'] > promedio_fuerza_femenino:
            mensaje_personajes += f"{personaje['nombre']:22}\t{float(personaje['peso']):.2f}KG\n"

    print(mensaje_personajes + '\n')


def mostrar_mensaje_salida() -> None:
    """
    Muestra por consola un mensaje de salida

    Args:
        None

    Return:
        None
    
    """
    print('Salir programa')


def mostrar_menu() -> None:
    """
    Muestra por consola una lista de opciones de un programa

    Args:
        None

    Return:
        None
    """
    mi_menu =\
    '''
    A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
    B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayorfuerza (MÁXIMO)
    C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)
    D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)
    E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
    género) los cuales su fuerza supere a la fuerza promedio de todas las
    superhéroes de género femenino
    '''
    print(mi_menu)


def comenzar_consulta_stark(lista_personajes:list) -> None:
    """
    Inicia una consulta de personajes Stark

    Args:
        lista_personajes (list): lista de diccionarios que representan los personajes

    Return:
        None
    """
    
    diccionario_opciones = {
                            'a':mostrar_datos_superheroes,
                            'b':mostrar_identidad_peso_superheroe_mayor_fuerza,
                            'c':mostrar_nombre_identidad_superheroe_mas_bajo,
                            'd':mostrar_peso_promedio_superheroes_masculinos,
                            'e':mostrar_nombres_pesos_superheroes_superen_fuerza_promedio_femenino,
                            'x':mostrar_mensaje_salida
                            }

    while True:
        mostrar_menu()
        opcion = input("ingrese una opcion: (X salir)").lower()

        if opcion in diccionario_opciones.keys():
            
            if opcion == 'x':
                diccionario_opciones[opcion]()
                break

            diccionario_opciones[opcion](lista_personajes)  
        else:
            print('\nopcion incorrecta. vuelve a intentarlo\n')

    