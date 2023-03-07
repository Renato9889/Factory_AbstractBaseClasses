from felinos import Leao,Gato,Cachorro
from traducao import TradutorFactory

#Exemplo de Abstract Base 
#Abstract Base Classes é um modelo base para outras classes, ela em si não implementa nenhum método, 
# mas as classes derivadas que herdam dela, irão implementar esses métodos abstratos.
# Esse tipo de classe é importante quando temos várias classes que são dependentes de um núcleo base. 
# Supondo que temos que alimentar vários animais e vamos criar uma classe para cada animal: Gato, Cachorro e Leão. 
# Podemos criar uma classe base que terá o método comer e cada classe derivada de Animal, 
# por padrão terá que implementar como aquele animal irá comer:

animais = [Leao(), Gato(), Cachorro()]

for felinos in animais:
    felinos.comer()

#Exemplo de Factory 
#A Factory é um padrão de projeto que prevê a criação de objetos a partir da classe,
#então, com base em uma condição, determinada classe é instanciada, é uma fábrica de construção.
#supondo que temos uma classe “Tradutor”, onde para cada localização irá retornar um tradutor específico,
#ou seja, será responsável por determinar qual tipo de objeto criar sem que o usuário tenha acesso a classe
#escolhida ou tenha que passar vários parâmetros. Veja como ficaria aplicando o conceito do factory method.

texto = TradutorFactory().factory('en').traduz()
print(texto)
