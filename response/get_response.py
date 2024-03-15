import anthropic, requests, dotenv, os

dotenv.load_dotenv()



def get_response(request):
    # Get the prompt from the request body
    prompt = request.data["prompt"]

    

    # Get the API key from the environment variables
    API_KEY = os.getenv("CLAUDE_KEY")
    API_URL = "https://api.anthropic.com/v1/complete"

    client = anthropic.Anthropic(api_key=API_KEY)
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    

    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0.0,
        system=f"You are a assistant to a user that needs help, user={user_details}",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

  
    response = message.content
    return response
    





#print(message.content)




