import google.generativeai as genai
import os

# Set up the model
generation_config = {
    'temperature': 0.3,
    'top_p': 0.6,
    'top_k': 20,
}

safety_settings = [
    {
        'category': 'HARM_CATEGORY_DANGEROUS',
        'threshold': 'BLOCK_NONE',
    },
    {
        'category': 'HARM_CATEGORY_HARASSMENT',
        'threshold': 'BLOCK_NONE'
    },
    {
        'category': 'HARM_CATEGORY_HATE_SPEECH',
        'threshold': 'BLOCK_NONE'
    },
    {
        'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT',
        'threshold': 'BLOCK_NONE'
    },
    {
        'category': 'HARM_CATEGORY_DANGEROUS_CONTENT',
        'threshold': 'BLOCK_NONE'
    },
]
api_key = os.getenv('GEMINI_API_KEY')
model = os.getenv('GEMINI_MODEL')
if not model:
    model = 'gemini-1.5-flash'

genai.configure(api_key=api_key)
model = genai.GenerativeModel(
            model_name=model,
            generation_config=generation_config,
            safety_settings=safety_settings,
        )

response = model.generate_content(contents=["Hello?"],stream=True)
for chunk in response:
    print(chunk.text, end="")
