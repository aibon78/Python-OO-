class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False  # Inicializa o atributo privado _ativo
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

    @ativo.setter
    def ativo(self, valor):
        self._ativo = valor

    @staticmethod
    def listar_restaurantes():
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

# Criação dos objetos Restaurante
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.ativo = True
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

# Listar os restaurantes
Restaurante.listar_restaurantes()
