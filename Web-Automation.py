import webbrowser as wb


def webauto():
    chrome_path = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
    URLS = (
            'youtube.com',
            'gmail.com',
            'github.com'
    )
    for URL in URLS:
        print('Opening : ',URL)
        wb.get(chrome_path).open(URL)


webauto()