from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import requests
import simplejson as json

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import CatSighting


def get_kitten_images():
    response = requests.get('http://api.giphy.com/v1/gifs/search?q=kitty&api_key=dc6zaTOxFJmzC&limit=50&offset=0')
    return [gif['images']['fixed_width_small']['url'] for gif in response.json()['data']]


@app.route('/cat-sightings/')
def get_cat_sightings():
    cat_sightings = CatSighting.query.all()
    return json.dumps(
        {'results':
            [
                {
                    'location': json.loads(cat_sighting.location),
                    'photo_url': cat_sighting.photo_url,
                }
                for cat_sighting in cat_sightings
            ]
         }
    )


@app.route('/')
def dummy_map():
    return render_template('dummy_map.html')

if __name__ == '__main__':
    app.run()
