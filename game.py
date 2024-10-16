import math

#Listas globales para los subtableros
bigA = ['','','','','','','','','']
bigB = ['','','','','','','','','']
bigC = ['','','','','','','','','']
bigD = ['','','','','','','','','']
bigE = ['','','','','','','','','']
bigF = ['','','','','','','','','']
bigG = ['','','','','','','','','']
bigH = ['','','','','','','','','']
bigI = ['','','','','','','','','']

#Con este diccionario accederemos a los subtableros
tableros = {
    'A': bigA, 'a': bigA,
    'B': bigB, 'b': bigB,
    'C': bigC, 'c': bigC,
    'D': bigD, 'd': bigD,
    'E': bigE, 'e': bigE,
    'F': bigF, 'f': bigF,
    'G': bigG, 'g': bigG,
    'H': bigH, 'h': bigH,
    'I': bigI, 'i': bigI
}

# Diccionario para convertir letras en índices
casilla = {
    'a': 0, 'b': 1, 'c': 2,
    'd': 3, 'e': 4, 'f': 5,
    'g': 6, 'h': 7, 'i': 8
}

#Función para imprimir el tablero con los subtableros
def imprimirTablero():
    print(bigA[:3],"||",bigB[:3],"||",bigC[:3])
    print(bigA[3:6],"||",bigB[3:6],"||",bigC[3:6])
    print(bigA[6:9],"||", bigB[6:9],"||", bigC[6:9])
    print("-----------------------------------------")
    print(bigD[:3],"||", bigE[:3],"||", bigF[:3])
    print(bigD[3:6],"||", bigE[3:6],"||", bigF[3:6])
    print(bigD[6:9],"||", bigE[6:9],"||", bigF[6:9])
    print("-----------------------------------------")
    print(bigG[:3],"||", bigH[:3],"||", bigI[:3])
    print(bigG[3:6],"||", bigH[3:6],"||", bigI[3:6])
    print(bigG[6:9],"||", bigH[6:9],"||", bigI[6:9])

#Función para obtener la casilla de un subtablero, recibe una letra
def obtener_casilla(letra):
    while True:
        if len(letra) != 1 or letra not in casilla:
            print("Error: Letra inválida. Introduce una letra válida de 'a' a 'i'.")
            letra = input("Ingresa una letra (a-i): ").lower()
        else:
            return casilla[letra]

#Función para determinar si "jugador" ha ganado un subtablero, recibe un subtablero y el jugador ("X" o "O")
def ha_ganado(subtablero, jugador):
    combinaciones = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontales
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticales
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    return any(all(subtablero[i] == jugador for i in combo) for combo in combinaciones)

#Función que actualiza el tablero global si un jugador ha ganado un subtablero
#Recibe el tablero global y el diccionario "tableros" para acceder a las listas (subtableros)
def actualizar_tablero_global(tablero_global, tableros):
    for i, letra in enumerate('ABCDEFGHI'):
        if ha_ganado(tableros[letra], 'X'):
            tablero_global[i] = 'X'
        elif ha_ganado(tableros[letra], 'O'):
            tablero_global[i] = 'O'
    return tablero_global

#Función para mandar la casilla seleccionada en el subtablero adecuado
def mandar_coordenadas(macro, micro, jugador, tablero_global, tableros):
    """macro: letra que hace referencia a un subtablero
    micro: letra que hace referencia a una casilla de un subtablero
    jugador: letra del jugador que mandó las coordenadas
    tablero_global: lista del tablero global si requiere ser actualizado
    tableros: diccionario que permite acceder a las listas (subtableros)"""
    aux = obtener_casilla(micro)
    subtablero = tableros.get(macro.upper())
    while subtablero[aux] != "":
        print("Casilla ocupada, elige otra.")
        micro = input(f"Coordenada en {macro}: ")
        aux = obtener_casilla(micro)
    subtablero[aux] = jugador
    
    # Actualizar el tablero global después de cada movimiento
    tablero_global = actualizar_tablero_global(tablero_global, tableros)
    
    return micro, tablero_global

#Función para determinar si nuestra lista (subtablero) está llena
def tablero_lleno(restriccion):
    if restriccion is None:
        return False
    subtablero = tableros.get(restriccion.upper())
    return all(i == "X" or i == "O" for i in subtablero)

#Función para alternar el jugador, recibe el turno
def determinar_jugador(turno):
    return "X" if turno % 2 == 0 else "O"

def verificar_victoria_global(tablero_global, jugador):
    return ha_ganado(tablero_global, jugador)

def todos_tableros_llenos(tablero_global):
    return all(casilla != "" for casilla in tablero_global)

# Funciones de Minimax y IA


