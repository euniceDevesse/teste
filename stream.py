import ollama

#ollama.embeddings(model='phi', prompt='The sky is blue because of rayleigh scattering')

stream = ollama.chat(
    model='phi',
    messages=[{'role': 'user', 'content': 'what is the secret of life?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)