import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "2 + 2"}])
print(completion.choices[0].message.content) 