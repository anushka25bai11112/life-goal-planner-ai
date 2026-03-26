# AI Life Goal Planner
# Beginner-level project by a 1st-year BTech student
# Helps you plan your weekly goals in a simple way

import random

print("Hey! Welcome to your Life Goal Planner AI.")
print("I’ll help you organize your goals for the week in a simple plan.\n")

# Get goals from the user
goals = input("Type your goals for this week, separated by commas (like: coding, reading, exercise): ")
goal_list = [goal.strip() for goal in goals.split(",")]

# Ask how many hours per day they can dedicate
try:
    hours_per_day = float(input("How many hours per day can you spend on your goals? "))
except:
    hours_per_day = 2
    print("Hmm, I didn’t get that properly. I’ll just assume 2 hours per day.")

# Assign random difficulty to each goal
goal_difficulty = {}
for goal in goal_list:
    goal_difficulty[goal] = random.randint(1,5)

# Create a weekly plan
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
weekly_plan = {day: [] for day in days}

for goal, diff in goal_difficulty.items():
    # more difficult goals get more sessions
    sessions = max(1, int((diff/5)*7))
    chosen_days = random.sample(days, sessions)
    for day in chosen_days:
        weekly_plan[day].append(goal)

# Display the weekly plan
print("\nHere’s your weekly plan (just my suggestion, you can change it if you want):\n")
for day in days:
    tasks = weekly_plan[day]
    if tasks:
        print(f"{day}: " + ", ".join(tasks))
    else:
        print(f"{day}: Nothing scheduled, maybe take it easy or catch up on something")

# Provide some humanized tips
print("\nSome tips from me based on your goals:")
for goal, diff in goal_difficulty.items():
    if diff >= 4:
        print(f"- {goal.capitalize()}: This one is a bit tough, try breaking it into smaller parts during the week")
    elif diff == 3:
        print(f"- {goal.capitalize()}: Medium effort, try to stay consistent")
    else:
        print(f"- {goal.capitalize()}: Easy goal, should be quick to do, keep it up")

print("\nTry following this plan as much as you can, but don’t stress if things don’t go exactly as planned. Just keep going!")