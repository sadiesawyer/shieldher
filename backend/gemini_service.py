from google import genai
from google.genai import types
from backend.schemas import MessageAnalysis

client = genai.Client(api_key="") #https://ai.google.dev/gemini-api/docs/quickstart

def threat_scan(message: str):
    prompt = f"""
    Your job is to:
    1. Analyze the message below.
    2. Score the message on a **risk scale** from Low to High including Moderately Low/High.
    3. Provide a one-sentence explanation of why you chose that score.
    4. Recommend what the user should do next. Be calm, supportive, and specific, but no need to include extraneous detail or commentary.

    Common red flags include urgent or threatening language, unfamiliar senders, spelling errors, improper grammar, generic greetings, mismatched or suspicious email domains, unverifiable senders, and deceptive links or attachments. Users should hover to preview links, be wary of pressure tactics, and avoid providing sensitive info. Awareness and caution are the best defenses.


    Here is the message to analyze:
    \"\"\"{message}\"\"\"

    Respond using this structure:

    Risk Score: <low, medium, high>
    Explanation: <why this score>
    Recommended Action: <what the user should consider doing>
    """
    #generated with gemini

    #next - add streaming to speed up the process: https://ai.google.dev/gemini-api/docs/text-generation
    # https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse 
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": MessageAnalysis,
                "max_output_tokens": 500,
                "system_instruction": "You are an AI assistant trained to detect online harassment and manipulation in text messages.",
            }
        )
        return (response.parsed)
    except Exception as e:
        print(f"Gemini API Call Failed: {e}")
    