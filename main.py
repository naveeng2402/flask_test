from website import create_app

app = create_app()

if __name__ == "__main__":
    from dotenv import load_dotenv
    from os import environ
    load_dotenv('.env')
    
    IP = environ.get('IP')
    PORT = environ.get('PORT')
    
    app.run(debug=True, host=IP, port=PORT)