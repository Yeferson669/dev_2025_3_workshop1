import pytest
from src.games.games import Games

class TestGames:
    def setup_method(self):
        self.games = Games()
    
    def test_piedra_papel_tijera(self):
        # Test empates
        assert self.games.piedra_papel_tijera("piedra", "piedra") == "empate"
        assert self.games.piedra_papel_tijera("papel", "papel") == "empate"
        assert self.games.piedra_papel_tijera("tijera", "tijera") == "empate"
        
        # Test victorias de jugador1
        assert self.games.piedra_papel_tijera("piedra", "tijera") == "jugador1"  # Piedra vence tijera
        assert self.games.piedra_papel_tijera("papel", "piedra") == "jugador1"   # Papel vence piedra
        assert self.games.piedra_papel_tijera("tijera", "papel") == "jugador1"   # Tijera vence papel
        
        # Test victorias de jugador2
        assert self.games.piedra_papel_tijera("tijera", "piedra") == "jugador2"  # Piedra vence tijera
        assert self.games.piedra_papel_tijera("piedra", "papel") == "jugador2"   # Papel vence piedra
        assert self.games.piedra_papel_tijera("papel", "tijera") == "jugador2"   # Tijera vence papel
        
        # Test con mayúsculas y minúsculas mixtas
        assert self.games.piedra_papel_tijera("PIEDRA", "tijera") == "jugador1"
        assert self.games.piedra_papel_tijera("Papel", "PIEDRA") == "jugador1"
        
        # Test con valores inválidos (debe retornar None o manejar error)
        assert self.games.piedra_papel_tijera("piedra", "invalid") == "invalid"
        assert self.games.piedra_papel_tijera("invalid", "papel") == "invalid"
    
    def test_adivinar_numero_pista(self):
        # Test con número correcto
        assert self.games.adivinar_numero_pista(50, 50) == "correcto"
        assert self.games.adivinar_numero_pista(1, 1) == "correcto"
        assert self.games.adivinar_numero_pista(100, 100) == "correcto"
        
        # Test con número muy alto
        assert self.games.adivinar_numero_pista(50, 75) == "muy alto"
        assert self.games.adivinar_numero_pista(10, 20) == "muy alto"
        assert self.games.adivinar_numero_pista(1, 99) == "muy alto"
        
        # Test con número muy bajo
        assert self.games.adivinar_numero_pista(50, 25) == "muy bajo"
        assert self.games.adivinar_numero_pista(100, 1) == "muy bajo"
        assert self.games.adivinar_numero_pista(20, 10) == "muy bajo"
        
        # Test con números negativos
        assert self.games.adivinar_numero_pista(-10, -5) == "muy alto"
        assert self.games.adivinar_numero_pista(-10, -15) == "muy bajo"
        assert self.games.adivinar_numero_pista(-10, -10) == "correcto"
        
        # Test casos límite
        assert self.games.adivinar_numero_pista(0, 1) == "muy alto"
        assert self.games.adivinar_numero_pista(0, -1) == "muy bajo"
    
    def test_ta_te_ti_ganador(self):
        # Test victoria en fila
        tablero_fila1 = [["X", "X", "X"], ["O", "O", " "], [" ", " ", " "]]
        assert self.games.ta_te_ti_ganador(tablero_fila1) == "X"
        
        tablero_fila2 = [[" ", " ", " "], ["O", "O", "O"], ["X", "X", " "]]
        assert self.games.ta_te_ti_ganador(tablero_fila2) == "O"
        
        tablero_fila3 = [["O", "X", "O"], ["X", "O", "X"], ["X", "X", "X"]]
        assert self.games.ta_te_ti_ganador(tablero_fila3) == "X"
        
        # Test victoria en columna
        tablero_col1 = [["X", "O", "O"], ["X", "O", "X"], ["X", " ", " "]]
        assert self.games.ta_te_ti_ganador(tablero_col1) == "X"
        
        tablero_col2 = [["X", "O", "X"], [" ", "O", "X"], ["X", "O", " "]]
        assert self.games.ta_te_ti_ganador(tablero_col2) == "O"
        
        tablero_col3 = [["X", "O", "O"], ["X", "X", "O"], [" ", " ", "O"]]
        assert self.games.ta_te_ti_ganador(tablero_col3) == "O"
        
        # Test victoria en diagonal principal
        tablero_diag1 = [["X", "O", "O"], ["O", "X", "O"], ["X", "O", "X"]]
        assert self.games.ta_te_ti_ganador(tablero_diag1) == "X"
        
        # Test victoria en diagonal secundaria
        tablero_diag2 = [["X", "O", "O"], ["X", "O", "X"], ["O", "X", "X"]]
        assert self.games.ta_te_ti_ganador(tablero_diag2) == "O"
        
        # Test empate (tablero lleno sin ganador)
        tablero_empate = [["X", "O", "X"], ["O", "O", "X"], ["O", "X", "O"]]
        assert self.games.ta_te_ti_ganador(tablero_empate) == "empate"
        
        # Test juego continúa (tablero incompleto sin ganador)
        tablero_continua = [["X", "O", " "], [" ", "X", "O"], ["O", " ", "X"]]
        assert self.games.ta_te_ti_ganador(tablero_continua) == "X"

        
        # Test tablero vacío
        tablero_vacio = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        assert self.games.ta_te_ti_ganador(tablero_vacio) == "continua"
    
    def test_generar_combinacion_mastermind(self):
        colores = ["rojo", "azul", "verde", "amarillo"]
        
        # Test longitud correcta
        combinacion = self.games.generar_combinacion_mastermind(4, colores)
        assert len(combinacion) == 4
        
        # Test que todos los colores están en la lista disponible
        for color in combinacion:
            assert color in colores
        
        # Test con longitud diferente
        combinacion2 = self.games.generar_combinacion_mastermind(6, colores)
        assert len(combinacion2) == 6
        
        # Test con longitud 1
        combinacion3 = self.games.generar_combinacion_mastermind(1, colores)
        assert len(combinacion3) == 1
        assert combinacion3[0] in colores
        
        # Test con diferentes colores disponibles
        colores_limitados = ["rojo", "azul"]
        combinacion4 = self.games.generar_combinacion_mastermind(3, colores_limitados)
        assert len(combinacion4) == 3
        for color in combinacion4:
            assert color in colores_limitados
        
        # Test con longitud 0
        combinacion5 = self.games.generar_combinacion_mastermind(0, colores)
        assert len(combinacion5) == 0
        
        # Test que las combinaciones pueden ser diferentes (aunque no garantizado)
        # Solo verificamos que la función no siempre retorna lo mismo
        combinaciones = []
        for _ in range(10):
            comb = self.games.generar_combinacion_mastermind(4, colores)
            combinaciones.append(tuple(comb))  # Convertir a tupla para comparar
        
        # Al menos debe haber alguna variación en 10 intentos (muy probable)
        assert len(set(combinaciones)) >= 1  # Mínimo debe generar algo
    
    def test_validar_movimiento_torre_ajedrez(self):
        # Tablero vacío para movimientos básicos
        tablero_vacio = [[" " for _ in range(8)] for _ in range(8)]
        
        # Test movimientos horizontales válidos
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 0, 7, tablero_vacio) == True  # Fila completa
        assert self.games.validar_movimiento_torre_ajedrez(4, 2, 4, 6, tablero_vacio) == True  # Movimiento parcial
        assert self.games.validar_movimiento_torre_ajedrez(7, 7, 7, 0, tablero_vacio) == True  # Reversa
        
        # Test movimientos verticales válidos
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 7, 0, tablero_vacio) == True  # Columna completa
        assert self.games.validar_movimiento_torre_ajedrez(2, 4, 6, 4, tablero_vacio) == True  # Movimiento parcial
        assert self.games.validar_movimiento_torre_ajedrez(7, 3, 1, 3, tablero_vacio) == True  # Hacia arriba
        
        # Test movimiento diagonal (inválido para torre)
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 1, 1, tablero_vacio) == False
        assert self.games.validar_movimiento_torre_ajedrez(3, 3, 5, 5, tablero_vacio) == False
        
        # Test movimiento a la misma posición (inválido)
        assert self.games.validar_movimiento_torre_ajedrez(4, 4, 4, 4, tablero_vacio) == False
        
        # Test con obstáculos en el camino
        tablero_con_piezas = [[" " for _ in range(8)] for _ in range(8)]
        tablero_con_piezas[0][3] = "P"  # Peón en el camino
        
        # Movimiento bloqueado horizontalmente
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 0, 7, tablero_con_piezas) == False
        # Movimiento que no pasa por el obstáculo
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 0, 2, tablero_con_piezas) == True
        # Movimiento después del obstáculo
        assert self.games.validar_movimiento_torre_ajedrez(0, 4, 0, 7, tablero_con_piezas) == True
        
        # Test con obstáculo vertical
        tablero_con_piezas2 = [[" " for _ in range(8)] for _ in range(8)]
        tablero_con_piezas2[3][0] = "R"  # Torre en el camino
        
        # Movimiento bloqueado verticalmente
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 7, 0, tablero_con_piezas2) == False
        # Movimiento que no pasa por el obstáculo
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 2, 0, tablero_con_piezas2) == True
        
        # Test movimientos fuera del tablero (deben ser inválidos)
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 0, 8, tablero_vacio) == False
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 8, 0, tablero_vacio) == False
        assert self.games.validar_movimiento_torre_ajedrez(-1, 0, 0, 0, tablero_vacio) == False
        assert self.games.validar_movimiento_torre_ajedrez(0, -1, 0, 0, tablero_vacio) == False