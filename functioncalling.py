from google import genai
from google.genai import types
import json
import utlis


# Function declarations for Gemini
add_function = types.FunctionDeclaration(
    name="add",
    description="Adds two numbers.",
    parameters={
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "The first number."},
            "b": {"type": "number", "description": "The second number."},
        },
        "required": ["a", "b"],
    },
)

sum_function = types.FunctionDeclaration(
    name="sum_list",
    description="Calculates the sum of a list of numbers.",
    parameters={
        "type": "object",
        "properties": {
            "numbers": {
                "type": "array",
                "items": {"type": "number"},
                "description": "List of numbers to sum.",
            },
        },
        "required": ["numbers"],
    },
)

client = genai.Client()
tools = types.Tool(function_declarations=[add_function, sum_function])
config = types.GenerateContentConfig(tools=[tools])

# Ask Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Add 5 and 7",
    config=config,
)

# Check for function call
if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"Arguments: {function_call.args}")

    # Dispatch to your Python implementation
    if function_call.name == "add":
        result = add(**function_call.args)
    elif function_call.name == "sum_list":
        result = sum_list(**function_call.args)
    else:
        result = "Unknown function"

    print("Result:", result)
else:
    print("No function call found.")
    print(response.text)
