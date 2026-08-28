from ollama import chat
import json
import re


SYSTEM_PROMPT = """
You are an engineering requirement parser.

Convert the user's mechanical design request into JSON.

Return ONLY this JSON structure:

{
  "component": "L-bracket",
  "load_kg": 5,
  "safety_factor": 2.0,
  "material": "Steel",
  "max_displacement_mm": 0.5
}

Rules:
- load_kg must be a number.
- Default safety_factor = 2.0.
- Default material = Steel.
- Default max_displacement_mm = 0.5.
- component should describe the requested mechanical component.
- Do NOT write explanations.
- Do NOT use markdown.
- Return ONLY valid JSON.
"""


def parse_requirement(user_request):

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_request
            }
        ],
        format="json"
    )

    content = response["message"]["content"].strip()

    print("\nRaw AI response:")
    print(content)

    # Extract JSON if the model somehow added extra text
    match = re.search(r"\{.*\}", content, re.DOTALL)

    if not match:
        raise ValueError(
            "Llama did not return valid JSON.\n"
            f"AI response was:\n{content}"
        )

    json_text = match.group(0)

    try:
        return json.loads(json_text)

    except json.JSONDecodeError:
        raise ValueError(
            "Llama returned invalid JSON.\n"
            f"AI response was:\n{content}"
        )


if __name__ == "__main__":

    request = input("What do you want to design?\n> ")

    try:

        result = parse_requirement(request)

        print("\n" + "=" * 40)
        print("ENGINEERING REQUIREMENTS")
        print("=" * 40)

        print(json.dumps(result, indent=4))

    except Exception as error:

        print("\n❌ ERROR")
        print(error)
