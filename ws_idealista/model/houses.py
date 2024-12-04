from db import db

class Houses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return f"HouseId(house_id={self.house_id})"