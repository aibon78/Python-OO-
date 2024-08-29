Este repositório contém exemplos e exercícios práticos para avançar na orientação a objetos (OO) em Python e aprender a consumir APIs RESTful. O objetivo é proporcionar uma compreensão mais profunda dos conceitos de OO e como integrá-los em projetos que consomem dados de APIs externas.

⚪ Conceitos Abordados

• Orientação a Objetos (OO):

• Classes e Objetos

• Herança

• Encapsulamento

• Abstração

• Polimorfismo

• Métodos Mágicos

Consumo de APIs:

Requisições HTTP com requests

Autenticação e autorização (ex. OAuth)

Manipulação de dados JSON

Tratamento de erros em requisições

⚫ Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:

Python 3.x

pip (gerenciador de pacotes Python)

Além disso, é recomendado ter conhecimento básico de Python e familiaridade com conceitos de orientação a objetos.

*Instalação*
Clone este repositório para sua máquina local:

```git clone https://github.com/seu-usuario/nome-do-repositorio.git```

Navegue até o diretório do projeto:

```cd nome-do-repositorio```

Instale as dependências necessárias:

```pip install -r requirements.txt```

*Exemplos*

Classes e Herança
Neste exemplo, você aprenderá a criar classes base e derivadas, explorando a reutilização de código através da herança.
```
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

dog = Cachorro("Rex")
cat = Gato("Mia")
print(dog.emitir_som())  # Saída: Au Au!
print(cat.emitir_som())  # Saída: Miau!
```
⚪ Encapsulamento e Abstração
 ↪︎ Aprenda a encapsular dados e a utilizar a abstração para criar interfaces simples e eficazes.

⚫ Polimorfismo
 ↪︎ Veja como implementar polimorfismo para permitir que diferentes classes implementem métodos de maneiras variadas.

⚪Manipulação de APIs RESTful
 ↪︎ Aprenda a fazer requisições GET, POST, PUT, DELETE e a manipular as respostas das APIs.

```
import requests

response = requests.get('https://api.exemplo.com/dados')
if response.status_code == 200:
    dados = response.json()
    print(dados)
else:
    print(f"Erro ao fazer requisição: {response.status_code}")
```

*Como Contribuir*

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

➊.Faça um fork deste repositório.

➋.Crie uma nova branch: git checkout -b minha-feature.

➌.Faça suas alterações e commit: git commit -m 'Minha nova feature'.

➍.Envie para a branch original: git push origin minha-feature.

➎.Abra um pull request.
