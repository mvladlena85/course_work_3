import werkzeug
from flask import Flask

from api.api import api_blueprint
from main.main import main_blueprint


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def handle_bad_request(e):
    return '<b>Код 404 </b></br>Страница не существует!', 404


@app.errorhandler(500)
def handle_internal_server_error(e):
    return '<b>Код 500 </b></br>Возникла ошибка на стороне сервера!', 500


if __name__ == "__main__":
    app.run()
