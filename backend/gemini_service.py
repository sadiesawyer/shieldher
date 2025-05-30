from google import genai

client = genai.Client(api_key="apikeyhere")

def threat_scan(message: str):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Repeat after me, and then give a message confirming it worked: " + message.content,
    )

    return (response.text)