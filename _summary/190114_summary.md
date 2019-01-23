# 190114 수업정리

## 1. hangman & pokemon 발표

- hangman

try, except

re 식을 만족 하느냐 안하느냐? 폰번호, 주소 등을 받을 때 주로 사용

- pokemon



## 2. 복습 

- 01_Python_intro

정식 명칭 단어들에 대해 어느정도 봐야함 (식별자, 시퀀스, 등)

식별자 => 이름. 우리가 만들어놓은 이름. 쓸 수 없는 것들 알아두기

인코딩선언은 외울필요는 없으나 손에 익혀놓는 것이 코드칠때 편리

주석은 기계는 못읽고 사람이 읽으라고 써놓은 것.

docstring -> `print(ss3.__doc__)`로 내용확인가능

`print("""
말하는대로,
쓰는대로, 
다 써져요!
""")` 주석처럼 쓰지만  print도 가능

코드라인 -> 세미콜론 없다. 가능은 하나 거의 안쓴다.

여러줄 쓸때는 \역슬래쉬 사용. 리스트, 딕셔너리, 셋, 튜플 안에서는 엔터쳐도 잘 됨

변수에 담겨있는 것이 할당된다고 하는데 리스트, 딕셔너리, 셋, 튜플 등의 경우에는 위치를 저장하는 것=> 메모리 주소id()

int 256까진 저장되어있는 고정값, 나머지는 주소가 고정되지 않은 값

수치형 (int, float) 오퍼플로우가 없다. 정수가 엄청 큰 정수도 다 담을 수 있다.

n진수, 다양한 진수의 숫자들을 사용하고있다.

실수에서 부동소수점 사용 -> 우리 의도와는 다르게 오류가 발생할 수 있다.

컴퓨터 연산이 2진수를 통해 숫자를 표현하는 과정이기 때문에 생기는 오류

`import math
math.isclose(a, b) ` 주로 이 방법을 사용

복소수 -> 허수 j가 붙어있으면 제곱했을 때 -값이 나온다.

`a.imag` 괄호가 없다!! -> class complex 에서 하나의 인스턴스 생성한것!?

bool -> `0, 0.0, (), [], {}, '', None `는 다 False. 없는것!!

None 정말 안에 아무것도 없다. 리턴문 없는 함수는 None이 나옴

이스케이프 문자열 ->

 `%-formatting`  [`str.format()`](https://pyformat.info/)  [`f-strings`](https://www.python.org/dev/peps/pep-0498/) 다 기억하기!!!

.format을 알고 있고 3.6이상에서만 사용가능하기 때문에  f-strings 주로 사용

산술연산자, 비교연산자, 논리연산자, 복합연산자, (+는 숫자뿐 아니라 문자열이나 리스트 등 다른 식에 사용가능하기 때문에 Concatenation으로) 기타연산자로 나눠져있음. 슬라이싱, 다 기억하기!!!

연산자 우선순위 기억하기

기초 형변환 (typecasting)  if 0 => 0이 자동으로  false로 인식되는..

정수랑 실수를 더라하고 했더니 실수로 결과가 나오는..

시퀀스 => 통일성은 중요하지 않음. 하나 이상의 것이 나열되어 있으면 시퀀스, 보통 인덱스 접근 가능(range말고..) 어떤 것들이 시퀀스인지 알아두기

string도 시퀀스. apple가 한 단어가 아니라 a, p, p, l, e로 나열되어 있는것.

튜플 -> immutable 수정불가능!

시퀀스에서 활용할 수 있는 연산자/ 함수 중요!!! 적어도 어떻게 동작하는지 알아둘것!!!

set, dict => 시퀀스 자료형 아님.  순서 없음. 집합에서 쓰는 연산들 -차집합(산술연산은 아님), 인덱스 접근 안됨

데이터타입 정리표!!!!!!

immutable - 변할 수 없는! 

mutable - 변할 수 있는!



- 02_Control_of_flow

if 조건문 if , elif, else  T/F의 결과로 나오는 것

fizzbuzz문제 - 15번 조건이 먼저 나와야 하는 이유 납득하기!

조건표현식 - 복잡한 식에서는 적합하지 않음, 정말 짧게 쓸때만(정수인지 음수인지 등) 함수의 return이라고 생각하면 좀 더 사용하고 이해하기 쉬움, 코드 사용법 기억

if else만 가능

반복문

while T이면 계속 실행 F면 멈춤 break로도 멈춤

언제 끝날지 모르는데 조건 만족하면 끝낼거야 -> while문 사용

for문 시퀀스가 아닌 애들도 돌아요! 알아서 처음부터 끝까지 돌고 끝나 while문보다 안전.  시퀀스가 무한하지 않으시 어쨌든 시작하면 끝남

`enumerate()` 활용. 인덱스를 꺼내쓰는 것이므로 언제 써야할지..인덱스 접근이 가능한 것들만 사용할 수 있다는 것을 기억하기!!!  set은 순서가 없으니 굳이 사용을..

dict는 key, value 접근 가능. `dict.keys()` `dict.values()` ` dict.items()`

for문은 끝이 있지만 중간에 멈추고 싶을 때, 더이상 볼 필요없을때 break건다

continue 뒤에 있는 애는 안함. 생략하고 다음회차로 넘어감

else 중간에 break를 걸지 않은 이상 끝을 봤을 때 마지막에 실행되는 것.

problem set은 보기!



- 03_Function

특정 코드가 반복이 된다면 묶어서 함수로 만든다!!

함수에서 print는 디버깅용. 끝은 return으로 끝나야한다!!!!

`return` 값이 없으면, None을 반환합니다.

built-in functions -> `dir(__builtins__)`로 확인가능

함수는 return값이 있을 수 있으며 뭐든 다 객체이기 때문에 그 객체로 반환될 수 있다. 리스트 -> 리스트, 문자열 -> 문자열

but 튜플은 불가!!  ,를 하면 자동으로 튜플로 되어버림

기본값 설정, 기본값이 없으면 아무것도 입력하지 않았을때 오류남

()에 순서에 상관없이 변수 넣어줄 수 있음

가변인자 *args 몇개가 들어올지 모르는데 튜플로 묶어버림

`**kwargs` `(**ddggg)`라고도 쓸 수 있음.**앞에 두개 쓰면 됨. 몇개가 들어올지 모르는데 하나로 잡혀 dict로 자동변환됨

이름공간(name space) 식별하는 것? 맥락. 공간마다 지칭되는 이름이 달라진다! ?

그 공간안에서 만큼은 유니크해야함 하나의 객체를 가리켜야 하기때문?

순서가 LEGB



## 3. 기본 Web

https://gist.github.com/eduyu 에서  raw - ctrl+s 로 저장 (jupyter notebook 내용복사해오기)



#### <기본웹의 구성!!>

- Web Service

Web service 를 만든다!

Web Service?? Web + Service!!

Web -> 거미줄? 월드와이드웹은 인터넷에 연결된 / 컴퓨터들을 통해 / 사람들이 정보를 공유할 수 있는 전 세계적인 정.보.공.간.!! => 공간!!

Service -> 용역? 쓰앵님이 크게 두 가지로 나눠보았다! 

1) 주세요!! 있으면 네!! 하고 건네 줌 => 내놔!!! (GET)

