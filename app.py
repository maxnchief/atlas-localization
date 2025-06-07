from flask import Flask, request
from flask_babel import Babel, _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
app.config['LANGUAGES'] = ['en', 'fr']

babel = Babel(app)

@babel.locale_selector
def get_locale():
    # Try to get locale from query parameter (?lang=fr), fallback to best match
    return request.args.get('lang') or request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    greetings = _("Hello, World!")
    return greetings

if __name__ == '__main__':
    app.run(debug=True)