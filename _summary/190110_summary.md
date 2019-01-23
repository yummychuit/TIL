# 190110 수업정리

## 1. Morning Quiz

### 1. Hangman

> 주어진 코드를 활용하여 `hangman(answer)`를 만들자! 
> 사용자가 답을 맞추거나 시도가 8번을 넘어가면 종료! (8번 가능, 9번째 죽음ㅠㅠ)

```python
#다 맞으면 True
def is_answer(answer, letters):
    answer = set(answer)
    count = 0
    for char in set(letters):
        if char in answer:
            count += 1
    return len(answer) == count
    
is_answer('apple', ['a', 'p', 'l']) #False
```

```python
# 맞힌 단어 표시
def status(answer, letters):
    for char in answer:
        if char not in letters:
            answer = answer.replace(char, '*')
    return answer
status('apple', ['a', 'p']) 
```

```python
#풀이
def hangman(answer):
    input_letters = []
    attempt = 8
    print('=====START=====')
    
    while 1:
        print("남은 목숨: " + '♥' * attempt)
        print(status(answer, input_letters))
        
        guess = input('알파벳을 입력하세요: ').lower()
        input_letters.append(guess)
        
        # + some code
        
        if is_answer(answer, input_letters):
            return '성공!!'
        else:
            attempt -= 1
        
        if not attempt:
            return '실패ㅜㅜ'
        
hangman('apple')           
```



### 2. OOP



