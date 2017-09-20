import urllib

def read_text():
    quotes = open("checker")
    text_inside = quotes.read()
    quotes.close()
    check_curse(text_inside)


def check_curse(text_to_scan):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_scan)
    response = connection.read()
    connection.close()
    if "true" in response:
        print("Curse word alert!\t Curse word alert!")
    elif "false" in response:
        print("good to go, the document does not contain curse word")
    else:
        print("can't scan the document mr. shubham")


read_text()