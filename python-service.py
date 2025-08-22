from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Define the path for the counter file
COUNTER_FILE = "/data/counter.txt"
#COUNTER_FILE = os.path.join(os.path.dirname(__file__), "counter.txt")

"""
def ensure_counter_file():
    # Crée le fichier counter.txt si il n'existe pas, avec valeur initiale 0.

    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "w") as f:
            f.write("0")
"""

def read_counter():
    """
    Reads and returns the current counter value from the file.
    Returns 0 if the file doesn't exist.
    """
    # ensure_counter_file()
    with open(COUNTER_FILE, "r") as f:
        return int(f.read().strip())

def update_counter(counter):
    """
    Updates the counter file with the new counter value.
    """
    # ensure_counter_file()
    with open(COUNTER_FILE, "w") as f:
        f.write(str(counter))

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    counter = read_counter()
    if request.method == 'POST':
        counter += 1
        update_counter(counter)
        return f"POST requests counter updated. Current count: {counter}"
    else:
        return f"Current POST requests count: {counter}"

@app.route('/health', methods=['GET'])
def health_check():
    try:
        read_counter()
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "reason": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
