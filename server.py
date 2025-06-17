from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])  # We changed this from /analyzer-data to /data
def receive_data():
    try:
        raw_data = request.get_data(as_text=True)
        print("📥 Received:", raw_data)

        # Optional: Save locally if not in production
        import os
        if os.environ.get("FLASK_ENV") != "production":
            with open("data_log.txt", "a") as f:
                f.write(raw_data + "\n")

        return "OK", 200
    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
