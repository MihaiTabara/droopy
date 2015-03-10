from flask import render_template, Blueprint, request, current_app as app
from application.forms import DroopyForm
from application.drootweepy import Drootweepy

portal = Blueprint('portal', __name__, url_prefix='/portal')


@portal.route('/', methods=['GET', 'POST'])
def index():
    form = DroopyForm(request.form)
    if form.validate_on_submit():
        drootweepy = Drootweepy(app.config['CONSUMER_KEY'],
                                app.config['CONSUMER_SECRET'],
                                app.config['ACCESS_TOKEN'],
                                app.config['ACCESS_TOKEN_SECRET'],
                                form.no_of_tweets.data)
        tweets = drootweepy.scrap_user(form.screen_name.data)
        return render_template('tweets.html', tweets=tweets)

    ctx = {
        'form': form,
    }
    return render_template('homepage.html', **ctx)
