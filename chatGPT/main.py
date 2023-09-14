import openai
import config

openai.api_key = config.api_key
response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
    messages= [{"role": "user", "content": "Hi, is it a good night in Argentina?"}])
print(f"Message: {response.choices[0].message.content}\nRemaining usages: {response.usage}")