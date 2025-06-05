import openai
import os
import time

# Set your OpenAI API key as an environment variable for security
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_llm(prompt, system="You are an autonomous AI agent."):
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500,
        temperature=0.4
    )
    return response['choices'][0]['message']['content'].strip()

def plan_steps(goal):
    prompt = f"Given the goal: '{goal}', break it down into 3-5 clear, actionable steps."
    steps = ask_llm(prompt)
    return steps

def execute_step(step):
    # Here, we simulate execution by asking the LLM to suggest an outcome.
    # For advanced agents, integrate with tools/APIs for real execution.
    prompt = f"Execute the following step, and describe the result: {step}"
    result = ask_llm(prompt)
    return result

def main():
    print("=== Agentic AI App ===")
    goal = input("What is your goal? ")
    
    print("\nPlanning steps...")
    steps = plan_steps(goal)
    print("\nProposed Steps:\n", steps)
    step_list = [s for s in steps.split('\n') if s.strip() and any(c.isalpha() for c in s)]
    
    print("\nExecuting steps...\n")
    for idx, step in enumerate(step_list, 1):
        print(f"Step {idx}: {step}")
        result = execute_step(step)
        print("Result:", result)
        print("-" * 40)
        time.sleep(1)  # Simulate real-world delay
    
    print("\nAll steps completed. Would you like a summary? (y/n)")
    if input().lower().startswith('y'):
        summary_prompt = f"The user wanted: '{goal}'. Here are the steps I took: {steps}. Summarize the outcomes."
        summary = ask_llm(summary_prompt)
        print("\nSummary:\n", summary)

if __name__ == "__main__":
    main()
