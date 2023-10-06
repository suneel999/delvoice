import requests
from flask import Flask, render_template,request, redirect, url_for

import pandas as pd
import json

app = Flask(__name__)
url = "https://api.elevenlabs.io/v1/voices"

headers = {
  "Accept": "application/json",
  "xi-api-key": "e327fdf320043677a512f1b0dade8403"
}

response = requests.get(url, headers=headers)
json_response = response.text
data = json.loads(json_response)

# Extract the 'voices' data
voices = data.get('voices', [])

# Convert the data into a DataFrame
df = pd.DataFrame(voices)


@app.route('/')
def index():
    # Parse the JSON response
    data = json.loads(json_response)
    voices = data.get('voices', [])
    return render_template('index.html', voices=voices)
@app.route('/delete', methods=['POST'])
def delete():
    voice_id = request.form['voiceId']
    url = f"https://api.elevenlabs.io/v1/voices/{voice_id}"
    headers = {
        "Accept": "application/json",
        "xi-api-key": "e327fdf320043677a512f1b0dade8403"
    }
    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        # Deletion successful, redirect to the index page
        return "success"
    else:
        # Deletion failed, handle the error (e.g., display an error message)
        return "Failed to delete voice."

if __name__ == '__main__':
    app.run(debug=True)