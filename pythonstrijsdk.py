import requests
link = "https://www.chess.com/login_check"
data = {"username":"username","password":"password"}
r = requests.post(link, data=data)