def main():
    print("\nThe room is dark...")

    name = input("\nWhat's your name?\n").strip()
    age = int(input("\nWhat's your age?\n"))

    print(f"\nWelcome, {name}...\n\nIn 365 days you will be trapped here at age {age + 1}.")

    choice = input("\nDo you light a candle? (yes/no)\n").strip().lower()

    if choice == "yes":
        print("\nThe flame flickers... shadows dance across the walls.")
    elif choice == "no":
        print("\nYou remain in darkness. Something moves nearby...")
    else:
        print("\nI didn't understand that...")

    door = input("\nDo you open the door? (yes/no)\n").strip().lower()

    if door == "yes":
        print("\nThe door creaks open... a cold wind rushes in.")
    elif door == "no":
        print("\nYou lean against the door. Something scratches on the other side...")
    else:
        print("\nThe door doesn't respond to nonsense...")
main()