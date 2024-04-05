# Avaliação 1 - Consumo API: Conversor de Moedas
Conversor de moedas simples desenvolvido em python para demonstrar o consumo de uma API pública utilizando a biblioteca requests. A API utilizada obtém as taxas de câmbio atualizadas e realiza conversões entre diferentes moedas.

# Como rodar esse projeto?
## Instalação
- Certifique-se de ter o Python instalado em sua máquina. Você pode baixar o Python em python.org.

- Clone este repositório para o seu ambiente local:

    git clone https://github.com/marquesluana/avaliacao1_consumoAPI.git

- Navegue até o diretório do projeto:

    cd... cd... cd avaliacao1_consumoAPI

- Instale as dependências necessárias usando pip:

    pip install -r requirements.txt

## Uso
- Execute o script conversormoedas.py:

py conversormoedas.py

Informe os valores desejados. Por exemplo:

      O código exibirá: Digite o valor a ser convertido:
  
      Você informa: 100
  

      O código exibirá: Digite a moeda de origem (ex: BRL, USD, EUR):
  
      Você informa: BRL
  

      O código exibirá: Digite a moeda de destino (ex: BRL, USD, EUR):
  
      Você informa: usd
  

Isso converterá 100 reais brasileiros para dólares americanos.


E dado essas informações o código retornará:

      O valor informado (100.0 BRL) convertido fica: 19.7 USD
