"""Message wall where visitors can post messages which show up directly on the home page.

Providing a name is optional, with messages posted anonymously by default. Every message's associated IP address and
location exports into the user database under the wall table.
"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class MessageWallForm(FlaskForm):
    """Form for adding messages to the public message wall, and the wall table in the user database."""

    name = StringField("name")
    message = StringField("message", validators=[DataRequired()])
