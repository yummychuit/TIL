# Movie Recommender System

## - Web Project

WEB 프론트엔드에 대한 이해를 위해 반응형 웹 페이지로 영화 추천 사이트를 구현합니다.

HTML를 통한 웹 페이지 마크업 및 레이아웃 구성, CSS를 통한 선택자 활용 및 웹 페이지 꾸미기, Bootstrap을 이용한 HTML/CSS, JS Component를 활용합니다.

## 준비사항

1. HTML/CSS, Bootstrap 환경 구성

  - Text Editor
  - Bootstrap v.4.2.1

2. 웹 페이지를 위한 Assets 다운로드

  - https://zzu.li/02_web
    - assets 폴더 (활용할 이미지)
    - data (입력해야 할 내용)
    - 예시이미지 (결과물 이미지)

3. (선택 활용) 

   - https://fontawesome.com/ font-awesome

     font-awesome 은 웹 개발과정에서 많이 활용되는 아이콘들을 css 혹은 svg 형태로 제공 해줍니다.

   - https://fonts.google.com/ google font

## 작동 방법

HTML/CSS와 Bootstrap을 활용하여 목표로 하는 반응형 웹사이트를 구성합니다.

### 1. 영화 추천 사이트를 위한 레이아웃 구성_1

- 영화 추천 사이트 메인 페이지 기초 레이아웃을 구성합니다.

  - HTML 기초 - 기본 설정
    - DOCTYPE 은 html입니다.
    - html 의 언어는 한국어(ko)입니다.
    - meta 태그에 인코딩 설정을 UTF-8로 설정합니다.
    - meta 태그에 기본 viewport 설정을 합니다. (width: device-width, initialscale: 1.0)

  - Navigation Bar
    - 최상단에 위치하는 Sticky navigation bar로 구성됩니다.
    - Item List(예시 - Home/친구평점보러가기/Login)는 우측 정렬입니다.
    - 반응형으로 구성되어 일정 수준 이하에서는 item이 숨김 처리 됩니다.
    - Item List에서 Home을 제외한 것들은 아직 기능이 구현되어 있지 않으므로 클릭이 불가능(disable)합니다.
  - Header
    - Navigation Bar 바로 아래에 위치합니다.
    - 높이는 350px , 너비는 브라우저 전체 영역입니다.
    - 반드시 css 속성 background-* 를 활용한 배경 이미지가 있어야 합니다.
    - Header 영역의 수직/수평 가운데 정렬 위치에 h2 태그를 사용하여 작성합니다.
  - Footer
    - 브라우저 최하단에 위치합니다. (Sticky와 내용 최하단 중 선택)
    - 높이는 50px 이상, 너비는 브라우저 전체 영역입니다.
    - 왼쪽에는 본인의 이름 혹은 닉네임, 오른쪽에는 헤더로 올라가는 링크로 구성됩니다.
    - Footer는 padding이 좌우로 3rem입니다.

  - Font 설정
    - 서로 다른 폰트를 2개 이상 활용합니다.

기본적인 설정을 위해 처음에 DOCTYPE과 언어설정을 한 뒤, head tag 안에 meta tag로 인코딩 설정과 viewport설정을 해줍니다. 그리고 HTML과 CSS, Bootstrap, Font 등을 연결하기 위해 head tag안에 링크를 입력해줍니다. 

웹페이지의 기본 구성을 이루는 것들을 만들기 위해 Navigation bar와 Header, Footer를 만듭니다.  navigation bar는 Bootstrap을 이용하였고 header와 footer는 HTML과 CSS를 이용하였으며, Bootstrap 명령어와 CSS 사용하여 디자인을 설정하었습니다.

### 2. 영화 추천 사이트를 위한 영화 리스트 구성_2

