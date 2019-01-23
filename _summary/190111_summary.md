# 190111 수업정리

## 1. Flask

- git bash에서 

```
cd TIL 에서
mkdir 04_Flask 만들고
cd 04_Flask/로 가서
mkdir first_app 을 만든다.
cd first_app/ 으로 가서
touch app.py 만든다.
pip -V 버전 확인하고
pip install flask 플라스크 설치하고
python -m pip install --upgrade pip =>pip버전 업글
code .으로 다 실행시킨다? 켠다?!
```

- vs에서

``` python
from flask import Flask # Flask라는 클래스를 빼쓰겠다!

app = Flask(__name__) #type(__name__)은 string / 객체를 생성했다!!

@app.route('/') # @은 decorator ,, .route('/') 는 method를 의미 ,, /뒤에 아무말도 없을때 보통 index 페이지라고 함
def index():
    return 'Hi!'

@app.route('/ssafy') # @은 decorator / .route('/') 는 method
def index():
    return 'Hi'

@app.route('/pick_lotto')
def pick_lotto():
    numbers = random.sample(range(1, 46), 6)
    return jsonify(numbers)

@app.route('/hi/kmj') #/뒤에 있는 이름을 정확하게 써줘야 동작함
def hi():
    return(f'hi kmj!')

@app.route('/hi/<string:name>') #<>안의 값은 변수
def hi(name):
    return(f'hi {name}!')

@app.route('/dictionary/<string:word>')
def my_dictionary(word):
    my_dic = {
        'apple': '사과',
        'banana': '바나나',
        'melon': '멜론',
        'cherry': '체리',
        'grapefruit': '자몽',
        'pomegranate': '석류'
    }

    if word in my_dic:
        return f'{word}은(는) {my_dic[word]}!!'
    else:
        return f'{word}은(는) 나만의 단어장에 없는 단어입니다!'

if __name__ == '__main__':   #run -> 서버가 돌고있다! <-> 서버가 죽었다ㅠㅠ
    app.run(debug=True) # **kwagrs 사용하여 입력된듯
```

/ => 최상단을 의미하며 root라고 함



- vs 터미널에서 python app.py 입력

```
 python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 
```

-> 프롬프트($)사라짐!!

Flask 라는 프로그램으로 만든 어플리케이션 응용프로그램의 이름은 'app'이다.

production = 배포, 완성되었으니 배포한 상태이다! (프로토타입=미완성, 개발중)

warning -> 배포 준비가 안되었으니 개발서버를 배포환경에서 사용하지 말아라ㅠㅠ

=>환경을 개발로 바꾸거나 개발 서버를 바꿔라!?

http://127.0.0.1:5000에서 일하고 있다! (ip:포트)

(서버를 돌린 상태에서 위의 주소 입력하면 접속 가능)



- http://127.0.0.1:5000/ 으로 접속

```
127.0.0.1 - - [11/Jan/2019 09:31:16] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [11/Jan/2019 09:31:16] "GET /favicon.ico HTTP/1.1" 404 -
```

11/Jan/2019 09:31:16 에 누가 왔다갔어요~

11/Jan/2019 09:31:16에 favicon.ico HTTP/1.1" 404 -   => .ico줘야하는데 없어서 못줬어요~

404 => 없어요~

http://127.0.0.1:5000/1 입력하면 "GET /1 HTTP/1.1" 404 - => 없어요!
 http://127.0.0.1:5000/ssafy 입력하면 "GET /ssafy HTTP/1.1" 404 - => 없어요!

#### 코드를 고치면 서버를 껐다가 다시 켜야합니다!!!



```$ python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 149-588-683
 * Running on http://0.0.0.0:3000/ (Press CTRL+C to quit)
 
```



- vs 터미널 bash에서

```
export FLASK_ENV='development' ; bash ; reset
```

export  = 변수 설정을 할거에요. 컴퓨터 자체에 변수 세팅을 때려넣는것!

FLASK_ENV 라는 환경변수에 'development'라는 내용을 넣어줄거에요.

```
$FLASK_ENV
bash: development: command not found
```

```
development
bash: development: command not found
```

```
#FLASK_ENV에 'development'라는 값이 들어있는 것 확인!
echo $FLASK_ENV 
development
```

```
#변수 초기화
$ export RUN_FLASK= 
```

```
$ $RUN_FLASK
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 149-588-683
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

개발환경으로 바뀜!!



#### - 앱을 만들어도 배포하려면 압축파일을 받아 설치하거나 사용자가 터미널에서 돌려야함.

=> 플라스크를 통해 주소를 넣어주면 쉽게 사용할 수 있다!!!

- 왜 함수 실행을 안했는데 서버에서는 실행되어 결과값이 나오는 것일까!?

app => 플라스크 서버 에서

route => 길을 뚫어놨는데

('/pick_lotto'): => 여기 들어오면 밑에 정의되어 있는 함수를 실행해라!! 



### 2. Git 

- git bash에서

```
cd ssafy_git/

git status

git pull랑 git push해보고

code . 로 열기
```

## - Basic workflow

```ㅠㅠ
$ git init
$ git status #빨간색확인
$ git add .
$ git status #초록색 확인(초록색만 커밋됨)
$ git commit -m '짧고 간결하고 현재형'

#github, bitbucket, gitlab etc... remote repo 를 생성
$ git remote add origin <REMOTE REPO URL.git>
$ git push (-u origin master) #첫번째만

