from flask import Blueprint, render_template

signup = Blueprint('signup', __name__)


@signup.route('/signUp')
def signing_up():

    return render_template("sign_up.html")