2) 처리해주세요!! 받은 사람이 처리하고 네!! => 처리해줘!! 받아라!! (POST)

고객(요청하는 사람) -> 요청 ____ 응답 <- 해주는 사람

=> 클라이언트(client) -> 요청(request) ___ 응답(response) <- 서버 컴퓨터(server)

우리가 만드려고 하는 것은 서버컴퓨터!!!



브라우저(browser) 익스플로러 / 크롬/.. 크롬사용할거야!!

user ---(computer)---> request ___ response <---(server)--- program

우리가 할 것은 요청을 받아서 응답을 보내는 것 까지 하는 프로그램!!

-> Web service를 만들겠다

''우리는 앞으로 2월까지 서버컴퓨터에서 요청과응답을 처리할 프로그램을 개발한다.''



- 개발 환경 준비 -지금 상태로는 개발을 할 수 없어ㅠㅠ

1. 근본적으로 소프트웨어 환경이 다르다.

   하드웨어 (물리적 컴퓨터) / 소프트웨어 (프로그램/도구)

   그렇다면 sw만 설치하고 내 pc를 서버컴퓨터로 사용하면 되지 않나요?



2. 물리적 컴퓨터도 다르다!!

개인pc

1) 개인pc 는 나에게 필요한 프로그램들이 깔려있다.

2) 내가 쓰는 용도에 맞는 성능을 가진다.

3) 보안에 있어 공격대상이 될 확률이 낮다.

4) 꺼지기도 한다.

서버컴퓨터

1) 서버 역할을 위해 필요한 프로그램만 깔려있다.

2) 클라이언트 사용량에 맞는 성능을 가진다.

3) 보안에 있어 공격대상이 되기 쉽다.

4) 절대 꺼지지도, 인터넷 연결이 끊겨서는 안된다.



그러면 어떻게 해???

내 컴퓨터에 서버에서 사용하는 프로그램을 설치하여 프로그래밍을 개발하고 program&code를 서버로 보낸다.

서버로 코드를 보낼때 github이 가장 많이 쓰이는 방법

실제로도 그렇게 배포를 함



새컴퓨터

어떻게 서버컴퓨터를 조작할 것인가!?

예전엔 직접가서 접속해서 썼었음 -> remote control



- HTML - 이게 뭔데 우리가 배우고 있죠?

1. Hyper Text Markup Language

Hyper Text => 

기존엔 책을 우선 먼저 펼쳐야하고 순서대로 해야함

하이퍼텍스트는 각자 하나의 문서고 길이도 제한이 없어 제각각임 순서없이 원하는 대로 갈 수 있음! 하이퍼링크를 통해 자유롭게 이동이 가능. 기존의 텍스트를 초월했다!  

