# web_app/routes/weather_routes.py

from flask import Blueprint, request, jsonify

from covid_tracker import get_cases

country_routes = Blueprint("country_routes", __name__)


@country_routes.route("/country/cases.json")
def case_forecast_api():
    print("COVID CASES...")
    print("URL PARAMS:", dict(request.args))

    country_id = request.args.get("country_id") or "USA"

    results = get_cases(
        country_id=country_id)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message": "Invalid Country. Please try again."}), 404
