import webbrowser

keywords = ['초밥',
                '비빔밥']

for keyword in keywords:
    url = 'https://www.google.com/search?q=' + keyword + '맛집'
    webbrowser.open_new(url)
    