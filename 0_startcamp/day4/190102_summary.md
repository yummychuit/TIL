# 190102 수업정리

좌석표 시트  zzu.li/ss3_seat

## 1. SCRATCH

1. 깃발 누르면 움직임



2. 최대공약수&최소공배수

   클릭하면 첫번째숫자? 엔터치면 두번째 숫자??

   숫자 입력받아 최대공약수& 최소공배수 말해주는 것 만들기

https://scratch.mit.edu/projects/239809991/#editor



3. 주피터 설치
   선생님 github

   https://github.com/eduyu

   clone or download에서 주소 복사

git bash 실행 (-> python -i하면 파이썬 실행 but 코드 저장안해줘서 내용 날라감)

pip -V 파이썬 버전 확인

pip install jupyter 주피터 설치

cd TIL

cd 01_basic

 git clone https://github.com/eduyu/jupyter_notebooks.git

=>jupyter_notebooks라는 폴더 생김

cd jupyter_notebooks/

ls -a

rm -rf .git

ls -a

=> /../python101-students/라고 나옴 (.git 없앰)

jupyter notebook

=> 크롬에 주피터 노트북 켜짐

ctrl + c => 빠져나가서 주피터 노트북 꺼짐



cd til => (master)생겨야함

안생기면 git init 엔터!



echo '.ipynb_checkpoints/'>> .gitignore

git config --global core.autocrlf true





4. 주피터
   주피터에서 뉴 - 폴더 playground

뉴 - python3 -> first_notebook으로 rename



초록색 -> edit 모드 (esc누르면 파란색됨)

파란색 -> 명령모드 command 모드



하나하나의 박스  -> 셀

코드 수정하면 실행해줘야함. 셀단위로 실행됨.

crtl + enter => 실행 (파란색상태에서)



b -> 아래에 새 셀 생김

00 -> 위에 코드들 다 초기화 되어 내용이 있더라도 1번째 실행이 됨

h -> 단축키

dd -> 해당 셀 삭제

z -> 삭제한 셀 살리기



5.  추가 확장 프로그램 설치

http://localhost:8888/tree 

git bash 에서

pip install rise

jupyter-nbextension install rise --py --sys-prefix

bash

jupyter-nbextension enable rise --py --sys-prefix



6. python_intro



7. git add .

   git commit -m 'ss3 | python intro | ~190102'  

   => 어디서 어떤 것을 언제했는지로 저장해놓으면 좋음

   git push

