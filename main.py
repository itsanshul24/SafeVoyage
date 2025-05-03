import openai

openai.api_key = "your-openai-key"

prompt = input("Ask something: ")

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=50
)

print(response.choices[0].text.strip())
