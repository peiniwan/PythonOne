

from aip import AipOcr
# pip install aip
APP_ID = '1131473' \
         '6'
API_KEY = '8Z2HYrpUM1PyGIqGass9MaYC'
SECRET_KEY = 'njq3OGA1RXdRal8LY25eZCwRjpBBNv2R'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
with open('D:\\test2.png', 'rb') as f:
    img = f.read()
    msg = client.general(img)
    for i in msg.get('words_result'):
        print(i.get('words'))
