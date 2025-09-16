import google.generativeai as genai

# Replace with your real API key
genai.configure(api_key="YOUR_API_KEY")

# List all available models
for m in genai.list_models():
    print(m.name, " -> ", m.supported_generation_methods)
