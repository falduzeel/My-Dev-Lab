print("=== Game Level Checker ===")

score = int(input("Enter your score: "))

if score >= 1000:
    level = "Legendary"
    reward = "Diamond Badge"
elif score >= 750:
    level = "Master"
    reward = "Gold Badge"
elif score >= 500:
    level = "Expert"
    reward = "Silver Badge"
elif score >= 250:
    level = "Intermediate"
    reward = "Bronze Badge"
elif score >= 100:
    level = "Beginner"
    reward = "Starter Badge"
else:
    level = "Novice"
    reward = "No Badge"

print("\n=== Game Result ===")
print("Score:", score)
print("Level:", level)
print("Reward:", reward)
