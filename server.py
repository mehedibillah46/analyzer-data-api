from flask import Flask, request

app = Flask(__name__)

def parse_hex_data(hex_str):
    # Clean up whitespace/newlines
    hex_str = hex_str.strip()

    try:
        # Example: Extract bytes from raw HEX (this is just an example!)
        # You MUST replace this logic with actual byte positions and scaling for your analyzer
        do_raw = int(hex_str[6:10], 16)      # bytes 3–4 (2 bytes)
        ph_raw = int(hex_str[10:14], 16)     # bytes 5–6 (2 bytes)
        temp_raw = int(hex_str[14:18], 16)   # bytes 7–8 (2 bytes)

        # Convert raw to scaled values (example: divide by 100)
        do = do_raw / 100
        ph = ph_raw / 100
        temp = temp_raw / 10

        return {
            "dissolved_oxygen": do,
            "ph": ph,
            "temperature": temp
        }

    except Exception as e:
        return {"error": str(e)}

@app.route('/data', methods=['POST'])
def receive_data():
    raw_data = request.get_data(as_text=True)
    print("📥 Raw Received:", raw_data)

    parsed = parse_hex_data(raw_data)

    print("🔍 Parsed Data:", parsed)

    # Save to log file
    with open("data_log.txt", "a") as f:
        f.write(raw_data + "\n")

    return "OK", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
