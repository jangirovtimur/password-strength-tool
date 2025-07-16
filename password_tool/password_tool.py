import string
import random

def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])
    if length >= 12 and score == 4:
        return "strong password"
    elif length >= 8 and score == 3:
        return "medium password"
    else:
        return "weak password"

def suggest_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

def estimate_crack_time(password, guesses_per_second=100_000_000):
    possible_chars = 0
    if any(c.isupper() for c in password):
        possible_chars += len(string.ascii_uppercase)
    if any(c.islower() for c in password):
        possible_chars += len(string.ascii_lowercase)
    if any(c.isdigit() for c in password):
        possible_chars += len(string.digits)
    if any(c in string.punctuation for c in password):
        possible_chars += len(string.punctuation)

    total_combinations = possible_chars ** len(password)
    seconds = total_combinations / guesses_per_second
    return format_time(seconds)

def format_time(seconds):
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365

    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif minutes < 60:
        return f"{minutes:.2f} minutes"
    elif hours < 24:
        return f"{hours:.2f} hours"
    elif days < 365:
        return f"{days:.2f} days"
    else:
        return f"{years:.2f} years"

def main():
    print("Password Tool")
    print("1. Check password strength and crack time")
    print("2. Generate strong password")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        password = input("Enter your password: ")
        strength = check_password_strength(password)
        time_to_crack = estimate_crack_time(password)
        print(f"Your password is {strength}")
        print(f"Estimated crack time: {time_to_crack}")
    elif choice == "2":
        try:
            length = int(input("Enter password length (min 8): "))
            if length < 8:
                print("Your password is too short. Try again.")
            else:
                new_password = suggest_password(length)
                print(f"Your strong password is: {new_password}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
