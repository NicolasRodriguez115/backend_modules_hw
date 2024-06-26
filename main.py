import mood
while True:
    user_mood = input(f"How are you feeling today?\n1. Happy\n2. Sad\n3. Normal\n4. quit\n")
    if user_mood == "4":
        break
    mood.mood_response(user_mood)
