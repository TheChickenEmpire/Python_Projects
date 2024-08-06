from openai import OpenAI

client = OpenAI('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')

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")