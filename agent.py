"""
ABAG AI Business Advisor Agent
American Business Advisory Group
"""

import os
from pathlib import Path

from openai import OpenAI


SYSTEM_PROMPT_PATH = Path(__file__).parent / "system_prompt.txt"


def load_system_prompt() -> str:
    """Load the system prompt from file."""
    return SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")


def create_client() -> OpenAI:
    """Create and return an OpenAI client."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is not set. "
            "Please set it before running the agent."
        )
    return OpenAI(api_key=api_key)


def run_chat(model: str = "gpt-4o") -> None:
    """Run an interactive chat session with the ABAG advisor agent."""
    client = create_client()
    system_prompt = load_system_prompt()
    conversation_history = []

    print("ABAG AI Business Advisor")
    print("American Business Advisory Group")
    print("=" * 50)
    print("Helping U.S. companies expand into Italy and Europe.")
    print("Type 'exit' or 'quit' to end the session.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nEnding session. Goodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("Ending session. Goodbye!")
            break

        conversation_history.append({"role": "user", "content": user_input})

        messages = [{"role": "system", "content": system_prompt}] + conversation_history

        response = client.chat.completions.create(
            model=model,
            messages=messages,
        )

        assistant_message = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": assistant_message})

        print(f"\nABAG Advisor: {assistant_message}\n")


def get_single_response(user_message: str, model: str = "gpt-4o") -> str:
    """
    Get a single response from the ABAG advisor agent.

    Args:
        user_message: The user's message or question.
        model: The OpenAI model to use.

    Returns:
        The assistant's response as a string.
    """
    client = create_client()
    system_prompt = load_system_prompt()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message},
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    run_chat()
