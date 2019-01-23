# 190107 수업정리

### 1. 재귀 함수(recursive function)



-look and say

``` python
look 과  say를 따로 보자!

look

say = 0

for num in list:

	if num == look:

		say += 1

1. remain[0]을 본다.
2. remain[0]을 다른 숫자가 나올때까지 센다.
3. result에 t = (look, say)
4. remain에서 본 것은 버린다.
(반복)
remain이 비면 result를 remain으로 바꾼다.
n -=1하다 n == 0일때 remain을 return한다.

(반복)

```



### 2. data structure

1. 문자열 메소드 활용하기

메소드도 함수!

리턴값으로 받는다! (원본은 변하지 않는다.)

.greeting()  => 첫 글자만 대문자, 나머진 다 소문자로

.title() => 어포스트로피나 공백을 이후를 대문자로

.upper() => 모두 대문자

==>> type이 str





