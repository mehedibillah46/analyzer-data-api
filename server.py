from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])  # Accepts POST to root "/"
def receive_data():
    data = request.get_data(as_text=True)
    print("📥 Received:", data)

    # Optional: Save to file
    with open("data_log.txt", "a") as f:
        f.write(data + "\n")

    return "OK", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
