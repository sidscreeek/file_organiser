from pydantic import BaseModel
from typing import Optional, Literal


class AgentDecision(BaseModel):
    action: Literal["call_tool", "final_answer"]

    # Only filled in when action == "call_tool"
    tool_name: Optional[Literal[
        "search_similar_transactions",
        "get_category_rules",
        "flag_for_manual_review"
    ]] = None
    tool_input: Optional[str] = None

    # Only filled in when action == "final_answer"
    category: Optional[Literal[
        "Inventory", "Rent", "Utilities", "Salary",
        "Bank Charges", "Logistics", "Taxes", "Manual Review"
    ]] = None