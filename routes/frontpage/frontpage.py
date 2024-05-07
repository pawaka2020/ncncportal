# routes/frontpage/frontpage.py
import justpy as jp

def frontpage():
    wp = jp.WebPage()

    jp.P(text="NCNC Portal3 home page", a=wp, classes="text-2xl m-4")

    # Return the webpage
    return wp

