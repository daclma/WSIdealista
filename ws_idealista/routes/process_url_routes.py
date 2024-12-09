from flask import Blueprint, request, jsonify
from service.houses_service import get_houses, clean_houses, update_new_houses, compare_houses, process_houses

process_url_routes = Blueprint("process_url_routes", __name__)

#Example URL: https://www.idealista.com/alquiler-viviendas/barcelona/horta-guinardo/?ordenado-por=fecha-publicacion-desc
@process_url_routes.route("/processUrl", methods=["GET"])
def processURL():
    try:
        url = request.args.get(f"url")
        if not url:
            return jsonify({"error" : "Invalid URL"}), 400
        
        new_houses = process_houses(url)

        return jsonify({
            "status": 200, 
            "content": new_houses
            }), 200
    except Exception as e:
        return jsonify({"error" : "Generic error during web scraping: " + str({e})}), 500
