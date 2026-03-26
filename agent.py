import os
from google import genai
from google.genai import types

def run_intelligence_agent(topic: str):
    # Initialize client. This will fail if GEMINI_API_KEY is not in your environment.
    client = genai.Client()
    
    system_instruction = """
    You are an expert geopolitical intelligence agent. Your task is to provide a comprehensive, unbiased timeline and current status of the requested topic.
    
    Strict Execution Rules:
    1. Use your search tool to retrieve the most up-to-date information.
    2. Separate your output into exactly two sections: 'Historical Context' (the root of the issue) and 'Current Events' (what is happening right now).
    3. Ground your claims in specific, cited events and dates.
    4. Do not provide commentary, opinions, or speculative analysis.
    """

    print(f"Deploying agent to investigate: {topic}...\n")

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=topic,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                tools=[{"google_search": {}}], 
                temperature=0.2, 
            )
        )

        print("=== Intelligence Report ===")
        print(response.text)
        
    except Exception as e:
        print(f"CRITICAL ERROR: Agent execution failed. Details: {e}")

if __name__ == "__main__":
    if not os.environ.get("GEMINI_API_KEY"):
        print("CRITICAL ERROR: GEMINI_API_KEY environment variable is missing. Set it before running.")
    else:
        print("\n--- AI Intelligence Agent Initialized ---")
        print("Type 'exit' to quit.")
        
        while True:
            # 1. Ask the user for the topic
            target_topic = input("\nEnter the news topic or event you want me to investigate: ")
            
            # 2. Allow the user to exit gracefully
            if target_topic.lower() == 'exit':
                print("Shutting down agent.")
                break
                
            # 3. Prevent empty inputs from crashing the agent
            if not target_topic.strip():
                print("Error: You must enter a valid topic.")
                continue
                
            # 4. Run the agent with the user's input
            run_intelligence_agent(target_topic)