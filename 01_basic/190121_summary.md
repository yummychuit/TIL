# 190121 수업정리

### 1. PYTHON 시험...



### 2. HTML_CSS

- box

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {
            margin: 0;
        }
        .parent {
            width: 150px;
            height: 150px;
            background: aqua;
            border: 1px solid black;
        }
        .static-box {
            position: static;
            background: darkblue;
            color: deepskyblue;
            font-weight: bold;
            text-align: center;
            line-height: 150px;
        }
    </style>
</head>
<body>
    <div class="parent">
        <div class="static-box">
            static-box
        </div>
    </div>
</body>
</html>
```



```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {
            margin: 0;
        }
        .parent {
            width: 150px;
            height: 150px;
            background: aqua;
            border: 1px solid black;
            margin: 50px;
        }
        .relative-box {
            position: relative;
            top: 50px;
            left: 50px;
            background: darkblue;
            color: deepskyblue;
            font-weight: bold;
            text-align: center;
            line-height: 150px;
        }
    </style>
</head>
<body>
    <div class="parent">
        <div class="relative-box">
            relative-box
        </div>
    </div>
</body>
</html>
```



- static과 relative의 차이

relative를 받았을 때만 쓸 수 있는 애들이 있다!

=>상대값으로 좌표값을 주어 밀어낼 수 있다.





```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {
            margin: 0;
        }
        .parent {
            width: 200px;
            height: 200px;
            background: aqua;
            border: 1px solid black;
            margin: 50px 0 0 300px;
            position: relative;
        }
        .absolute-box {
            position: absolute;
            height: 200px;
            width: 200px;
            top: 50px;
            left: 50px;
            background: darkblue;
            color: deepskyblue;
            font-weight: bold;
            text-align: center;
            line-height: 150px;
        }
    </style>
</head>
<body>
    <div class="parent">
        <div class="absolute-box">
            absolute-box
        </div>
    </div>
    <div class="absolute-box">
        absolute box no parent
    </div>
</body>
</html>
```



- 부모는 body

 absolute는 부모를 가림ㅠㅠ

부모가 static만 아니면 => 부모 기준으로 바뀜

부모와 조상 중에 static이 있으면 탈선.. 마이웨이 => parent가 영향을 주지 못한다

절대값에 자리를 잡게 된다. => body에 자리잡음



- static_relative_absolute.html

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {
            margin: 0;
        }
        .parent {
            width: 150px;
            height: 150px;
            background: gold;
            border: 1px solid black;
            margin: 50px;
            /* position: relative; */
        }
        .relative-box { 
            position: relative;
            top: 10px;
            left: 10px;
            width: 150px;
            height: 150px;
            background: orangered;
            color: orange;
            font-weight: bold;
            text-align: center;
            line-height: 150px;
        }
        .absolute-box {
            position: absolute;
            height: 150px;
            width: 150px;
            top: 10px;
            left: 10px;
            background: darkblue;
            color: deepskyblue;
            font-weight: bold;
            text-align: center;
            line-height: 150px;
        }
    </style>
</head>
<body>
    <div class="parent">
        <div class="absolute-box">
            absolute box
        </div>
    </div>
    <div class="parent">
        <div class="relative-box">
            relative box
        </div>
    </div>
</body>
</html>
```





- fixed.html

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {
            margin: 0;
        }
        .fixed-box {
            position: fixed;
            color: olive;
            font-weight: bold;
            text-align: center;
            background: black;
        }
        .sidebar {
            width: 50px;
            height: 100%;
            top: 0;
            right: 0;
            padding-top: 100px;
        }
        .footer {
            /* width: 200px; */
            width: 100%
            height: 50px;
            bottom: 0;
            left: 0;
            line-height: 50px;
        }
        .big-content {
            height: 2000px;
            background: cadetblue;
        }
    </style>
</head>
<body>
    <div class="fixed-box sidebar">
        fixed box side bar
    </div>
    <div class="fixed-box footer">
        fixed box footer
    </div>
    <div class="big-content">
        bigbigbigbigbig
    </div>
</body>
</html>
```

- 말그대로 고정!!!



z index가 정수가 클수록 앞으로 나옴.

맨 앞으로!!?





- 

image는 inline!! 

div는 block이라 가질 수 있는 공간을 최대한으로 가지려함!

=> 정렬하기 어려움ㅠㅠ

img에 margin을 준다!!



transition: all 2s;

아래에 있는 것 모두 다 2초에 걸쳐서 변경시킬거야!!!!





- 

```html
<body>
    <div class="container">
        <div class="row">
            <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">01</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">02</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">03</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">04</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">05</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">06</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">07</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">08</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">09</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">10</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">11</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2">12</div>
        </div>
    </div>
</body>
```

- grid system (break system)

  기본조건 : div.row안에 들어가있어야함

container 클래스에서 row를 12개!

가로6칸씩 2줄 총12칸

col-12는 모바일 화면일때 12픽셀을 한칸으로 하겠다!

xl화면에서 2칸을 먹겠다!

lg-3 => 화면이 작아지면 3*4로 배열

어떤 디바이스로 볼지 모르기때문에 사전정의를 하는 것.

하나의 마크업에 모든 디바이스 지원가능!!!







workshop

아래는 떨어져있는걸보니 container안에 있는듯

위의 바는 아닌듯



col-md-4

미디움보다 큰 사이즈는 다 4칸을 먹겠다!



### 3.

c9에서 django 로 새로 만듬

버전정보 X.Y.Z => semver(Semantic Versioning)

버전을 올릴 때 의미있게 올리자!

=> Major.Minor.Patch

Major: 많은 것이 바뀌었으므로 기존처럼 사용하기 어려울 수 있다. 새로 코드를 짜야한다!

Minor: 기능의 추가나 삭제가 있지만 기존 코드를 부수진 않는다.

Patch: 버그 픽스

버저닝은 개발자 배포자가 하는 것.



여러 버전을 깔아놓고 관리하는 것이 필요.

관리자 => pyenv

파이썬 버전관리를 하려고 합니다!







