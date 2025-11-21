import google.generativeai as genai
import os

genai.configure(api_key='AIzaSyA_Xy5e-No5HBkAmlMRPwS_y9iRRJyx0ZQ')

print("Available Gemini models:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"  - {model.name}")
