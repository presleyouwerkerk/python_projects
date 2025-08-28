print("\nThe room is dark...")

name = input("\nWhat's your name?\n")
age = int(input("\nWhat's your age?\n"))

print(f"\nWelcome, {name}...\n\nIn 365 days you will be trapped here at age {age + 1}.")

choice = input("\nDo you light a candle? (yes/no)\n")

if choice.lower() == "yes":
    print("\nThe flame flickers... shadows dance across the walls.")
else:
    print("\nYou remain in darkness. Something moves nearby...")

door = input("\nDo you open the door? (yes/no)\n")

if door.lower() == "yes":
    print("\nThe door creaks open... a cold wind rushes in.\n")
else:
    print("\nYou lean against the door. Something scratches on the other side...\n")