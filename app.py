# Common Classes
import json
from flask import Flask

# Private Classes
from db.models import database
from api.freeboard import default as freeboard_default

if __name__ == '__main__':
    # Load configuration
    with open('config.json', 'r') as f:
        data = f.read()
    config = json.loads(data)

    # Create app
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(freeboard_default, url_prefix = '/freeboard')

    # Config app
    urlstring ='mysql+mysqldb://%s:%s@%s/%s' % \
                (config['DATABASE_USER'],
                 config['DATABASE_PASS'],
                 config['DATABASE_URL'],
                 config['DATABASE_DBNAME'])

    print(urlstring)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://%s:%s@%s/%s' % \
                                           (config['DATABASE_USER'],
                                            config['DATABASE_PASS'],
                                            config['DATABASE_URL'],
                                            config['DATABASE_DBNAME'])

    # Init DB
    database.init(app)
    db = database.get_db()


    # Run Flask Web Server
    app.run(host=config['host'], port=config['port'])
