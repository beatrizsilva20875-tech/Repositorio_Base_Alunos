# importamos o módulo json
import json

# Criamos um dicionário Python
dados = {
    "nome": "Maria",
    "idade": 30,
    "curso": ["Python", "Machine Learning"]
}

# Criar um arquivo JSON e escrever dentro dele
with open('dados.json', 'w', encoding='utf-8') as arquivo:  # 'w' é o modo para escrever
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
