import requests
from sys import exit

r = requests.get("http://localhost:53001/hello")
if r.status_code != 200:
    print("Error did not receive a 200 response code from the simple hello world. Is your server running?")
    exit(1)
else: 
    if r.text != "hello world":
        print("Your simple hello world example is not working. did you change the function?")
        exit(1)
    
r = requests.get("http://localhost:53001/hello/anya")
if r.status_code != 200:
    print("Error did not receive a 200 response code from the simple hello world. did you fix the function hello_name?")
    exit(1)
else: 
    if r.text != "hello anya":
        print("Your simple hello world example is not working. did you get it working? I was expecting hello anya and got: %s"%r.text)
        exit(1)
    
    
r = requests.get("http://localhost:53001/hello/Shreya")
if r.status_code != 200:
    print("Error did not receive a 200 response code from the simple hello world. did you fix the function hello_name?")
    exit(1)
else: 
    if r.text != "hello Shreya":
        print("Your simple hello world example is not working. did you get it working? I was expecting hello Shreya and got: %s"%r.text)
        exit(1)

print("It seems like your simple web server is working!")