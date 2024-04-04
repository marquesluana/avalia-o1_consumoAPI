import requests

def converter_moeda(valor, moeda_entrada, moeda_saida):
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_entrada}"
    
    respostas = requests.get(url)
    
    if respostas.status_code == 200:
        dados = respostas.json()
        taxa = dados['rates'][moeda_saida]
        valor_convertido = valor * taxa
        print(f"O valor informado ({valor} {moeda_entrada}) convertido fica: {valor_convertido} {moeda_saida}")
    else:
        print("Erro ao converter moeda:", respostas.text)

if __name__ == "__main__":
    valor = float(input("Digite o valor a ser convertido: "))
    moeda_origem = input("Digite a moeda de origem (ex: BRL, USD, EUR): ").upper()
    moeda_destino = input("Digite a moeda de destino (ex: BRL, USD, EUR): ").upper()

    converter_moeda(valor, moeda_origem, moeda_destino)
