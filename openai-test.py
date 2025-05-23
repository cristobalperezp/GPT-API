from openai import OpenAI
client = OpenAI()

# response = client.images.generate(
#   prompt="A bear drinking coffee",
#   n=1,
#   size="1024x1024"
# )

# print(response)


# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)
# print(completion)


user_input = input("Ingresa tu mensaje: ")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You will be provided with statements, and your task is to convert them to standard English."},
        {"role": "user", "content": user_input}
    ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)

print(completion.choices[0].message.content)