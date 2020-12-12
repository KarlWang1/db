from bottle import Bottle, post, get, HTTPResponse, request, response, template
import bottle



#Our bottle app, using the default. We can store variables in app
app = bottle.default_app()

#Hello World. This is a simple test! You do not need to make any changes.
@get("/hello")
def hello():
    return ('hello world')


# TODO This is what you need to get working for proj7. It should return 'hello <name>' where name is parsed from the URL
# For example, calling localhost:53001/hello/aaron returns 'hello aaron'.
# TODO This function is broken in two ways. Please read the quickstart guide or my notes
@get("/hello/<name>")
def hello_name():
    return ('hello world')


#The main function to start the server
if __name__ == "__main__":
    print("Your server is running. Please check http://localhost:53001/hello in your favorite web browser. If you see 'hello world' then run simpletest.py")
    app.run(host="localhost", port=53001, debug=True)
