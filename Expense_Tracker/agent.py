import os
import time
import json
from dotenv import load_dotenv
from google import genai

from schema import AgentDecision
from prompts import SYSTEM_PROMPT, build_user_prompt
from models import AgentState, ToolCall
from tools import search_similar_transactions, get_category_rules, flag_for_manual_review

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

MAX_ITERATIONS = 5

# Maps the tool_name string Gemini gives us to the real Python function.
TOOL_FUNCTIONS = {
    "search_similar_transactions": search_similar_transactions,
    "get_category_rules": get_category_rules,
    "flag_for_manual_review": flag_for_manual_review,
}


def get_agent_decision(transaction, history) -> AgentDecision:
    """
    Sends the current transaction + history to Gemini, and gets back
    a decision that is GUARANTEED to match the AgentDecision schema.
    Retries automatically if we hit a rate limit (429).
    """
    user_prompt = build_user_prompt(transaction, history)

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=SYSTEM_PROMPT + "\n\n" + user_prompt,
                config={
                    "response_mime_type": "application/json",
                    "response_schema": AgentDecision,
                },
            )
            return response.parsed
        except Exception as e:
            if "RESOURCE_EXHAUSTED" in str(e) and attempt < max_retries - 1:
                print("  Rate limited, waiting 20s before retry...")
                time.sleep(20)
            else:
                raise


def run_agent(transaction) -> AgentState:
    state = AgentState(transaction=transaction)

    while state.status == "in_progress" and state.iterations < MAX_ITERATIONS:
        decision = get_agent_decision(state.transaction, state.history)

        if decision.action == "call_tool":
            tool_fn = TOOL_FUNCTIONS[decision.tool_name]
            result = tool_fn(decision.tool_input)

            state.history.append(ToolCall(
                tool_name=decision.tool_name,
                tool_input=decision.tool_input,
                tool_output=result,
            ))

        elif decision.action == "final_answer":
            state.final_category = decision.category
            state.status = "done"

        state.iterations += 1

    # Safety net: never leave a transaction unresolved.
    if state.status == "in_progress":
        state.final_category = "Manual Review"
        state.status = "done"

    return state