import time
from data import transactions
from models import Transaction
from agent import run_agent

print(f"{'ID':<4}{'Description':<45}{'Category':<18}{'Iter':<6}{'Tools Used'}")
print("-" * 100)

for t_data in transactions:
    t = Transaction(id=t_data["id"], description=t_data["description"], amount=t_data["amount"])
    result = run_agent(t)

    tools_used = ", ".join(call.tool_name for call in result.history) or "none"

    print(f"{result.transaction.id:<4}"
          f"{result.transaction.description[:43]:<45}"
          f"{str(result.final_category):<18}"
          f"{result.iterations:<6}"
          f"{tools_used}")

    time.sleep(13)  # stay under free-tier rate limit