
class RomanNumber:
    def __init__(self, roman):
        self.roman = roman
        self.i = 0
        self.estado_actual = False

        pass

    def leer(self):
        while self.i < len(self.roman):
            c = self.roman[self.i]
            self.i += 1 #aumento el contador para leer el caracter siguiente
            return c
        return None
    
    def evaluar(self):
        self.start()
        return self.estado_actual
    
    def start(self):
        self.estado_inicial()

    def estado_inicial(self):
        c = self.leer()
        if c == 'I':
            self.estado_I()
        elif c == 'V':
            self.estado_V()
        elif c == 'X':
            self.estado_X()
        elif c == 'L':
            self.estado_residual()
        elif c == None:
            self.estado_actual = False  # Cadena vacía
        else:
            self.estado_actual = False  # Caracter inválido

    def estado_I(self):
        c = self.leer()
        if c == 'I':
            self.estado_II() #III
        elif c == 'V':
            self.estado_residual() #IV
        elif c == 'X':
            self.estado_residual() #IX
        elif c == None:
            self.estado_actual = True   #I
        else:
            self.estado_actual = False

    def estado_II(self):
        c = self.leer()
        if c == 'I':
            self.estado_residual() #III
        elif c == None:
            self.estado_actual = True #II
        else:
            self.estado_actual = False

    def estado_V(self):
        c = self.leer()
        if c == 'I':
            self.estado_VI()
        elif c == None:
            self.estado_actual = True #V
        else:
            self.estado_actual = False 
    
    def estado_VI(self):
        c = self.leer()
        if c == 'I':
            self.estado_VII()
        elif c == None:
            self.estado_actual = True #VI
    
    def estado_VII(self):
        c = self.leer()
        if c == 'I':
            self.estado_residual() #VIII - 8
        elif c == None:
            self.estado_actual = True #VII - 7
        else:
            self.estado_actual = False
    
    def estado_X(self):
        c = self.leer()
        if c == 'I':
            self.estado_I()
        elif c == 'V':
            self.estado_V()
        elif c == 'X':
            self.estado_XX()
        elif c == 'L':
            self.estado_XL()
        elif c == None:
            self.estado_actual = True #X
        else:
            self.estado_actual = False
    
    def estado_XX(self):
        c = self.leer()
        if c == 'I':
            self.estado_I()
        elif c == 'V':
            self.estado_V()
        elif c == 'X':
            self.estado_XXX()
        elif c == None:
            self.estado_actual = True
    
    def estado_XXX(self):
        c = self.leer()
        if c == 'I':
            self.estado_I()
        elif c == 'V':
            self.estado_V()
        elif c == None:
            self.estado_actual = True #XXX
        else:
            self.estado_actual = False
    
    def estado_XL(self):
        c = self.leer()
        if c == 'I':
            self.estado_I()
        elif c == 'V':
            self.estado_V()
        elif c == None:
            self.estado_actual = True #XL - 40
        else:
            self.estado_actual = False

    def estado_residual(self):
        c = self.leer()
        if c == None:
            self.estado_actual = True
        else:
            self.estado_actual = False
            
if __name__== "__main__":
    i=input("Ingresa un numero romano del I al L\n")
    """romanos = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
            'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX',
            'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX',
            'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI', 'XXXVII', 'XXXVIII', 'XXXIX', 'XL',
            'XLI', 'XLII', 'XLIII', 'XLIV', 'XLV', 'XLVI', 'XLVII', 'XLVIII', 'XLIX', 'L']
    for i in romanos:"""
    numeroRomano=RomanNumber(i)
    mensaje=lambda valido: "Numero valido" if valido else "Numero invalido"
    print(f"{i:7} → {mensaje(numeroRomano.evaluar())}")
    

    
    