import os
import json
from groq import Groq
from dotenv import load_dotenv

try:
    from .prompt import complaint_prompt
except ImportError:
    from prompt import complaint_prompt

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("Missing GROQ_API_KEY in environment. Set GROQ_API_KEY in ai/.env or your environment variables.")

client = Groq(api_key=GROQ_API_KEY)


def analyze_complaint(complaint_text: str) -> dict:
    prompt = complaint_prompt.format(complaint_text=complaint_text)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content
    # Strip markdown code fences if the model returns JSON wrapped in ```
    content = content.strip()
    if content.startswith("```") and content.endswith("```"):
        content = content[3:-3].strip()

    try:
        result = json.loads(content)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Unable to parse Groq response as JSON: {exc}\nResponse was: {content}")

    return {
        "category": result.get("category", ""),
        "priority": result.get("priority", ""),
        "summary": result.get("summary", ""),
        "suggested_solution": result.get("suggested_solution", "")
    }


if __name__ == "__main__":
    sample_complaint = "My electricity bill is too high."
    output = analyze_complaint(sample_complaint)
    print(json.dumps(output, indent=2, ensure_ascii=False))
