# ai_text_generator.py
# Simple AI Text Generator by Bárbara dos Reis

import openai

def generate_text(prompt):
    # You need to have an API key from OpenAI and set it as an environment variable
    # Example (on terminal): export OPENAI_API_KEY="your_api_key_here"
    openai.api_key = "your_api_key_here"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=100
        )

        print("🤖 AI says:")
        print(response["choices"][0]["message"]["content"])

    except Exception as e:
        print("⚠️ Error:", e)


if __name__ == "__main__":
    user_input = input("Enter a prompt for the AI: ")
    generate_text(user_input)