def minimax_alpha_beta(tablero_global, tableros, depth, alpha, beta, maximizing_player, last_move):
    # Caso base: se alcanzó la profundidad máxima o el juego terminó
    if depth == 0 or game_over(tablero_global):
        return heuristic_evaluation(tablero_global, tableros)

    if maximizing_player:
        max_eval = -math.inf
        for move in get_valid_moves(tableros, last_move, tablero_global):
            new_tablero_global, new_tableros = make_move(tablero_global, tableros, move, 'X')
            eval = minimax_alpha_beta(new_tablero_global, new_tableros, depth - 1, alpha, beta, False, move[1])
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                return max_eval
        return max_eval
    else:
        min_eval = math.inf
        for move in get_valid_moves(tableros, last_move, tablero_global):
            new_tablero_global, new_tableros = make_move(tablero_global, tableros, move, 'O')
            eval = minimax_alpha_beta(new_tablero_global, new_tableros, depth - 1, alpha, beta, True, move[1])
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                return min_eval
        return min_eval


def get_best_move(tablero_global, tableros, last_move, depth):
    # Inicializa la mejor jugada y el mejor valor posibles
    best_move = None
    best_value = -math.inf  # Valor más bajo para comenzar (maximización)

    # Inicializa los límites para la poda alfa-beta
    alpha = -math.inf  # Valor máximo que el jugador max (X) puede garantizar
    beta = math.inf  # Valor mínimo que el jugador min (O) puede garantizar

    # Itera sobre todas las jugadas válidas disponibles según el estado actual
    for move in get_valid_moves(tableros, last_move, tablero_global):
        # Simula el tablero después de realizar la jugada actual
        new_tablero_global, new_tableros = make_move(tablero_global, tableros, move, 'X')

        # Llama al algoritmo Minimax con poda alfa-beta para evaluar la jugada
        move_value = minimax_alpha_beta(
            new_tablero_global, new_tableros, depth - 1, alpha, beta, False, move[1]
        )

        # Si la evaluación de esta jugada es mejor que la anterior, actualiza el mejor valor y jugada
        if move_value > best_value:
            best_value = move_value
            best_move = move  # Guarda la jugada óptima hasta ahora

        # Actualiza el valor de alfa para la poda
        alpha = max(alpha, best_value)

    # Retorna la mejor jugada encontrada después de evaluar todas las opciones
    return best_move


def game_over(tablero_global):
    x_win = verificar_victoria_global(tablero_global, 'X')
    o_win = verificar_victoria_global(tablero_global, 'O')
    full_board = todos_tableros_llenos(tablero_global)

    return x_win or o_win or full_board


def get_valid_moves(tableros, last_move, tablero_global):
    # Inicializa la lista de movimientos válidos
    valid_moves = []

    # Verifica si no hay última jugada, si el subtablero correspondiente está lleno,
    # o si ya fue ganado en el tablero global.
    if last_move is None or tablero_lleno(last_move) or tablero_global[casilla[last_move.lower()]] != '':
        # Recorre cada subtablero disponible
        for i, subtablero in tableros.items():
            # Verifica si el subtablero está disponible para jugar (sin ganar) en el tablero global
            if i.isupper() and tablero_global[casilla[i.lower()]] == '':
                # Busca casillas vacías en el subtablero actual
                for j, cell in enumerate(subtablero):
                    if cell == '':
                        # Agrega la jugada como (subtablero, casilla)
                        valid_moves.append((i, chr(ord('a') + j)))
    else:
        # Si hay una restricción (por la última jugada), se debe jugar en ese subtablero
        target_subtablero = tableros[last_move.upper()]

        # Busca casillas vacías en el subtablero correspondiente
        for j, cell in enumerate(target_subtablero):
            if cell == '':
                # Agrega la jugada como (subtablero, casilla)
                valid_moves.append((last_move.upper(), chr(ord('a') + j)))

    # Retorna la lista de movimientos válidos encontrados
    return valid_moves


def make_move(tablero_global, tableros, move, player):
    # Realiza copias del tablero global y de los subtableros para no modificar los originales
    new_tablero_global = tablero_global.copy()
    new_tableros = {k: v[:] for k, v in tableros.items()}

    # Desempaqueta la jugada en subtablero y posición
    subtablero, position = move

    # Marca la casilla del subtablero con el símbolo del jugador ('X' o 'O')
    new_tableros[subtablero][casilla[position]] = player

    # Verifica si el jugador ha ganado el subtablero
    if ha_ganado(new_tableros[subtablero], player):
        # Si ganó, marca ese subtablero como ganado en el tablero global
        new_tablero_global[casilla[subtablero.lower()]] = player

    # Retorna los nuevos estados del tablero global y los subtableros
    return new_tablero_global, new_tableros


