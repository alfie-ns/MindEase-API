# initial_plan.py

import openai, os
from dotenv import load_dotenv

load_dotenv() # Load the .env file

'''
   This file contains the code to generate an initial plan for the user based on their profile information; 
   it uses the OpenAI API to generate the plan. The function generate_initial_plan takes the user_profile as
   input and generates an initial plan based on the user's profile information. The function uses the OpenAI
   ChatCompletion API to generate the plan. 
'''

def generate_initial_plan(user_profile):
    
    openai.api_key = os.getenv("OPENAI_API_KEY") # Extract -> Set API key

    prompt = f"""

    User Profile:
    - Name: {user_profile.name}
    - Gender: {user_profile.gender}
    - Age: {user_profile.age}
    - Weight: {user_profile.weight}
    - Height: {user_profile.height}
    - Goal: {user_profile.goal}
    - Activity Level: {user_profile.activity_level}
    - Determination Level: {user_profile.determination_level}
    - Brain Injury Context: {user_profile.brain_injury_context}
    - Brain Injury Severity: {user_profile.brain_injury_severity}
    - General Context: {user_profile.general_context}
    - Strengths: {user_profile.strengths}
    - Weaknesses: {user_profile.weaknesses}

    Based on the user's profile information, generate an initial plan to help the user achieve their cognitive prime. Provide specific recommendations and steps.
    """

    res = openai.ChatCompletion.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": """You are are an expert life coach. Create an initial assessment to determine the user's cognitive strengths and weaknesses, 
                                             if they're not provided in the user profile, if they are, use them to generate an initial plan.
                                             Furthermore, you will create a personalized training plan based on their needs:"""},
            {"role": "user", "content": prompt}
        ]
    )

    initial_plan = res["choices"][0]["message"]["content"]

    return initial_plan