from flask import Flask
from db import db
from routes.process_url_routes import process_url_routes

app = Flask(__name__)
app.config.from_object("config.Config")

# Initialize database
db.init_app(app)

# Register blueprints
app.register_blueprint(process_url_routes)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)