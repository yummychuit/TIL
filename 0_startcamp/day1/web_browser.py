import webbrowser

keywords = [
    'bts', 
    'python', 
    'SSAFY'
]

for keyword in keywords:
    url = 'https://www.google.com/search?q=' + keyword
    webbrowser.open_new(url)



