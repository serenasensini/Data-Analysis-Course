from flask import Blueprint, jsonify
from services.imdb_loader import get_dataset
health_blueprint = Blueprint("health", __name__)
api_blueprint = Blueprint("api", __name__)
@health_blueprint.get("/health")
def health_check():
    return jsonify({"status": "ok", "message": "API is running"}), 200

@api_blueprint.get("/oldestMovie")
def oldest_movie():
    get_dataset()
    return (
        jsonify(
            {
                "message": "Endpoint not implemented yet. Implement with pandas during the lab.",
                "endpoint": "oldestMovie",
            }
        ),
        301,
    )
@api_blueprint.get("/bestMovie")
def best_movie():
    get_dataset()
    return (
        jsonify(
            {
                "message": "Endpoint not implemented yet. Implement with pandas during the lab.",
                "endpoint": "bestMovie",
            }
        ),
        301,
    )
@api_blueprint.get("/totMoviePerYear")
def total_movie_per_year():
    get_dataset()
    return (
        jsonify(
            {
                "message": "Endpoint not implemented yet. Implement with pandas during the lab.",
                "endpoint": "totMoviePerYear",
            }
        ),
        301,
    )
