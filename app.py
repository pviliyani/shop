from flask import Flask
from blueprint.general import app as general
app = Flask(__name__)
app.register_blueprint(general)




if __name__ == '__main__':
    app.run()
