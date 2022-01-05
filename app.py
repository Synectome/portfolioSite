from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instantiate the app
app = Flask(__name__)
# When live, this should come in from environment var, and not hardcoded for sec
app.config['SECRET_KEY'] = 'FlyingBirdsExcellentBirdsWatchThemFlyThereTheyGo'
# sqlite db configuration for the URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# database instantiation
db = SQLAlchemy(app)

# Import all of our routes (equivalent to having the whole routes file right here)
# This must occure after initializing the app, because it is used in routes
from routes import *

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
