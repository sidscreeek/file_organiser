#pure structure 
from dataclasses import dataclass, field
from typing import Optional,Literal

Category = Literal[
    "Inventory",
    "Rent",
    "Utilities",
    "Salary",
    "Bank Charges",
    "Logistics",       # courier, diesel, delivery-related
    "Taxes",           # GST etc.
    "Manual Review",   # the "I'm not confident" escape hatch
]

@dataclass
class Transaction:
    id: int 
    description: str
    amount: float 

@dataclass
class ToolCall:
    tool_name: str
    tool_input: str
    tool_output: Optional[str] = None 

@dataclass 
class AgentState:
    transaction: Transaction
    history: list[ToolCall] = field(default_factory=list)
    status: Literal["in_progress", "done"] = "in_progress"
    final_category: Optional[Category] = None
    iterations: int = 0