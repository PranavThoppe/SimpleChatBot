import openai

openai.api_key = 'API-Key'
openai.base_url = "http://localhost:3040/v1/"

completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": input("Ask GPT: ")},
    ],
)

print("GPT:",completion.choices[0].message.content, sep=" ")