import openai
openai.api_key = "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"
while True:
    print("You:")
    Ask = input("")
    print("Generating....")
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "assistant", "content": Ask}])
    print(completion.choices[0].message.content)