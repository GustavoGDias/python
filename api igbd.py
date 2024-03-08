from igdb.wrapper import IGDBWrapper

# Substitua 'seu_client_id' e 'seu_auth_token' pelos seus próprios dados de autenticação da API IGDB
client_id = '4o9ljha7qvrspye99lh38jbmm9lwti'
auth_token = 'qqmry7v0gbdyyp15a3modlksw75esx'

# Crie uma instância do IGDBWrapper com suas credenciais
wrapper = IGDBWrapper(client_id, auth_token)

# Consulta à API do IGDB buscando jogos relacionados ao termo 'Zelda'
query = 'fields name, summary, cover; search "Zelda"; limit 10;'
response = wrapper.api_request('games', query)

# Imprime a resposta
print(response)