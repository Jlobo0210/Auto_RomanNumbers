class FloatAutomaton:
    def __init__(self, cadena):
        self.cadena = cadena
        self.i = 0
        self.estado_actual = False
    
    def leer(self):
        if self.i < len(self.cadena):
            c = self.cadena[self.i]
            self.i += 1
            return c
        return None
    
    def evaluar(self):
        self.start()
        return self.estado_actual

    def start(self):
        self.estado_inicial()

    def estado_inicial(self):
        c = self.leer()
        if c is not None and c in '+-':
            self.estado_signo()
        elif c is not None and c.isdigit():
            self.estado_entero()
        elif c == '.':
            self.estado_punto()
        else:
            self.estado_actual = False

    def estado_signo(self):
        c = self.leer()
        if c is not None and c.isdigit():
            self.estado_entero()
        elif c == '.':
            self.estado_punto()
        else:
            self.estado_actual = False

    def estado_punto(self):
        c = self.leer()
        if c is not None and c.isdigit():
            self.estado_decimal()
        elif c is None:
            self.estado_actual = True
        else:
            self.estado_actual = False

    def estado_entero(self):
        c = self.leer()
        if c is None:
            self.estado_actual = True 
        elif c is not None and c.isdigit():
            self.estado_entero()
        elif c == '.':
            self.estado_punto()
        elif c is not None and c in 'eE':
            self.estado_exponencial()
        else:
            self.estado_actual = False
    
    def estado_decimal(self):
        c = self.leer()
        if c is not None and c.isdigit():
            self.estado_decimal()
        elif c is not None and c in 'eE':
            self.estado_exponencial()
        elif c is None:
            self.estado_actual = True
        else:
            self.estado_actual = False
    
    def estado_exponencial(self):
        c = self.leer()
        if c is not None and c in '+-':
            self.estado_expo_signo_num()
        elif c is not None and c.isdigit():
            self.estado_expo_num()
        else:
            self.estado_actual = False
    
    def estado_expo_signo_num(self):
        c = self.leer()
        if c is not None and c.isdigit():
            self.estado_expo_num()
        else:
            self.estado_actual = False
    
    def estado_expo_num(self):
        c = self.leer()
        if c is not None and c.isdigit():
            self.estado_expo_num()
        elif c is None:
            self.estado_actual = True
        else:
            self.estado_actual = False


if __name__ == "__main__":
    mensaje=lambda valido: "Cadena valida" if valido else "Cadena invalida"
    while True:
        try:
            cadena = input("Ingrese una cadena para evaluar si es un punto flotante (o exit para terminar): \n")
            if cadena.lower() == 'exit':
                break
            automata = FloatAutomaton(cadena)
            print(f"{cadena} → {mensaje(automata.evaluar())}")
        except Exception as e:
            print(f"Error: {e}")