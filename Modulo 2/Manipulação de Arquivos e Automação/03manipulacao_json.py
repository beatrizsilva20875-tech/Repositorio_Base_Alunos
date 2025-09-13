# Lendo um arquivo do tipo JSON
# Sempre iniciamos importando a biblioteca json
import json

# Abriremos o arquivo no modo "r" (leitura)
with open("dados.json", "r", encoding="utf-8") as arquivo:
    # Esse método json.load converte o conteúdo do arquivo JSON em um dicionário
    dados = json.load(arquivo)

# Exibindo o tipo da variável 'dados' para verificar se foi carregado corretamente
print(type(dados))
