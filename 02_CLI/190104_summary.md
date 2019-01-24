# 190102 수업정리

1. git bash

cd TIL

cd 01_basic/

cd jupyter_notebooks/



pwd

ls



jupyter notebook =>주피터 시작!



alt + enter => 셀 실행 + 아래에 새 셀

shift + enter => 셀 실행 + 아래 새 셀만들어 이동

2. jupyter





3. Command Line Interface

운영체제 operating system = os 



탐색기/git bash/ 명령프롬프트(cmd) 켜고 함



-cmd

dir (= gitbash에서 ls와 동일)



-git bash (마치 유닉스인척..)

ls  -> 지금 내가 있는 위치에 있는 모든 것을 불러와라! 리스트

현재 위치의 폴더에서 목록보여줌

~ 는 내 위치를 의미, home directory

pwd -> 내위치

/ (내pc) /c (c드라이브) /Users /student

cd (=cd ~) => 홈으로 가기

cd .. => 한단계 위로 가기

cd . => 지금 내가 있는 곳

​	git add . => .의 의미는 지금 내 위치에 있는 애들 다 올릴거야!!!!!

cd - => 이전으로 가기

ls -a  -> (=ls --all) .붙은 애들이 나옴! 다 보여줘라!! .붙은 애들은 숨긴파일들도 나옴.

cd sth -> 특정 디렉토리로 이동. 폴더의 위치를 바꾼다(탐색기에서 더블클릭으로 폴더 들어간 것과 동일)

mkdir classroom -> classroom 이라는 폴더 만들어라

touch classmates.txt -> classmates라는 문서 만들어라

vim classmates.txt -> 내용 입력할 수 있음

​	:Q ->빠져나감 

​	:

touch a.txt b.txt c.py e.py ->폴더 한번에 만들어짐



-c9

$ : 프롬프트. 지금 입력을 받아들일 준비가 되어있다!

^ :캐럿sign = ctrl 

echo = print('')

man echo = echo에 대한 설명나옴. man = manual. 빠져나오려면 q, 검색하려면 /(검색할것)

^p = 이전 명령어

^c = 작업 취소

clear = ^l 화면을 위로 올리기 

^d = 터미널 끄기, 파이썬 상태에서 빠져나감



echo "When I was .." > black_parade.txt -> black_parade라는 텍스트 파일 만듬 

"내용" 을 >..파일에 써!!

`>`  redirect 앞의 내용이 뭐든 덮어씌움

`>>` 앞의 내용에 내용 추가

cat black_parade.txt = 파일에 있는 내용 출력해줌

touch .hidden => hidden이라는 숨김파일 만들어줌



ls -l  => 긴설명..

ls a => a파일 있나 알려줌

ls a* => a로 시작하는 파일 알려줌

-rw-r--r-- =>권한

ls -a -l (= ls -al)

ls -altr => all longformat  time reverse

ls -lh => 용량을 단위 변환해서 보여줌



mv => 이름바꾸기 mv reverse.txt rev.txt (reverse.txt를 rev.txt로 바꿈)



cp => 복사 cp rev.txt copy.txt => rev.txt 파일을 copy.txt라는 이름의 파일로 내용 복사함



rm =>지우기 rm .hidden => 지워! (윈도우에서 shift+del과 같음)

​	rm -i rev.txt => 진짜 지울거냐 물어봄 y누르면 지워짐

​	rm -f =>강제로 지우겠다!!!!!

​	rm *.txt => 텍스트파일 다 지워버린다!!!  

​	rm * => 걍 다 지워버린다!!!

​	rm a*=> a로 시작하는거 다 지워버린다!!!!

​	rm *a *=> 중간에 a들어간거 지워버린다!!!



which curl => curl 이 있는지 확인해줌 없으면 안나옴



curl -OL neovansoarer.github.io/files/sonnets.txt 

​	=> neovansoarer.github.io/files/sonnets.txt의 텍스트 파일 받아옴



curl -I https://eduyu.github.io => 

head sonnets.txt => 위에 열줄? 보여줌

tail sonnets.txt => 마지막 열줄 보여줌



wc sonnets.txt =>줄 단어 바이트(글자)수 나옴

head sonnets.txt | wc => 앞의 표준출력을 뒤에 적용!!! (| : 파이프)



less sonnets.txt => 뷰어

d : 페이지 다운 u : 페이지 업 /rose : rose검색 n :다음검색위치 shift+n: 이전검색위치



grep => 강력한!!검색!!!분석!!!! 

​	grep rose sonnets.txt => sonnets.txt에서 rose라는 단어를 찾겠다!

​	grep rose sonnets.txt | wc => 몇번 등장!?

​	grep -i  rose sonnets.txt | wc  => 대소문자 관련없이 검색!!!



ps aux => 지금 돌고있는 status가 나온다!!!



ps =>컴퓨터에서 제일 많이 잡아먹고 있는 것



ls / => 컴퓨터의 최상단에 있는 디렉토리들. 반드시 있어야 하는 애들.  컴퓨터에서 허용권한 만들어놓음

sudo --명령문---=> 어명이오!! 다 할 수 있음. 허용권한 있어야 한다는 것들도 강제할 수 있음



mkdir a => a라는 디렉토리 만듬

rmdir (=rm -r) a => a라는 디렉토리 지움. 안에 뭐가 있음 안지워줌ㅠㅠ

​	=> rm -r a/

​	rm -rf a/ =>강압적으로 파일이든 폴더든 다지움!!!

​	sudo rm -rf / ...절대 하지 말아야하는 말......









ps aux | prep jupyter

kill -9 (3080: 검색시 나오는 첫번째 숫자) 하면 주피터 강제종료 가능





크롬 - ^t 새탭 ^l 주소창 ^w 탭끄기 ^shift + t 꺼진 탭 살리기