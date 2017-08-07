import os
import random
import simplejson as json
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db, get_kitten_images
from models import CatSighting


app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def seed_database():
    kitten_image_urls = get_kitten_images()
    for url in kitten_image_urls:
        cat_sighting = CatSighting(
            photo_url=url,
            location=json.dumps(
                {
                    'lat': 47 + random.randrange(6500, 6600)/10000.,
                    'lng': -122 - random.randrange(3450, 3550)/10000.,
                }
            )
        )
        db.session.add(cat_sighting)
        db.session.commit()

if __name__ == '__main__':
    manager.run()