- 영화 목록 섹션 레이아웃을 만듭니다.
  - 레이아웃
    - 영화 리스트는 container에 속합니다.
  - subtitle
    - subtitle 영역은 위 아래 margin이 3rem입니다.
    - 글씨 부분은 h3 태그입니다.
    - 밑줄은 너비가 70px이고, 색상은 자유입니다.
  - Card view
    - 카드 총 6개 이상이며, 반응형으로 배치해야 합니다. 한 줄에 보이는 카드의 갯수는 다음
      과 같이 구성됩니다.
      576px 미만 : 1개
      576px 이상 768px 미만 : 2개
      768px 이상 992px 미만 : 3개
      992px 이상 : 4개
    - 카드는 각각 위 아래 margin이 1rem입니다.
    - 이미지는 제공된 이미지를 활용 해야하며, 반드시 alt 속성에 값이 있어야 합니다.
    - 이미지 밑에는 h4 태그를 활용하여 영화 제목을 작성 해주세요.
    - 영화 제목 옆에는 네이버 영화 평점을 작성 해주세요.
      영화 평점은 9점 이상인 경우 청색 계열의 색으로, 9점 미만인 경우는 어두운 계열
      의 색으로 꾸며 주세요.
    - 제목 및 평점과 내용에는 구분선이 있습니다.
    - 구분선 아래에는 영화 장르와 개봉일을 작성 해주세요.
    - 가장 아래에는 네이버 영화 상세 정보 링크를 만들어 주세요. 링크는 반드시 새 창에서 열려야 합니다.

위에서 만들어놓은 기본적인 구성에 본문 내용을 추가합니다. header아래로 내용이 나와야하기 때문에 위의 margin 400px을 주었습니다. 그리고 반응형 웹페이지에 맞게 화면의 사이즈에 따라 카드의 수가 다르게 보일 수 있도록 division의 class를 col-12 col-sm-6 col-md-4 col-lg-3으로 지정하였습니다.  카드에서는 기본적으로 영화 포스터와 영화명, 영화 평점, 장르, 개봉일이 확인됩니다.

### 3. 영화 상세보기

- 영화 상세보기 레이아웃을 만듭니다.

  - Modal 이미지를 클릭하면, 영화에 대한 상세 정보와 추가 이미지를 보여 주도록 구성합니다.

    - ```html
      <!-- Modal은 클릭 대상에 다음과 같이 설정 되어야합니다.
      data-target : modal의 id
      data-toggle : modal
      -->
      <img data-target="#movie-1-modal" data-toggle="modal">
      <!-- Modal -->
      <div id="movie-1-modal" class="modal fade" >
       <!-- Modal 내용 -->
      </div>
      ```

    - Modal의 상단( .modal-header .modal-title )에는 영화의 한글명과 영문명을 같이
      작성합니다.

    - Modal의 헤더(.modal-header)와 내용(.modal-body) 사이에 이미지를 삽입합니다.
      이미지 대신 carousel로 구성할 수 있습니다.

본문 내용에서 상세보기 버튼을 클릭하면 나오는 상세 내용을 입력해줍니다. 위에서 만들었던 영화정보 보러가기 버튼을 modal이미지로 하였고 클릭하면 영화 스틸컷 3장이 carousel로 돌아가며 볼 수 있게 나옵니다.  그 아래엔 관람등급과 누적관객수, 영화에 대한 설명, 그리고 Naver Movie의 해당 영화 페이지로 갈 수 있는 버튼과 닫기 버튼으로 구성되어 있습니다. 

### 4. 추가

- 파비콘을 삽입합니다.

  - ```html
    <!-- href 경로는 꼭 확인하세요! -->
    <link rel="icon" type="image/png" sizes="96x96" href="assets/favicon96x96.png">
    ```

    파비콘(Favicon) : 인터넷 웹 브라우저 주소창 혹은 탭에 표시되는 웹 페이지를 대표하는 아이콘 입니다. (png 는 익스플로러 11버전 이상에서만 표현됩니다. 일반적으로 .ico 확장자를 사용하지만 픽셀 때문에 png를 사용합니다.)

완성된 기본 페이지에 href 경로를 입력하여 파비콘을 삽입하면 Title 제목 왼쪽에 아이콘이 생긴 것을 확인할 수 있습니다.

## 결과 파일

```
02_web/
		README.md
		01_layout.html
		01_layout.css
		02_movie.html
		02_movie.css
		03_detail_view.html
		03_detail_view.css
		assets/
			*.jpg
```

