"""Task 2: Loops that Count Attempts (OTP Verification at Bank Kiosk)."""

def run_kiosk_simulations():
    print("--- Bank Kiosk OTP Simulation ---")
    correct_otp = "4829"
    user_inputs = ["", "1234", "4829"]
    
    attempts = 0
    locked = True
    
    print("Simulation 1: While loop verification")
    for entry in user_inputs:
        if entry == "":
            print("Blank entry detected. Does not count as an attempt. (pass used)")
            pass
            continue
        
        attempts += 1
        print(f"Attempt {attempts}: entered '{entry}'")
        if entry == correct_otp:
            print("OTP Correct! Access granted. (break used)")
            locked = False
            break
        else:
            print("Incorrect OTP.")
    else:
        if locked:
            print("Account locked for 30 minutes due to failed attempts! (loop-else triggered)")

if __name__ == "__main__":
    run_kiosk_simulations()
