import eel

eel.init("HTMLS")
@eel.expose
def alert_value(x):
    return x

eel.start("index.html",size=(500,500))


