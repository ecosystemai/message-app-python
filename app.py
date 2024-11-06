from flask import Flask, render_template, request, jsonify
import requests
import json  # Import json for serialization

app = Flask(__name__)

# API URLs
MESSAGES_API_URL = 'http://localhost:8098/invocations'
PERSONALITY_API_URL = 'http://localhost:8092/invocations'
ACCEPTANCE_API_URL = 'http://localhost:8098/response'

def fetch_personality(customer_number):
    headers = {'Content-Type': 'application/json'}
    body = {
        "campaign": "spend_personality",
        "subcampaign": "api",
        "channel": "app",
        "customer": customer_number,
        "userid": "flask",
        "numberoffers": 1,
        "params": "{}"
    }
    try:
        response = requests.post(PERSONALITY_API_URL, json=body, headers=headers)
        response.raise_for_status()
        data = response.json()
        print("Personality API response:", data)  # Debug log
        personality = data.get("final_result", [{}])[0].get("result_full", {}).get("trait", "")
        return personality
    except Exception as e:
        print("Error fetching personality:", e)  # Debug log
        raise

def fetch_messages(customer_number):
    try:
        personality = fetch_personality(customer_number)
        headers = {'Content-Type': 'application/json'}
        body = {
            "campaign": "budget_messages",
            "subcampaign": "none",
            "channel": "app",
            "customer": "none",
            "userid": "none",
            "numberoffers": 4,
            "params": json.dumps({
                "input": ["contextual_variable_one", "contextual_variable_two"],
                "value": [personality, ""]
            })  # Convert params to JSON string
        }
        response = requests.post(MESSAGES_API_URL, json=body, headers=headers)
        response.raise_for_status()
        data = response.json()
        print("Messages API response:", data)  # Debug log
        messages = data.get("final_result", [])
        return messages
    except Exception as e:
        print("Error fetching messages:", e)  # Debug log
        raise


def accept_message(uuid, offer_name):
    headers = {'Content-Type': 'application/json'}
    body = {
        "uuid": uuid,
        "offers_accepted": [{"offer_name": offer_name}],
        "channel_name": "app"
    }
    try:
        response = requests.post(ACCEPTANCE_API_URL, json=body, headers=headers)
        response.raise_for_status()
        print("Acceptance API response:", response.json())  # Debug log
        return response.json()
    except Exception as e:
        print("Error sending acceptance:", e)  # Debug log
        raise

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_messages', methods=['POST'])
def handle_fetch_messages():
    customer_number = request.form.get('customerNumber')
    try:
        messages = fetch_messages(customer_number)
        return jsonify({'messages': messages, 'success': True})
    except Exception as e:
        return jsonify({'error': str(e), 'success': False})

@app.route('/accept_message', methods=['POST'])
def handle_accept_message():
    data = request.json
    uuid = data.get('uuid')
    offer_name = data.get('offerName')
    try:
        accept_message(uuid, offer_name)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e), 'success': False})

if __name__ == '__main__':
    app.run(debug=True)
