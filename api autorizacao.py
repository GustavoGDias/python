from igdb.wrapper import IGDBWrapper
#wrapper = IGDBWrapper("4o9ljha7qvrspye99lh38jbmm9lwti", "qqmry7v0gbdyyp15a3modlksw75esx")


# Substitua 'SEU_CLIENT_ID' e 'SEU_APP_ACCESS_TOKEN' pelos seus valores reais
wrapper = IGDBWrapper("4o9ljha7qvrspye99lh38jbmm9lwti", "qqmry7v0gbdyyp15a3modlksw75esx")

# Consulta por jogos da franquia Zelda
query = "zelda"

# Consulta para buscar jogos relacionados à franquia Zelda
byte_array = wrapper.api_request(
    'games',
    f'fields name, summary, cover; search "{query}"; limit 5;'
)

# Mostra os dados dos jogos relacionados à franquia Zelda
games_info = byte_array.decode('utf-8')
print(games_info)