Hyper Text를 주고받는 규칙?! transfer protocol => HTTP(S) 규약을 맞추겠다는 일종의 선언. (s)는 보안을 강화했다는 으미



Markup=>

글자들이 갖고 있는 역할의 선언, 각 텍스트의 역할을 지정해놓은 것 

큰제목- 내용, 작은 제목 - 내용, 내용, 작은 제목- 내용 => 역할이 뭔지 표시한것



Language=> 프로그래밍 언어는 아니지만(if , for문 없음) 언어...



HTML파일 : HTML로 작성된 문서파일. 확장자가 .html이 아니라도 HMTL일 수 있음



user와 서버가 주고받는 것은 html로 작성된 문서 단 하나!!!



2. CSS

C S S

띄어쓰기 간격, 글자색, 정렬 등

내용에 차이는 없지만 눈에 보이는게 달라지도록 만들어주는 것



w3c에서 html관련 표준을 관리함. 가장 최근 것이 html5



- static web -가장 단순한 웹서비스

아무것도 없는 컴퓨터에 하나만 설치해야 한다면?! 크롬!!!

파일도 열 수 있다!

/dir1/dir2/../wantthis.file

내컴퓨터 최상단!

남의 컴퓨터 주소/ dir1/.../file 하면 해킹이 되는것!!

어디에 있는지 정확히 알아서 찾아야함. 아무도 찾아주지 않음.

정확하게 지정을 해야함.

html은 / 뒤에 아무것도 안써줘도 index페이지가 알아서 나옴. ->http의 약속임



- Dynamic Web -Web application program

http://hphk/lectures/1

마지막 /1은 파일이름이 1인걸까?? -> 말이안됨!! 사서가 1의 내용을 꺼내어 html파일과 합쳐서 갖다주는것임!!

.html이면 static web일 확률이 높고 요즘 대부분은 dynamic web임

사서같은 존재 -> 컨트롤러 

서버 컴퓨터에 달라고 하는 방법은?! 단하나 URI뿐!!! 주소창에 입력하는 것뿐!!

(uniform resource locator)

네트워트상에서 자원이 어디에 있는지 알려주기 위한 고유의 규약



주소창에 요청사항을 입력하면 get a html에서 get!!



# 4. HTML

https://validator.w3.org/ 에서 error와 warning 알려줌



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>yummychuit's github page</title>
</head>
<body>
    <h1>Comming Soon...</h1>
</body>
</html>
```

!DOCTYPE 이 문서는 html입니다! 선언!!

```html
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>yummychuit's github page</title>
</head>

<body>

    <h1>Comming Soon...</h1>

</body>
</html> 
```

트리구조 - 최상단으로부터 시작하는 부모-자식관계로 되어있는 구조

html 문서를 구성하고 있는 요소

```<html lang="ko">``` 

head 는 페이지에 대한 정보를 담고있음. 이 문서가 어떻게 보였으면 좋겠다~

body 안의 내용이 사람들에게 보여지는 내용

h1 테그

dom트리 document object model 브라우저에 랜더되는 화면이라고 하면 이해하기 쉬움

하나의 테그들이 object가 됨

어떤테그는 혼자 열리고 닫히는 것들이 있지만 기본적으로 여는 테그 - 내용 - 닫는테그

테그 + 내용 == 엘리먼트

img  src="" / => 혼자 열리고 혼자 닫힘

attribute속성 테그가 끝나기 전에 ㅇㅇㅇ= 이거다! 라고 값이 붙는 것들

img src="animals/cat1.jpg" alt="first cat" / => src, alt도 어트리뷰트가 붙은 것

속성명은 따옴표가 반드시 없고 속성값은 무조건 따옴표 안에 있음.

<li>HTML</li>

이 엘리먼트는 li테그로 되어있고 콘텐츠는 HTML

body테그가 h1의 부모고 h1과 ul은 시블링(형제)관계에 있습니다.

```html
<header></header>
<nav></nav>
<aside></aside>
<section>
    <article></article>
    <article></article>
</section>
<footer></footer>
```

기존의 <div>로 되어있는 것을 굳이 이렇게 나누어 쓸까?

시멘틱 마크업!

시멘틱 테그들



#### chrome Web Developer설치하기

information - view document outline으로 보기



h1 만큼은 하나의 가장 중요한 제목이기 때문에 한 번만 쓸 것.

(글씨크기를 크게 하기 위해 h1 사용은 지양....쓰면 안돼요!!)



paragraph -> p 본문에 해당하는 내용

b ->굵게할래

strong -> 강하게 할래!! 이게 역할이니깐 b 말고 strong을 쓰자!

i -> 이탤릭 기울임

em -> 강조! 기울임!! 의미론적으로 em을 쓰자!!



blockquote -> 인용구







- table만들기





- link 만들기





```
안보고 쓸 수 있을정도로? 대소문자? 퀴즈내기 딱좋음..
<!DOCTYPE html>
```

hyper reference = href



