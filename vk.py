import requests
from datetime import datetime
import db

token_user = "188c4347188c4347188c4347861b999ff41188c188c43477d93a35f89f2824bab58942f"
version = "5.154"
domain = "overhearfefu"


our_data = []


for x in range(0, 10_000, 100):
    response = requests.get('https://api.vk.com/method/wall.get',
                            params={'access_token': token_user,
                                    'v': version,
                                    'domain': domain,
                                    'count': 100,
                                    'filter': str('owner'),
                                    'offset': x})

    data = response.json()['response']['items']
    for y in data:
        ti = y['date']
#        unit = (datetime.fromtimestamp(ti).strftime('%Y'), y['text'])
        ti1 = int(datetime.fromtimestamp(ti).strftime('%Y'))
        ti2 = int(datetime.fromtimestamp(ti).strftime('%m'))
        # our_data.append(unit)
        try:
            db.insert_post(ti1, ti2, y['text'])
        except:
            mystr = y['text']
            newstr = mystr.replace("’", " ")
            newstr = mystr.replace("'", " ")
            db.insert_post(ti1, ti2, newstr)
        # try:
        #     cur.execute(f"""INSERT INTO posts (year, data) VALUES('{ti1}', '{newstr}')""")
        # except:
        #     print("error!!!  ", ti1, newstr)
        #     break
       # try:
       #     cur.execute(f"""INSERT INTO posts (year, data) VALUES('{ti1}', '{y['text']}')""")
       #  except:
       #      print(y['text'])
       #      break
    print(x)

# print(our_data)

