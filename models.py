from app import db

# each table is an extension of the db.Model class
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    company = db.Column(db.String(64))
    email = db.Column(db.String(64), nullable=False)
    message = db.Column(db.String(1024), nullable=False)

    # I should time stamp the submissions in this table

    def __repr__(self):
        return f'name: {self.name}, w-mail: {self.email}, left a message:\n{self.message}\n\n'