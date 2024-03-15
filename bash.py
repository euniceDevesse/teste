import ollama
response = ollama.chat(model='phi', messages=[
  {
    'role': 'user',
    'content': 'What is your name?',
  },
])
print(response['message']['content'])