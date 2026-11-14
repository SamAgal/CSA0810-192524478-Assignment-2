"""Task 3: Engineer a Vehicle Registration Number Validator."""

def normalise(text):
    """Remove spaces and hyphens and convert to upper case using string methods."""
    cleaned = ""
    for char in text:
        if char != " " and char != "-":
            cleaned += char
    return cleaned.upper()

def is_valid(reg):
    """Valid form: 2 letters, 2 digits, 1 or 2 letters, 4 digits (e.g. TN09AB1234)."""
    length = len(reg)
    if length != 9 and length != 10:
        return False
    
    if length == 9:
        state = reg[0:2]
        district = reg[2:4]
        series = reg[4:5]
        digits = reg[5:9]
    else:
        state = reg[0:2]
        district = reg[2:4]
        series = reg[4:6]
        digits = reg[6:10]
        
    return state.isalpha() and district.isdigit() and series.isalpha() and digits.isdigit()

def format_receipt(reg):
    if not is_valid(reg):
        return reg
    if len(reg) == 9:
        return f"{reg[0:2]} {reg[2:4]} {reg[4:5]} {reg[5:9]}"
    else:
        return f"{reg[0:2]} {reg[2:4]} {reg[4:6]} {reg[6:10]}"

if __name__ == "__main__":
    test_numbers = [
        "tn 09 ab 1234",
        "KA-01-M-0007",
        "TN9AB1234",
        "TN 22 1234 AB",
        "MH12DE1433",
        "DL-3C-9999"
    ]

    for raw in test_numbers:
        reg = normalise(raw)
        valid = is_valid(reg)
        formatted = format_receipt(reg) if valid else "INVALID"
        print(f"{raw:15} -> {reg:11} {'valid' if valid else 'INVALID'} | Receipt: {formatted}")