def heuristic_evaluation(tablero_global, tableros):
    score = 0
    
    # Evaluar cada subtablero
    for subtablero, estado in tableros.items():
        if subtablero.isupper():
            score += evaluate_subtablero(estado, tablero_global[casilla[subtablero.lower()]])
    
    # Evaluar el tablero global
    score += evaluate_global_tablero(tablero_global) * 15  # Aumentamos el peso del tablero global
    
    return score

def evaluate_subtablero(subtablero, global_state):
    if global_state == 'X':
        return 100  # Aumentamos el valor de ganar un subtablero
    elif global_state == 'O':
        return -100
    
    score = 0
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontales
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticales
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    
    # Valor de las posiciones
    position_values = [3, 2, 3, 2, 4, 2, 3, 2, 3]  # Centro y esquinas valen más
    
    for i, symbol in enumerate(subtablero):
        if symbol == 'X':
            score += position_values[i]
        elif symbol == 'O':
            score -= position_values[i]
    
    # Evaluar líneas
    for line in lines:
        x_count = sum(1 for i in line if subtablero[i] == 'X')
        o_count = sum(1 for i in line if subtablero[i] == 'O')
        
        if x_count == 3:
            score += 50
        elif x_count == 2 and o_count == 0:
            score += 10
        elif x_count == 1 and o_count == 0:
            score += 1
        elif o_count == 3:
            score -= 50
        elif o_count == 2 and x_count == 0:
            score -= 10
        elif o_count == 1 and x_count == 0:
            score -= 1
    
    return score

def evaluate_global_tablero(tablero_global):
    score = 0
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Ganar en Horizontales
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Ganar en Verticales
        [0, 4, 8], [2, 4, 6]              # Ganar en Diagonales
    ]
    
    # Valor de las posiciones en el tablero global
    position_values = [3, 2, 3, 2, 4, 2, 3, 2, 3]  # Centro y esquinas valen más
    
    for i, symbol in enumerate(tablero_global):
        if symbol == 'X':
            score += position_values[i] * 5  # Aumentamos el peso en el tablero global
        elif symbol == 'O':
            score -= position_values[i] * 5
    
    # Evaluar líneas en el tablero global
    for line in lines:
        x_count = sum(1 for i in line if tablero_global[i] == 'X')
        o_count = sum(1 for i in line if tablero_global[i] == 'O')
        
        if x_count == 3:
            return 1000  # Victoria inmediata
        elif x_count == 2 and o_count == 0:
            score += 50
        elif x_count == 1 and o_count == 0:
            score += 10
        elif o_count == 3:
            return -1000  # Derrota inmediata
        elif o_count == 2 and x_count == 0:
            score -= 50
        elif o_count == 1 and x_count == 0:
            score -= 10
    
    return score

def jugar(tablero_global):
    juego_activo = True
    turno = 1 #inicializar en 1 para que empiece el jugador humano
    restriccion = None

    while juego_activo:
        print("Inicio del Juego: ULTIMATE TIC TAC TOE")
        jugador_actual = determinar_jugador(turno)
        
        if jugador_actual == 'X':  # Jugador IA
            move = get_best_move(tablero_global, tableros, restriccion, depth=5)
            grande, peque = move
            print(f"La IA juega en el tablero {grande}, casilla {peque}")
        else:  # Jugador humano
            if restriccion is None or tablero_lleno(restriccion) or tablero_global[casilla[restriccion.lower()]] != '':
                print("Puedes jugar en cualquier tablero disponible.")
                while True:
                    grande = input("Escribe la coordenada del tablero grande (A-I): ").upper()
                    if grande in 'ABCDEFGHI' and tablero_global[casilla[grande.lower()]] == '':
                        break
                    else:
                        print("Entrada inválida o tablero ya ganado. Por favor, elige otro.")
            else:
                print(f"Debes jugar en el tablero {restriccion.upper()}")
                grande = restriccion.upper()
            
            peque = input(f"Escribe la coordenada del tablero pequeño en {grande} (a-i): ").lower()

        restriccion, tablero_global = mandar_coordenadas(grande, peque, jugador_actual, tablero_global, tableros)
        imprimirTablero()

        if verificar_victoria_global(tablero_global, jugador_actual):
            print(f"El jugador {jugador_actual} ha ganado el juego global.")
            juego_activo = False
            

        turno += 1

        if todos_tableros_llenos(tablero_global):
            print("¡Empate! Todos los tableros están llenos.")
            juego_activo = False

        print("Estado del tablero global:")
        print(tablero_global[:3])
        print(tablero_global[3:6])
        print(tablero_global[6:])

        # Verificar si el próximo movimiento es válido
        if restriccion and tablero_global[casilla[restriccion.lower()]] != '':
            restriccion = None  # Resetear la restricción si el próximo subtablero ya está ganado

if __name__ == '__main__':
    tablero_global = ['','','','','','','','','']
    jugar(tablero_global)
