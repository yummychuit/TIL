print('hi')
len('hi')
type('a')

scores = [45, 60, 78, 88]
higt_score = max(scores) #최대값
lowest_score = min(scores) #최소값 min([]), min(1,2) 최소 2개 이상의 숫자
round(1.8) #2
round(1.4) #1 =>반올림
round(1.876, 2) # 소숫점 둘째자리까지 반올림


first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

#full에 first 와 second 을 합쳐서 저장
full = first + second

#full_sorted에 full을 오름차순으로 정렬하여 저장
full_sorted = sorted(full)

#reverse_sorted 에 full을 내림차순으로 정렬하여 저장
reverse_sorted = sorted(full, reverse=True)