#다른 컴퓨터라면,
$ git clone <REMOTE REPO URL.git> #downloadZIP => .git 없음ㅠㅠ
#작업작업
$ git add . && git commit -m 'MSG' && git push 
$ git add . ; git commit -m 'MSG' ; git push
# 한번에 작업 가능/ repo가 아닌곳에서 진행하면 &&는 에러남.진행안됨 ;은 에러나도 무시하고 진행

$ git pull
```



```
$ mkdir images 이미지 디렉토리를 만들고 이미지를 하나 저장해 놓는다.
$ ls 확인해보면 이미지 파일 보인다
$ mv cat.jpg images/ 이미지 디렉토리에 고양이이미지를 옮겨준다.
$ ls 로 확인
$ touch index.html 을 만들어준다.
$ git status 로 확인해본다.

```

- index.html에서 입력한다

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Learn git!</title>
</head>
<body>
    <img src="./images/cat.jpg" alt="cat" />
</body>
</html>
```

img에 alt 는 사진이 안나올때 어떤 사진인지 나오는 메시지로 

```
$ git add .
$ git status
$ git commit -m ''
#수정후..
$ git diff 달라진점 확인
$ git log 에서 확인
다시 add 하고 push
```



```
$ vim dummy.txt
# github에 add하고싶지 않은 파일이 있을때 (git에서 내려야지만 무시가능)
다른 bash에서 
$ touch .gitignore 에 숨길 파일을 지정해줌
 ->.gitignore에 들어가서 *.swp 나 *.txt 나 secrets/ 같이 지정해서 넣어주면 무시해줌
$ git status 보면 숨겨진 것 확인됨


# stage에 올렸는데 다시 내리고 싶을때
$ git rm dummy.txt
$ git rm --cached dummy.txt
$ git status 에서 내려간 것 확인

$ mkdir secrets 만듬
touch secrets/파일이름
 ->.gitignore에 들어가서 *.swp 나 *.txt 나 secrets/ 같이 지정해서 넣어주면 무시해줌



```



- branch

  master는 모두의 합의에 의해 건드려야함 보통 마스터는 건드리지 않고 각각의  branch가  merge(모으는) 식으로 진행함

```
$ git branch 지금 브랜치는 master -> 가장 메인 브랜치! 목록!!!
$ git branch about-page 어바웃페이지를 만듬
$ git checkout about-page 현재위치에서 나와 어바웃페이지로 가겠다!!
 -> master에서 about-page로 바뀜
 cf. commit한 시점에서 내려와야함, 커밋이 없는 상태여야함!!!
$ touch about.html 만듬
$ git add .
$ git commit - m ''
$ git log를 보면 맨 위의 commit에서 HEAD-> about-page인 것이 확인됨!!
commit에 (origin/master, origin/HEAD, master)라고 다 나옴!

$ git checkout master 로 가서 보면 about-page에서 한 것들이 없다고 나옴ㅠㅠ


다시 $ git checkout about-page로 와서 master와 연결해보자!!!
우선 git add 랑 commit하고
$ git diff master 로 마스터와 다른점 확인
$ git checkout master로 와서


마스터에서 복사본을 만들어 브랜치가 이어지는 것이라 마스터에는 변경사항이 없음
주가지는 마스터니까 마스터로 가서!!!
$ git checkout master
$ git merge about-page 로 머지함!!!

$ git log 해서 보면 HEAD-> master, about-page 로 나옴*
```



- conflict (충돌)

```
# 브랜치를 마스터와 합치려니 마스터에 변경사항이 있는 경우 (다른페이지는 고쳐주기도함..)

$ git checkout -b help-page 한번에 헬프페이지 만들고 이동할거야!
$ touch help.html 만들어서 내용넣고
$ git add .
$ git commit -m 'add help page' 하고
$ git checkout master 마스터로 가서 합침!
$ git merge help-page
$ git checkout help-page 헬프페이지 가서 문자 수정함
$ git add . 
$ git commit -m 'typo'
$ git checkout master 마스터에서 인덱스페이지 수정하고 헬프페이지 합침
$ git add .
$ git commit -m 'add a tag in index.html'
$ git merge help-page
Merge branch 'help-page'라는 vim 메시지뜸.. :wq해서 저장하고 나오면 저장되어있음!!

# 더 심한상황ㅠㅠ (같은페이지는 직접고치기)
$ git checkout -b final-check 만들어서 내용 넣고
$ git add .
$ git commit -m 'upper'
$ git checkout master 마스터로 와서 브랜치와 같은 페이지 같은 줄을 수정함!!
$ git add .
$ git commit -m 'lower'
$ git checkout final-check 브랜치에서 보니 마스터에서 수정했던 내용이 아니다!!!
$ git checkout master 머지는 마스터에서 할 수 있으니 마스터로 왔다!
$ git merge final-check 오류나서 어떤 변경내용으로 유지할지 선택하기!
$ git add .
$ git commit -m 'resolve conflict manually' 다시 커밋한다!
$ git push


```

- github은 브랜치 내용은 안가져옴 ->브랜치가 master밖에 확인안됨

```
#gitbub 에서는 브랜치가 확인 안된다ㅠㅠ

$ git checkout final-check 에서 README 링크를 만든다!
$ git add .
$ git commit -m 'add list README'
$ git push 브랜치에서 푸쉬 안된다!!!!
$ git push -u origin final-check 깃헙에 브랜치를 처음엔 이렇게 푸쉬한다.
깃헙에서 브랜치를 합칠 수 있다!
$ git checkout master 마스터에서 깃헙에서 브랜치 합친 것을
$ git pull 불러온다!
```