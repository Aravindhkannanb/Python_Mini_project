import webbrowser as wb
def web():
    url=(
        'https://www.stackoverflow.com',
        'https://www.gmail.com',
        "https://www.youtube.com"
    )
    for i in url:
        print("Opening "+i)
        wb.get(using=None).open(i)
web()