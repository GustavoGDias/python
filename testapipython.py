# Client-ID:'4o9ljha7qvrspye99lh38jbmm9lwti', Authorization': 'Bearer qqmry7v0gbdyyp15a3modlksw75esx'

from requests import post
response = post('https://api.igdb.com/v4/game_modes', **{'headers': {'Client-ID': '4o9ljha7qvrspye99lh38jbmm9lwti',
                'Authorization': 'Bearer qqmry7v0gbdyyp15a3modlksw75esx'}, 'data': 'fields checksum,created_at,name,slug,updated_at,url;'})
print("response: %s" % str(response.json()))
