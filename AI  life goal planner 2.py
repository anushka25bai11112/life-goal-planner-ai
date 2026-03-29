import tkinter as tk
from tkinter import messagebox

goals_data = []

# Convert priority to weight
def get_weight(priority):
    return {"High": 3, "Medium": 2, "Low": 1}[priority]

# Add goal to list
def add_goal():
    name = goal_name.get()
    time = goal_time.get()
    priority = priority_var.get()

    if name == "" or time == "":
        messagebox.showwarning("Error", "Please fill all fields!")
        return

    try:
        time = float(time)
    except:
        messagebox.showwarning("Error", "Time must be a number!")
        return

    goals_data.append({
        "name": name,
        "time": time,
        "priority": priority
    })

    goal_listbox.insert(tk.END, f"{name} | {time} hrs | {priority}")

    goal_name.delete(0, tk.END)
    goal_time.delete(0, tk.END)

# Generate smart plan
def generate_plan():
    if not goals_data:
        messagebox.showwarning("Error", "Add at least one goal!")
        return

    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    weekly_plan = {day: [] for day in days}

    # Sort by priority (High first)
    sorted_goals = sorted(goals_data, key=lambda x: get_weight(x["priority"]), reverse=True)

    day_index = 0

    for goal in sorted_goals:
        sessions = max(1, int(goal["time"]))  # number of sessions

        for i in range(sessions):
            day = days[day_index % 7]
            weekly_plan[day].append(goal["name"])
            day_index += 1

    # Show output
    output.delete(1.0, tk.END)
    output.insert(tk.END, "📅 YOUR SMART WEEKLY PLAN\n\n")

    for day in days:
        if weekly_plan[day]:
            output.insert(tk.END, f"{day}: {', '.join(weekly_plan[day])}\n")
        else:
            output.insert(tk.END, f"{day}: Rest / Free Time 😌\n")

    # AI Suggestions
    output.insert(tk.END, "\n🤖 AI Suggestions:\n")

    for goal in goals_data:
        if goal["priority"] == "High":
            output.insert(tk.END, f"- {goal['name']}: Focus daily in short sessions.\n")
        elif goal["priority"] == "Medium":
            output.insert(tk.END, f"- {goal['name']}: Stay consistent.\n")
        else:
            output.insert(tk.END, f"- {goal['name']}: Flexible timing works fine.\n")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("AI Life Goal Planner Pro+ 🤖")
root.geometry("600x600")

tk.Label(root, text="AI Life Goal Planner (Advanced)", font=("Arial", 16, "bold")).pack(pady=10)

# Goal name
tk.Label(root, text="Goal Name:").pack()
goal_name = tk.Entry(root, width=40)
goal_name.pack(pady=5)

# Time input
tk.Label(root, text="Hours per week:").pack()
goal_time = tk.Entry(root, width=20)
goal_time.pack(pady=5)

# Priority
tk.Label(root, text="Priority:").pack()
priority_var = tk.StringVar(value="Medium")

tk.Radiobutton(root, text="High", variable=priority_var, value="High").pack()
tk.Radiobutton(root, text="Medium", variable=priority_var, value="Medium").pack()
tk.Radiobutton(root, text="Low", variable=priority_var, value="Low").pack()

# Add button
tk.Button(root, text="Add Goal ➕", command=add_goal).pack(pady=10)

# List of goals
goal_listbox = tk.Listbox(root, width=60, height=8)
goal_listbox.pack(pady=10)

tk.Button(root, text="Generate Smart Plan 🚀", command=generate_plan).pack(pady=10)

output = tk.Text(root, height=15, width=70)
output.pack(pady=10)

root.mainloop()