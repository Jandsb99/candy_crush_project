class ScreenManager:
    def __init__(self, matriu):
        self.matriu = matriu
        self.valor_matriu = len(matriu)
        self.llargada = 3

    def main_loop(self):
        while True:
            x0 = input()
            y0 = input()
            x1 = input()
            y1 = input()

            self.rearrange(x0, y0, x1, y1)


    def clear(self, x, y):
        """
        Clear serveix per a comprovar que la matriu sigui correcte,
        és a dir, que tres valors consecutius (en horitzontal, vertical o diagonal) siguin DIFERENTS i
        modifica els valors a 0

        Parameters:
        -----------
        x: int
            Coordenada x
        y: int
            Coordenada y

        """
        needs_to_clear, dx, dy = self.unchained(x, y)
        if needs_to_clear:
            self.set_coordenades(x, y, 0)
            self.set_coordenades(x + dx, y + dy, 0)
            self.set_coordenades(x + dx + dx, y + dy + dy, 0)
        else:
            pass

    def coordenades(self, x, y):
        """
        Coordenades serveix per retornar coordenades de les posicions de diferents valors dins de la
        matriu

        Parameters:
        -----------
        x: int
            Coordenada x
        y:int
            Coordenada y

        Returns:
        --------
        (int)
        """
        return self.matriu[y][x]

    def set_coordenades(self, x, y, v):
        """
        Set_coordenades permet guardar un valor v a unes coordenades x y.

        Parameters:
        -----------
        x: int
            Coordenada x
        y: int
            Coordenada y
        v: int
            Valor de la coordenada
        """
        self.matriu[y][x] = v

    def chain(self, x, y, dx, dy):
        """
        Chain serveix per comprovar si dins la matriu 3 valors consecutius en direcció x, y o xy són iguals

        Parameters:
        -----------
        x: int
            Coordenada x
        y:int
            Coordenada y
        dx:int
            Direcció en horitzontal
        dy:int
            Direcció en vertical

        Returns:
        --------
        (bool)
        """
        max_x = x+(self.llargada-1)*dx
        max_y = y+(self.llargada-1)*dy
        if 0 > max_x or max_x >= self.valor_matriu:
            return False
        if 0 > max_y or max_y >= self.valor_matriu:
            return False

        for i in range(self.llargada-1):
            if self.coordenades(x,y) != self.coordenades(x+dx,y+dy):
                return False
            x = x+dx
            y = y+dy
        return True

    def unchained(self, x, y):
        """
        Donat un punt x,y de la matriu, comprovarà si existeix una cadena i retornarà si es cert o es fals
        Parameters:
        -----------
        x: int
            Coordenada x
        y:int
            Coordenada y

        Returns:
        --------
        (bool)
        """
        dx = -1
        dy = -1
        while dx < 2:
            if dx == 0 and dy == 0:
                dy = dy + 1
                continue
            if self.chain(x,y,dx,dy):
                return True, dx, dy
            dy = dy+1
            if dy > 1:
                dy = -1
                dx = dx+1
        return False, None, None

    @staticmethod
    def swap(a, b):
        """
        Donat dos valors a i b, retorna b i a.
        Parameters:
        -----------
        a: int
            Valor a
        b:int
            Valor b

        Returns:
        --------
        b a
        """
        return b, a

    def rearrange(self, x0, y0, x1, y1):
        """
        Donat dos coordenades x0,y0 i x1,y1, canviar les posicions a la matriu tals que x1,y1 i x0,y0.
        Parameters:
        -----------
        x0: int
            Valor x coordenada x0,y0
        y0: int
            Valor y coordenada x0,y0
        x1: int
            Valor x coordenada x1,y1
        y1: int
            Valor y coordenada x1,y1
        """
        v0 = self.coordenades(x0, y0)
        v1 = self.coordenades(x1, y1)

        v0, v1 = self.swap(v0, v1)

        self.set_coordenades(x0, y0, v0)
        self.set_coordenades(x1, y1, v1)