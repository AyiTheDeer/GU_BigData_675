import requests

# uri = 'https://github.com/AyiTheDeer'
# app = '1340729416286301'
# url = 'https://api.instagram.com/oauth/access_token'

# code = 'AQB-Arz43Doa2edFWgFj8_vs4ZzQJPL1AzAUfHMzvKY-7EkKafm19r6_nh5_0ow4DW5ZSCnfwW1L6RBajD_-E_UhHS4MMntFvFXhseJSN7OSZvw79v3R_JfXsp1YhIxnmSYJC3Tnwk8wYeWq7gFYB2StFavYRFrJ3VMh7DTS_OOje8TubgjHxPXO7B4EyK4_RkdiZIEcRBy7VynDw3-MtAfOpr0Wlnl--uOAGXPi5v5-0Q'
# secret = 'f67c4fcc1b3639818dbb76a08a2e3f45'

# aut = f'{url}?client_id={app}&client_secret={secret}&grant_type=authorization_code&redirect_uri={uri}&code={code}'

# r = requests.post(aut)

# Все что выше не получилось. Пришлось генерировать лонг-лайв токен доступа, чтобы сделать это

u = 'https://graph.instagram.com/me?'
t = 'MY TOKEN'
f = 'id,username'
url = f'{u}fields={f}&access_token={t}'
r = requests.get(url)
print(r.json())
# {'id': '17841402087013077', 'username': 'ayithedeer'}

