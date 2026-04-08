from flask import Flask
from api.routes import api_blueprint, health_blueprint
from services.imdb_loader import load_dataset
def create_app() -> Flask:
    app = Flask(__name__)
    # Load and validate the CSV on startup so runtime errors are surfaced early.
    load_dataset()
    app.register_blueprint(health_blueprint)
    app.register_blueprint(api_blueprint, url_prefix="/api")
    return app
app = create_app()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
