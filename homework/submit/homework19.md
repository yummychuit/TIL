1.
CSRF(Cross-site Request Forgery, 크로스사이트 요청 위조) 공격은 원클릭 공격, 사이드 재킹, 세션 라이딩 등으로도 알려져 있고, 약어로는 XSRF로도 알려져 있습니다. 이 공격은 사이트가 신뢰하는 사용자를 통해 공격자가 원하는 명령을 사이트로 전송하는 기법을 사용합니다. 공격이 사용자를 통해 이루어지기 때문에 공격자의 IP는 추적 불가능한 특성이 있습니다. 

2.
def create(request):
    input_title = request.POST.get('title')

    article = Article(title = input_title)
    article.save()
    return render(request, 'index.html')
    
3.
<form action="/posts/{{ post.id }}/update/" method="POST">
    {% csfr_token %}
    <input type="text" name="title" value={{ post.title }}/>
    <input type="text" name="content" value={{ post.content }}/>
    <input type="submit" name="Submit"/>
</form>