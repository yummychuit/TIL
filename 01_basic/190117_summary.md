# 190117 수업정리

## 1. CSS

tip

터미널에서 ctrl + w하면 띄어쓰기 단위로 지워짐

esc누르고 방향키하면 단어단위로 움직임

인덴팅 망했을때 alt + shift + f 하면 됨



한 뎁스 차이만 부모자식관계

그 이하는 그냥 하위요소 ,후손



pseudo => 의사코드. 가상이라는 의미

실제로 실행되는 코드는 아니지만 보면 알아..?

특정 상태에 따라 적용된다??

ex) 링크 위에 마우스를 올렸을 때!



margin-left => 왼쪽 벽을 밀어 오른쪽으로 밀리는 거라 생각하면 좋다. 왼쪽에 틈이 생기며 오른쪽으로 밀림



```
::selection {
            color : steelblue;
            background: palegoldenrod; 
        }
```

background 는 블록 선택했을때 색깔



```
/* http://meyerweb.com/eric/tools/css/reset/ 
   v2.0 | 20110126
   License: none (public domain)
*/

html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section {
	display: block;
}
body {
	line-height: 1;
}
ol, ul {
	list-style: none;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}
```

reset css라는 것이 존재함

이거 써넣으면 html 디폴트 값이 다 사라지고 기본으로 됨



위지위그!!!



*는 유니버셜의 의미 헤드도 포함

em => 상하좌우로 거리를 좀 벌릴게! 부모에서 곱셈

rem => 그냥



background는 padding + content한테 적용됨

padding: 10px 20px 30px 40px; 상우하좌 순으로 쓰기

2개쓰면 상하/ 좌우



hidden은 공간은 남아있고 content만 숨음

collapse는 다 숨음



- bootstrap

