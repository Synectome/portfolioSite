from app import db
from models import Message

# this will use the models.py as the template to generate a new
# database file using the chosen db type. During developemnt, we used
# sqlite, in production this will probable be postgres, but we will see

# make sure this only happens when we run this file directly
if __name__ == '__main__':
    db.create_all()
    mesg = Message(name="First and LastName",
                    company="testers Inc.",
                    email="firstRow@entry.com",
                    message="this is a legitimate submission\n which may have \t chars like this ><)*(^^%$$#@%$#@")
    