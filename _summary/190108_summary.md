# 190108 수업정리

### 1.  

- git bash에서

less .bash_history 히스토리 확인



줄임말 쓰고 싶을때

touch .bashrc 

vim .bashrc 

i 누르고 입력

alias 'jn'='jupyter notebook'

:w 저장

:q 빠져나가기

cat .bashrc 로 확인

bash => 새로고침? bash가 잠깐 껐다켜짐

이제 jn으로 주피터 노트북 켜짐!!



### 2. problems



### 3. Git -c9

VCS(version control system)버전관리 시스템



pwd => 현재 내 위치

ls 

rm README.md => README.md 삭제



git init => 자리 확인 하기!! git을 쓰겠다! 숨김 디렉토리인 .git 생김

(ls -a로 확인 가능)

repository => (master)생김

rm -rf .git 으로 지울 수 있음



which git => git이 있는지 확인!



c9은 자동으로 설정해주는 기능이 있음. 계정정보가 써져있음

다시 홈으로 돌아와서(cd)

cat .git  + tap키를 두번 누름!

cat .gitconfig = > git에 대한 설정을 바꾸는 것 

​	cat .gitconfig 에서 커서를 움직여 editor의 nano 에 가서 a누르고 지운뒤 vim으로 바꿔줌

​	esc를 막 누르고 :w (저장) :q (빠져나가기)



git help => 명령어 설명나옴

git status => 지금 리포의 상태에 변화있는지 확인! (뭐가 변한거 같은데..)

​			빨간글씨로 나옴(commit준비가 안됐다!!)

git add 파일명.txt =>  변화가 있는 것을 확인!! (여기보세요!) untracked->staged로 변함 초록글씨됨

git commit -m ' 남길 메시지 내용' => (찰칵!)  

untracked & unstaged -> staged ->

​					git add		git commit	



git log =>노란글씨가 우리가 만든 버젼 이름. 



git message tip!

1. 현재형으로
2. 명령하듯이
3. 너무 길지 않게
4. 더 자세한 사항은 "Shiny new commit style"참조



===>>> 내용들을 컴퓨터에 쌓임!!! 처음에 저장을 해놓으면 변경사항을 추가해나가는 것. (형상관리?)

​	 c9삭제하면 다 날라감ㅠㅠ -> cloud에 백업하자!! 

​	git != github



github에서 새로운 repo를 만든다! 바로 뜨는 설명서에서 아래 내용을 복사해서 붙여넣기한다

```
git remote add origin https://github.com/yummychuit/learn_git_prj.git
```

(cat .git/config에서 확인 가능) =>github을 찾아서 손가락질했다!!

다음줄도 복붙 (git push 받아라!!)

```
git push -u origin master
```

github username & password 입력하기 (최초에만 시행됨)(password는 안나오니 알아서 잘쓰길..)



### 자료를 가져오자!!!

github에서 clone or download -  주소 복사 - 다른 컴퓨터의 gitbash의 홈(~)에서 

(download ZIP은 git 없이 자료만 다운하는 것)

git clone ( https://github.com/yummychuit/learn_git_prj.git  :복사 주소) (ssafy_git : 이름)

cd ssafy_git 하면 master로 되어있는 것 확인 가능

code . =>vscode로 현재 위치에 있는 것 다 뜸



다른 컴퓨터에서 수정하고

git add . 

git commit -m 'blahblah'

git push



원래 컴퓨터에서 git pull 해서 받기



pull안받고 수정해서 push하면 오류남

다시 git pull하고 

vim 뜨면 esc 누르고 :wq 하기

그 후에 git push



github에서 직접 수정하는 것이 최악................ 지양하세요..........



### git commit 끝내고 바로 git push할것!! 수정한 내용이 있으면 push안됨!!!



교육장 도착!!

cd TIL

git pull



집가기 직전!!!!!!

cd TIL/

git add .

git commit

git push



집도착!!!

cd TIL/

git pull



잔다!!!!!

cd TIL/

git add .

git commit

git push

