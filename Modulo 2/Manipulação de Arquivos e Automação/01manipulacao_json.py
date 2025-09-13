import json
# Convertendo um arquivo json em Dicionário

# String no formato json, usar aspas duplas e os valores boolenos em minúsculo

json_data ='{"nome":"Ana","idade":30,"estudadnte":true}'

dados_pyton = json.loads(json_data)

print(dados_pyton['nome'])
print(dados_pyton['idade'])
print(dados_pyton['estudante'])