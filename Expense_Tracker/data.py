transactions = [
    {"id": 1, "description": "Rent payment to landlord - Shop No 4", "amount": 25000},
    {"id": 2, "description": "BESCOM electricity bill", "amount": 3200},
    {"id": 3, "description": "Salary - Ramesh (Sales Staff)", "amount": 15000},
    {"id": 4, "description": "Rajesh Textiles - 15000", "amount": 15000},  # ambiguous
    {"id": 5, "description": "UPI/234521/Kumar Enterprises", "amount": 8500},  # ambiguous
    {"id": 6, "description": "Cash withdrawal", "amount": 5000},  # should flag
    {"id": 7, "description": "Woolen fabric purchase - winter stock", "amount": 42000},
    {"id": 8, "description": "Internet bill - Airtel", "amount": 999},
    {"id": 9, "description": "Diwali bonus - staff", "amount": 10000},
    {"id": 10, "description": "Misc transfer", "amount": 2000},  # should flag
    {"id": 11, "description": "Packaging material - poly bags", "amount": 1500},
    {"id": 12, "description": "Shop maintenance - electrician visit", "amount": 800},
    {"id": 13, "description": "GST payment Q3", "amount": 12000},
    {"id": 14, "description": "Kumar Enterprises payment", "amount": 6000},  # same vendor as #5, no UPI ref this time
    {"id": 15, "description": "Courier charges - online order returns", "amount": 450},
    {"id": 16, "description": "Advance to Rajesh Textiles", "amount": 5000},  # tests if agent links to #4
    {"id": 17, "description": "Bank charges - NEFT", "amount": 50},
    {"id": 18, "description": "Diesel - delivery van", "amount": 2500},
    {"id": 19, "description": "NEFT/998877/unknown", "amount": 3000},  # should flag
    {"id": 20, "description": "Winter jacket stock - wholesale", "amount": 60000},
]

#print(transactions)
#print(len(transactions))