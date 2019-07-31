import webbrowser, time, os
URL = 'https://www.google.co.uk/search?q=subscribe+to+pewdiepie'

def spam(loop):
    for x in range(0,loop):
        webbrowser.open(URL)
        time.sleep(0.5)

spam(8)
time.sleep(4)
os.system('taskkill /im chrome.exe')
time.sleep(2)
webbrowser.open("https://www.google.co.uk/")
