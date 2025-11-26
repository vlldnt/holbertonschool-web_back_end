#!/usr/bin/env python3
"""
Basic Flask app for i18n project.
Exposes a single '/' route rendering templates/1-index.html With Babel.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    '''Class Config with all the config modeule'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale():
    """Get locale with a default en

    The order of priority should be:

    Locale from URL parameters
    Locale from user settings
    Locale from request header
    Default locale
    """

    # 1. from URL
    url_locale = request.args.get("locale")

    if url_locale in app.config["LANGUAGES"]:
        return url_locale

    # 2. from user Setting
    if g.get("user"):
        user_locale = g.user.get("locale")

        if user_locale in app.config.get("LANGUAGES"):
            return user_locale
    
    # 3. from request header 
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """Get user id fonction"""

    user_id = request.args.get("login_as")

    if user_id is None:
        return None

    return users.get(int(user_id))


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)


@app.before_request
def before_request():
    """app.before.request to find user connected"""

    g.user = get_user()


@app.route("/", methods=["GET"])
def index():
    """Render the 5-index.html page"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
