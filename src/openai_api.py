import os
import glob
import base64
import io
import requests
from PIL import Image

# Get the latest screenshot file
list_of_files = glob.glob('/Users/andrewyu/Desktop/ssf/assets/*.png')
latest_file = max(list_of_files, key=os.path.getctime)

# Open image file
img = Image.open(latest_file)

# Convert image to base64
buffer = io.BytesIO()
img.save(buffer, format='PNG')
img_base64 = base64.b64encode(buffer.getvalue()).decode()

# Prepare data for API
data = {
  'inputs': {
    'image': {
      'url': 'data:image/png;base64,' + img_base64
    },
    'prompt': 'describe what is in this image succinctly',
  }
}

# Send POST request to OpenAI API
headers = {'Authorization': f'Bearer {os.getenv('OPENAI_API_KEY')}'
response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers, json=data)

# Display the response
print(response.json())
