import os
import time 
from google import genai
from google.genai import types
import config

def generate_response(prompt,temperature=0.5):
    try:
        client=genai.Client(api_key=config.GEMINI_API_KEY)
        contents=[
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(tex6=prompt)
                ],
            ),
        ]
        generate_content_config=types.GenerateContentConfig(
            temperature=temperature,
            response_mime_type="text/plain",
        )
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"
    
def temperature_prompt_activity():
    print("=" * 80)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE & INSTRUCTION-BASED PROMPTS")
    print("=" * 80)
    print("\nIn this activity, we'll explore:")
    print("1. How temperature affects AI creativity and randomness")
    print("2. How instruction-based prompts can control AI outputs")
    print("\n" + "-" * 40)
    print("PART 1: TEMPERATURE EXPLORATION")
    print("-" * 40)

    base_prompt=input("\nEnter a creative prompt (e.g., 'Write a short storyabout a robot learning to paint)")
    print("\nGenerating responses with different temperature settings...")
    print("\n--- LOW TEMPERATURE (0.1) - MORE DETERMINISTIC ---")
    low_temp_response=generate_response(base_prompt,temperature=0.1)
    print(low_temp_response)

    time.sleep(1)

    print("\n --- MEDIUM TEMPERATURE (0.5) - BALANCED ---")
    medium_temp_response=generate_response(base_prompt,temperature=0.5)
    print(medium_temp_response)

    time.sleep(1)

    print("\n --- HIGH TEMPERATURE (0.9) - MORE RANDOM/CREATIVE ---")
    high_temp_response=generate_response(base_prompt,temperature=0.9)
    print(high_temp_response)

    print("\n" + "-" * 40)
    print("PART 2: INSTRUCTION-BASED PROMPTS")
    print("-" * 40)

    print("\nNow, let's explore how specific instructions change the AI's output.")

    topic=input("\nChoose a topic (e.g., 'climate change','space exploration'):")
    instructions=[
        f"Summarize the key facts about {topic} in 3-4 sentences.",
        f"Explain {topic} as if I'm a 10-year-old child.",
        f"Write a pro/con list about {topic}.",
        f"Create a fictional news headline from the year 2050 about {topic}."
    ]
    for i,instruction in enumerate(instructions,1):
        print(f"\n--- INSTRUCTION {i}: {instruction} ---")
        response=generate_response(instruction,temperature=0.7)
        print(response)
        time.sleep(1)

    print("\n" + "-" * 40)
    print("PART 3: CREATING YOUR OWN INSTRUCTION-BASED PROMPTS")
    print("-" * 40)

    print("\n Now it's your turn1 Create an instruction-based prompt and test it with different temperatures.")

    custom_instruction=input("\nEnter your instruction-based prompt: ")

    try:
        custom_temp=float(input("\nSet a temperature (0.1 to 1.0):"))
        if custom_temp <0.1 or custom_temp> 1.0:
            print("Invalid temperature. Using default 0.7.")
            custom_temp=0.7
    except ValueError:
        print("Invalid input. Using default temperature 0.7.")
        custom_temp=0.7

    print(f"\n-- YOUR CUSTOM PROMPT WITH TEMPERATURE {custom_temp} ---")
    custom_response=generate_response(custom_instruction,temperature=custom_temp)
    print(custom_response)

    print("\n" + "-" * 40)
    print("REFLECTION QUESTIONS")
    print("-" * 40)
    print("1. How did changing the temperature affect the creativity and  variety in the AI's responses?")
    print("2. Which instruction-based prompt produced the most useful or interesting result? Why?")
    print("3. How might you combine specific instructions and temperature settings in real applications?")
    print("4. What patterens did you notice in how the AI responds to different types of instructions?")

    print("\n" + "-" * 40)
    print("CHALLENGE ACTIVITY")
    print("-" * 40)
    print("Try creating a 'chain' of prompts where:")
    print("1. First, ask the AI to generate content about a topic")
    print("2. Then, use an instruction-based prompt to modify or build upon that content")
    print("3. Experiment with different temperature settings at each step")
    print("\nFor example: Generate a story → Instruct AI to rewrite it in a specific style → Ask AI to create a sequel")

def genrate_streaming_response(prompt, temperature=0.5):
    try:
        client=genai.Client(api_key=config.GEMINI_API_KEY)
        contents=[
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(tex6=prompt)
                ],
            ),
        ]
        generate_content_config=types.GenerateContentConfig(
            temperature=temperature,
            response_mime_type="text/plain",
        )
        print("\nStreaming response (press Ctrl+c to stop):")
        for chunk in client.models.generate_content_stream(
            model="gemini-2.0-flash",
            contents=contents,
            config=generate_content_config,
        ):
            print(chunk.text, end="")
        print("\n")

    except Exception as e:
        print(f"\nError generating streaming response: {str(e)}")

if __name__ == "__main__":

    temperature_prompt_activity()


    # Optional: Demonstrate streaming responses

    print("\n" + "-" * 40)

    print("BONUS: STREAMING RESPONSES")

    print("-" * 40)

    print("Would you like to see a streaming response? (y/n)")

    choice = input("> ").lower().strip()

    if choice == 'y':

        prompt = input("\nEnter a prompt for streaming response: ")

        generate_streaming_response(prompt, temperature=0.7)