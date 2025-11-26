#!/usr/bin/env python3
"""
Basic Flask app for i18n project.
Exposes a single '/' route rendering templates/1-index.html With Babel.
"""

from flask import Flask, render_template, g, request
from flask_babel import Babel, gettext as _


class Config:
    '''Class Config with all the config modeule'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'fr'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_locale():
    """Get locale with a default en"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)


@app.route("/", methods=["GET"])
def index():
    home_title = _("home_title")
    home_header = _("home_header")
    """Render the 1-index.html page"""
    return render_template("3-index.html", home_title=home_title, home_header=home_header)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
