from flask import Flask, request
from flask_babel import Babel, _, ngettext

app = Flask(__name__)
babel = Babel(app)

# Configure available languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

@babel.localeselector
def get_locale():
    # Use request headers or a user-specific preference to determine locale
    return request.accept_languages.best_match(['en', 'fr'])

@app.route('/')
def index():
    # This will display the string in the appropriate language
    greeting = _("Hello, World!")
    
    # Demo plural forms with different numbers
    message_1 = ngettext(
        "You have one message",
        "You have %(num)d messages",
        1
    ) % {"num": 1}
    
    message_3 = ngettext(
        "You have one message", 
        "You have %(num)d messages",
        3
    ) % {"num": 3}
    
    return f"""
    <h1>{greeting}</h1>
    <p>{message_1}</p>
    <p>{message_3}</p>
    <p><em>Language detected: {get_locale()}</em></p>
    <p><a href="/?lang=en">English</a> | <a href="/?lang=fr">Français</a></p>
    """

@app.route('/test')
def test():
    """Test endpoint to show current locale"""
    return {
        "greeting": _("Hello, World!"),
        "locale": get_locale(),
        "message_singular": ngettext("You have one message", "You have %(num)d messages", 1),
        "message_plural": ngettext("You have one message", "You have %(num)d messages", 3) % {"num": 3}
    }

if __name__ == "__main__":
    app.run(debug=True)