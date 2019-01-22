# Bootstrap

### 1. 부트스트랩 필수 HTML 환경설정

```html
<!DOCTYPE html>
<html lang="en">  
...
</html>
```

-부트스트랩은 HTML버전중 HTML5버전 문서포맷을  공식 지원하기 때문에 반드시 모든 웹페이지 문서는 최상단에는  HTML5문서임을 선언하는 `<!DOCTYPE html>` 태그가 선언되어 있어야 하며 html태그로 시작하여 html태그로 종료되어야 합니다.

`<meta charset="UTF-8">`

-한글,중국어,일어와 같은  유니코드 문자 지원을 위해서는 문자타입을 반드시 utf-8로 선언합니다.

`<meta name="viewport" content="width=device-width, initial-scale=1,minimum-scale=1, maximum-scale=2, user-scalable=no">`

-부트스트랩 3.0 이상 버전에서는 모바일 환경이 기본 사용자 환경으로 인식될수 있게 하기 위해 반드시 메타태그의 viewport 기본 가로폭설정을 
동적으로 각각의 디바이스별 해상도 가로폭값으로 지정될수 있게 설정해야합니다.
-initial-scale : 초기 화면 축소/확대 비율을  설정할수 있으며 1은 100% 설정값입니다.
-minimum-scale : 최소 축소 비율을 제어하며 사용자가 너무 화면을  작게 줄이는것을 방지합니다.
-maximum-scale : 최대 확대 비율을 제어하며 사용자가 너무 화면을  크게 늘리는것을 방지합니다.
-user-scalable : 화면의 확대/축소 기능을 사용 할지 말지를 결정합니다.

**TIP)****뷰포트 메타태그에 대해**
뷰포트 메타태그는 애플측에서 사용했던  모바일 전용 해상도 설정 메타 태그로  현재는 표준에 가깝게 사용되고 있는 태그로  웹페이지의 뷰포트 설정을 하지 않으면  애플 태블릿 장치에서는 기본 뷰포트 사이즈가 980px으로 설정되기 때문에 전체 내용이 보여지기 위해  비율이 축소되 페이지가 작게 보이는 문제가 발생하므로  반드시  반응형으로 개발되는 웹페이지는 뷰포트 가로폭 설정값을 width=device-width로 지정해야합니다.
참고 링크 URL) <http://aboooks.tistory.com/352>



http://mixedcode.com/Article/Index?aidx=1071 보는중