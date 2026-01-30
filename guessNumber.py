import random

best_score = None

print("=== Number Guessing Game ===")

while True:
    print("\nChoose difficulty:")
    print("1. Easy (1–10)")
    print("2. Medium (1–50)")
    print("3. Hard (1–100)")

    choice = input("Your choice: ").strip()

    if choice == '1':
        max_num = 10
    elif choice == '2':
        max_num = 50
    elif choice == '3':
        max_num = 100
    else:
        print("Invalid choice. Easy mode selected.")
        max_num = 10

    secret = random.randint(1, max_num)
    attempts = 0

    print(f"\nI picked a number between 1 and {max_num}. Start guessing!")

    while True:
        guess = input("Your guess: ").strip()

        if not guess.isdigit():
            print("Invalid input. Enter a number.")
            continue

        guess = int(guess)

        if guess < 1 or guess > max_num:
            print(f"Invalid input. Enter a number between 1 and {max_num}.")
            continue  # does NOT count as attempt

        attempts += 1

        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"🎉 Correct! Attempts: {attempts}")
            break

    if best_score is None or attempts < best_score:
        best_score = attempts
        print("⭐ New best score!")

    print(f"Best score so far: {best_score}")

    if input("\nPlay again? (yes/no): ").strip().lower() != 'yes':
        print("Thanks for playing 👋")
        break
