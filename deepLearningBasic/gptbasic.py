import openai

openai.api_key = "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"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "介绍一下你自己"}]
)
print(response.choices[0].message['content'])
