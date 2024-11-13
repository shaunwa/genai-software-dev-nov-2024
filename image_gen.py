from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a tropical landscape with lots of colorful flowers",
  size="1024x1024",
  quality="standard", 
  n=1,
)

image_url = response.data[0].url

print(image_url)