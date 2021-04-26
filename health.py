import json
import requests
from flask import Flask, jsonify, request


# inference 8080
INFERENCE_URL = "http://localhost:8080"
# management 8081
MANAGEMENT_URL = "http://localhost:8081"


app = Flask(__name__)


@app.route("/predictions/<model_name>", methods=["POST"])
def predictions(model_name):
    try:
        if request.is_json:
            content = request.get_json()
            text = content['text']
            num_samples = content['num_samples']
            length = content['length']
            data = {
                'text': text,
                'num_samples': num_samples,
                'length': length
            }
            headers = {'Content-Type': 'application/json; charset=utf-8'}
            path = f"/predictions/{model_name}"
            post_path = INFERENCE_URL + path
            res = requests.post(post_path, headers=headers, data=json.dumps(data))

            res = res.json()
            return jsonify(json.dumps(res)), 200
        return jsonify(json.dumps([-1])), 400
    except Exception as e:
        print(e)
        return jsonify(json.dumps([-1])), 400


@app.route("/model_status", methods=["GET"])
def model_status():
    model_name = request.args.get("model_name")
    path = f"/models/{model_name}"
    get_path = MANAGEMENT_URL + path
    res = requests.get(get_path)

    if res.status_code != 200:
        return jsonify({
            "code": res.status_code,
            "status": "UNKNOWN"
        })

    models_status = res.json()

    num_workers = len(models_status)
    if num_workers == 0:
        return jsonify({
            "code": res.status_code,
            "status": "LOADING"
        })
    model_status = models_status[0]

    if len(model_status["workers"]) == 0:
        return jsonify({
            "code": res.status_code,
            "status": "LOADING"
        })

    # if model is loaded, then return "READY"
    return jsonify({
            "code": res.status_code,
            "status": model_status["workers"][0]["status"]
    })


@app.route("/ping", methods=["GET"])
def ping():
    path = "/ping"
    get_path = INFERENCE_URL + path
    res = requests.get(get_path)

    if res.status_code != 200:
        return jsonify({
            "health": "No Healthy!",
            "code": res.status_code
        })

    result = res.json()
    result["code"] = res.status_code
    return jsonify(result)


@app.route("/healthz", methods=["GET"])
def health_check():
    return "OK", 200


if __name__ == "__main__":
    app.run(debug=False, port=8000, host="0.0.0.0", threaded=True)

