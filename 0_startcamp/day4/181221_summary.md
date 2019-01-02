# 181221 수업정리

`'https://ide.c9.io/eduyu/startcamp'`

​			'domain'



```python
@app.route('eduyu/startcamp')
def username_workspace():
    return 'username & workspace'

# 자동으로?
$ export FLASK_ENV='development'
$ flast run -h 0.0.0.0 -p8080
#or
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
$ export FLASK_ENV='development'
$ python3 app.py
```

$ sudo pip3 install beautifulsoup4



선생님 c9

ide.c9.io/eduyu/startcamp

기능을 쓰려면  import

 templates 폴더에 있는 



텔레그램 봇

주소 https://api.telegram.org/bot681028294:AAHg1Y8EJNdmudT9MoMV-gMixIPSDIynUvg/getUpdates

(https://api.telegram.org/bot<key값>/getUpdates)

from id가 우리의 아이디



https://api.telegram.org/bot681028294:AAHg1Y8EJNdmudT9MoMV-gMixIPSDIynUvg/sendMessage?chat_id=616428339&text=Happyhippo

(https://api.telegram.org/bot<key값>sendMessage?chat_id=<ID_no>&text=<하고싶은말>)

bot이 <하고싶은말>을 보내줌



```python
import requests

MY_CHAT_ID = '616428339'
BOT_TOKEN ='681028294:AAHg1Y8EJNdmudT9MoMV-gMixIPSDIynUvg' #대문자 이름은 상수
msg = 'HappyHacking'

url = "https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg)

response = requests.get(url)#요청
print(response.json()) #.json() 안하면 str이 아니라 딕셔너리로 됨 #요청 후 영수증

#input 에 사용자가 말함
#route 에 말해라! 넣어줌
```









