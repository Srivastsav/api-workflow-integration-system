from flask import Flask, request, jsonify

app = Flask(__name__)

leave_requests = []

@app.route("/")
def home():
    return "System Running"

@app.route("/leave-request", methods=["POST"])
def create_leave():
    data = request.json

    request_entry = {
        "employee_name": data.get("employee_name"),
        "leave_type": data.get("leave_type"),
        "status": "Pending"
    }

    leave_requests.append(request_entry)

    return jsonify(request_entry)

@app.route("/requests")
def get_requests():
    return jsonify(leave_requests)

if __name__ == "__main__":
    app.run()
