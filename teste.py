import requests

resposta = requests.get("https://parallelum.com.br/fipe/api/v1/carros/marcas")

# Verifica se a requisição deu certo
print(resposta.status_code)

# Mostra os dados em formato JSON
print(resposta.json())