import os
import glob
import base64
import openai

# Get the latest screenshot file
list_of_files = glob.glob('/Users/andrewyu/Desktop/ssf/assets/*.png')
latest_file = max(list_of_files, key=os.path.getctime)

# Read the image file and encode it in base64
with open(latest_file, "rb") as image_file:
    img_base64 = base64.b64encode(image_file.read()).decode()

# Initialize the OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()

# Create a chat completion with the image
# Create a chat completion with the image
response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{img_base64}"
                    }
                },
            ],
        }
    ],
    max_tokens=300,
)
# Print the response
print(response.choices[0])
