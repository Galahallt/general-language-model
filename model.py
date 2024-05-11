import google.generativeai as genai
import config

genai.configure(api_key=config.GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro")

prompt = """Show your result in paragraph form. 
    It should have at least 100 words and MUST start with the given input. 
    Continue the following input with a realistic and intense Formula One commentary as if it was during a race day: {}""".format(
    input()
)

result = model.generate_content(prompt)

print(result.text)
