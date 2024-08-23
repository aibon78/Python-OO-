class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    def __str__(self)

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca,restaurante_pizza]

print(dir(restaurante_praca))
print(restaurante_pizza)

