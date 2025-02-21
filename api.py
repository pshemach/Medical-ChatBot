from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is running!"}

# Use Ollama locally to generate service descriptions
OLLAMA_MODEL = "deepseek-r1:7b"  # Change to "llama2" if needed

@app.post("/generate_description")
def generate_description(data: dict):
    prompt = f"""
    Generate a customer-attractive service package description in bullet points for a booking system website.

    Industry: {data['industry']}
    Package Name: {data['package_name']}
    Services Included: {", ".join(data['services'])}

    - Highlight the key benefits and unique selling points.
    - Use persuasive and engaging language to attract customers.
    - Keep it concise, within 100 words.
    - Include a strong call-to-action.
    """

    # Send prompt to Ollama running locally
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": OLLAMA_MODEL, "prompt": prompt}
    )

    output = response.json()
    return {"description": output["response"]}
