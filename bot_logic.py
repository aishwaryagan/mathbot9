import anthropic
import os
from prompts import build_system_prompt

def get_client():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not set.")
    return anthropic.Anthropic(api_key=api_key)

def chat_with_mathbot(conversation_history: list, active_strand: str = None) -> str:
    """
    Send conversation to Claude and get MathBot9's response.
    
    Args:
        conversation_history: List of {"role": "user"/"assistant", "content": "..."} dicts
        active_strand: Optional strand filter (e.g., "Algebra", "Data")
    
    Returns:
        str: MathBot9's response text
    """
    try:
        client = get_client()
        system_prompt = build_system_prompt(active_strand)

        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1024,
            system=system_prompt,
            messages=conversation_history
        )
        return response.content[0].text

    except anthropic.AuthenticationError:
        return "⚠️ **API Key Error:** Please check your ANTHROPIC_API_KEY. Make sure it's set correctly in your `.env` file or environment variables."
    except anthropic.RateLimitError:
        return "⏳ **Too many requests!** MathBot9 needs a quick breather. Please wait a moment and try again!"
    except anthropic.APIConnectionError:
        return "🌐 **Connection Error:** Can't reach the MathBot9 servers right now. Check your internet connection and try again."
    except Exception as e:
        return f"😬 **Oops!** Something unexpected happened: {str(e)}. Please try again!"


def get_hint(problem: str, active_strand: str = None) -> str:
    """Get a hint for a specific math problem without solving it."""
    hint_messages = [
        {
            "role": "user",
            "content": f"Give me ONE small hint to get started on this problem, but don't solve it: {problem}"
        }
    ]
    return chat_with_mathbot(hint_messages, active_strand)


def check_answer(problem: str, student_answer: str, active_strand: str = None) -> str:
    """Check if a student's answer is correct and provide feedback."""
    check_messages = [
        {
            "role": "user",
            "content": f"Problem: {problem}\nMy answer: {student_answer}\n\nIs my answer correct? Give me detailed feedback using Growing Success language."
        }
    ]
    return chat_with_mathbot(check_messages, active_strand)
