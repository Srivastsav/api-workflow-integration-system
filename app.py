from flask import Flask, request, jsonify

app = Flask(__name__)

# fake database (just a list for now)
leave_requests = []

@app.route("/")
def home():
    return "API Workflow System Running"

@app.route("/leave-request", methods=["POST"])
def create_leave():
    data = request.json

    # Basic validation
    required_fields = ["employee_name", "leave_type", "start_date", "end_date"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    # simulate processing
    request_entry = {
        "employee_name": data["employee_name"],
        "leave_type": data["leave_type"],
        "status": "Pending Approval"
    }

    leave_requests.append(request_entry)

    return jsonify({
        "message": "Leave request created",
        "data": request_entry
    })

@app.route("/requests", methods=["GET"])
def get_requests():
    return jsonify(leave_requests)

if __name__ == "__main__":
    app.run(debug=True)
