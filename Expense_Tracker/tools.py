from data import transactions
from models import Category


def search_similar_transactions(description: str) -> str:
    words = [w for w in description.lower().split() if len(w) > 3]

    matches = []

    for t in transactions:
        past_desc = t["description"].lower()
        if any(word in past_desc for word in words):
            matches.append(t["description"])

    if not matches:
        return "No similar past transaction found"

    return "Similar Transactions found: " + "; ".join(matches)


def get_category_rules() -> str:
    categories = Category.__args__
    return "Valid categories: " + ", ".join(categories)


def flag_for_manual_review(reason: str) -> str:
    return f"Flagged for manual review. Reason: {reason}"