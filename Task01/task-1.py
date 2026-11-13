"""Task 1: Decisions with Many Boundaries (State Electricity Subsidy Eligibility)."""

def get_subsidy_buggy(units, has_ration_card, has_elderly_member):
    results = []
    if units <= 100:
        results.append("Full Subsidy")
    if 101 <= units <= 200 and has_ration_card:
        results.append("Partial Subsidy")
    if units > 200 and has_elderly_member:
        results.append("Age Exception Subsidy")
    return results if results else ["No Subsidy"]

def get_subsidy_correct(units, has_ration_card, has_elderly_member):
    if units <= 100:
        return "Full Subsidy"
    elif 101 <= units <= 200:
        return "Partial Subsidy" if has_ration_card else "No Subsidy"
    else:
        return "Age Exception Subsidy" if has_elderly_member else "No Subsidy"

if __name__ == "__main__":
    test_cases = [
        (90, False, False),
        (100, False, False),
        (101, True, False),
        (101, False, False),
        (200, True, False),
        (201, False, True),
        (201, False, False),
        (250, True, True),
    ]

    print("--- Buggy Independent If Statements (Can return multiple) ---")
    for units, rc, elderly in test_cases:
        res = get_subsidy_buggy(units, rc, elderly)
        print(f"Units: {units:3d} | Ration Card: {str(rc):5s} | Elderly: {str(elderly):5s} -> {res}")

    print("\n--- Corrected Mutually Exclusive if-elif-else Chain ---")
    for units, rc, elderly in test_cases:
        res = get_subsidy_correct(units, rc, elderly)
        print(f"Units: {units:3d} | Ration Card: {str(rc):5s} | Elderly: {str(elderly):5s} -> ['{res}']")
