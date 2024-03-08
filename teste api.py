import requests

# URL da solicitação de token de acesso
token_url = "https://id.twitch.tv/oauth2/token"

# Parâmetros necessários para a solicitação de token de acesso
params = {
    "client_id": "4o9ljha7qvrspye99lh38jbmm9lwti",
    "client_secret": "rv5b7quij54ya99utmvafibdza35hj",
    "grant_type": "client_credentials",
}

# Enviar a solicitação POST
response = requests.post(token_url, data=params)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Obter o token de acesso e imprimir
    access_token = response.json().get('access_token')
    print("Token de acesso obtido com sucesso:", access_token)
else:
    print("Erro ao obter o token de acesso:", response.text)