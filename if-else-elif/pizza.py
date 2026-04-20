print("🍕 Pizza Topping Advisor! 🍕")
topping = input("What's your favorite pizza topping? ").lower()

if topping in ["pepperoni", "cheese", "sausage"]:
    print("🔥 Classic choice! Everyone loves that!")
elif topping in ["pineapple", "anchovies"]:
    print("😲 Brave adventurer! Not everyone's cup of tea!")
elif topping == "mushroom":
    print("🍄 Healthy and tasty! Good pick!")
elif topping == "nothing":
    print("😄 Plain cheese pizza fan? Respect!")
else:
    print(f"🤔 {topping.title()}? Sounds exotic! Let's try it!")