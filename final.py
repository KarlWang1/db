from bottle import Bottle, post, get, HTTPResponse, request, response, template
import bottle
import os
import sys
import psycopg2 as pg
import logging
import argparse


#The logging level to control what messages are shown (skipping debug)
logging.basicConfig(level=logging.INFO)

#Our bottle app, using the default. We can store variables in app
app = bottle.default_app()

#Hello World
@get("/hello")
def hello():
    # Use a template to get the HTML to return. This template needs variables page_name (also for header.tpl) and  body 
    return template('main', page_name='Hello, World', body='This is the body of hello world')


#The main function to start the server
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c","--config",
        help="The path to the .conf configuration file.",
        default="server.conf"
    )
    parser.add_argument(
        "--host",
        help="Server hostname (default localhost)",
        default="localhost"
    )
    parser.add_argument(
        "-p","--port",
        help="Server port (default 53001)",
        default=53001,
        type=int
    )
    parser.add_argument(
        "--nodb",
        help="Disable DB connection on startup",
        action="store_true"
    )

    #Get the arguments
    args = parser.parse_args()
    if not os.path.isfile(args.config):
        logging.error("The file \"{}\" does not exist!".format(args.config))
        sys.exit(1)

    app.config.load_config(args.config)

    # Below is how to connect to a database. We put a connection in the default bottle application, app
    if not args.nodb:
        try:
            app.db_connection = pg.connect(
                dbname = app.config['db.dbname'],
                user = app.config['db.user'],
                password = app.config.get('db.password'),
                host = app.config['db.host'],
                port = app.config['db.port']
            )
        except KeyError as e:
            logging.error("Is your configuration file ({})".format(args.config) +
                        " missing options?")
            raise

    try:
        logging.info("Starting Bottle Web Server")
        app.run(host=args.host, port=args.port, debug=True)
    finally:
        #Ensure that the connection opened is closed 
        if not args.nodb:
            app.db_connection.close()
