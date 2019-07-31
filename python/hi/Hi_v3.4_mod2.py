import webbrowser, time, os
print("keep this window open on the other screen from chrome")
URL = 'https://www.google.co.uk/search?q=subscribe+to+pewdiepie'
MAX = 6

def spam(loop):
    for x in range(0,loop):
        webbrowser.open(URL)
        time.sleep(2)

while True:
    loop = input("enter number of tabs per loop: ")
    try:
        loop = int(loop)
        if loop > MAX: print("error: don't be stupid\n")
        else: break
    except: print("error: invalid input (enter a number)\n")

while True:
    spam(loop)
    time.sleep(loop)
    os.system('taskkill /im chrome.exe')
    time.sleep(60)
    print("Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.\n")
