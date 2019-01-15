# 190115 수업정리

## 1.복습 & 시험

- 04_recursive_function

  펙토리얼, 치킨쿠폰, 피보나치, 업다운, 스퀘어루트, 개미수열 안보고 풀 수 있을 정도...

  모르면 가져오세요ㅠㅠ

- 05_data_structure

cf) 01_Python_intro 데이터타입 정리

​	sequence(ordered) 특징 - 순서가 있어 인덱스 접근이 가능하다

​	unordered 특징 - 

​	mutable vs. immutable

​	mutable ->  원본이 바뀌는 애들

​	immutable -> 원본이 안바뀌는 애들



List Comprehension 꼭 자유자재로 코드 쓸 수 있도록!!

이중 for 문이 별로 안좋음. 메모리나 시간상 오래걸림. 2배정도 까지도 시가나이가 난다고 함

- OOP-intro

```python
class Mate: 
    classroom = 703 #mate의 공통정보
    ban = 3
    breath = True
    
    def __init__(self, name, github, blood, arrive):
        self.name = name
        self.blood = blood
        self.github = github
        self.arrive = arrive
        
    def get_info(self):
        print(f'안녕하세요! 제 이름은 {self.name}입니다.')
        print(f'제 혈액형은 {self.blood}형 입니다.')
    
    def dochak(self):
        print(f'{self.name}는 도착하면 {self.arrive}를 합니다.')
        
yu = Mate('유태영', 'eduyu', 'O', '화장실')
yu.dochak()
print(yu.ban, yu.classroom)

kim = Mate('김민주', 'yummychuit', 'A', '출석체크')
kim.dochak()
kim.get_info()
```

object 는 실존하는 것. 인스턴스가 실존하는거?ex) 703은 object

703은 int class의 instance다 (class 와 instance의 관계)

클래스 ==> 속성 -> data (ex) classroom, ban, breath 등 / 행위->method 들 (ex)  get_info(), dochak(), 등 ==> 정의만함

인스턴스 ==> 수행만함





## 2. HTML

emmit 검색해서 치트시트 참고하기



form은 양식. 제출하면 form 테그 안의 내용이 다 서버로 날라옴

`div` 는 영역 안에 따로 넣어주고 싶을때



 `<input type="text" name="name" autofocus>` 

autofocus는 새로고침해도 이 자리로 옴

value를 지정해주면 시작할때 입력되어 있는 값이 됨

radio는 하나만 선택할 수 있음

checkbox는 여러개 선택 가능



윈도우 팁!

ctrl + shift + 방향키 => 단어단위로 잡음

alt + 방향키 => 왔다갔다

ctrl + backspace => 단어단위로 지우기



## 3. CSS

selector가 중요!!

div 은 옆으로 늘어날 수 있을만큼 늘어남



CSS는 어떻게 보일지, 어디에 위치할지를 정하는 것!

컴퓨터의 입장에선 전혀 필요 없는 것...



어떤 선언, 자식요소가 어떤 부모요소의 내용을 받는지.. 우선순위가 존재함

head는 정보, 보여지는건  body

=>  CSS는 body를 다룸



우선순위가 덮어 씌여지는 경우가 많음

가까운 것이 우선!

1. 테그 옆에 바로 속성주는 것은 인라인 스타일링

좋지 않음!!!



2. head에 지정

양이 많지 않으면 나쁘진 않지만 양이 많아지면 body 테그에 가기전에 몇백줄이상 쌓일 수 있어 감당안됨



3. style sheet 만든다

`div { border: 1px solid black; }`

 border 는 속성

border: 1px solid black; 선언(디클러레이션)

div 테그의 모든 테두리를 저렇게 하겠다!!



 selector

모든 것이 다 테그안에 있을 수밖에 없기 때문에 정확하게 내가 원하는 특정 element를 뽑을 때 사용.



id

어떤 문서에서라도 id의 값이 같을 수 없음. 2번 등장할 수 없음

테그와 전혀 무관



class

요소 하나에 하나의 id만 사용한다. 숫자로 시작 못한다. 하이픈(-)으로 띄어쓰기 구분.

띄어쓰기로 class 구분 (bio a b c => bio a b c 각각의 클래스..)



네이밍!!

class id를 정할때 주의할 것

orange-link -> 보여지는 상태에 대해 이름을 지으면 안됨

.box -> 너무 포괄적임

=>의도가 무엇인지에 더 집중하여 설명하는 네이밍이 좋음

만약 .small로 이름을 지으면 얼마나 작은지...

-> .collapsed / .disabled 등



언제 id를 쓰고 언제 class를 쓸지?

id는 첫번째꺼만 적용됨 -> css에서 쓰지 않는게 옳다!

전부 class로 넘기는 것이 맞다!!

부트스트랩 - style.css 에 엄청 많은 스타일이 있는 것을 저장하는 것.

​	

CSS 명시도 -우선순위(강한순서)

!important 라는 것이 제일 강한 것!! 하나때문에 모든 것이 깨지니 있다는 것만 알고 절대로 쓰지 말것.. 쓰는 방법도 안알려줄거얌

inline  얘때문에 꼬일 수 있으니 쓰지 말것

미디어타입커리???

브라우저 디폴트를 수정한 값

id

class

더 나중에 정의된 것이 우선순위 -> 더 상세하게 정의하면 그것이 우선순위

부모한테 상속받은 것

style sheet에 작성된 것

브라우저 디폴트값



```html
/* Bad Example */
body div#exec-bio.bio-box {
    color: green;
}
```

굳이 안써도 될 내용을 써서........굳이 길게....... 할 필요 없음.

