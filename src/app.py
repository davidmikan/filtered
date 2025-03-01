from openai import OpenAI

with open('api_token.txt', 'r') as f:
    api_key = f.read().strip()

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com/v1"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "Complete this sentence: Hello world, "}
    ]
)

print(response.choices[0].message.content)