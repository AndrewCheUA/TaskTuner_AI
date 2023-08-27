habit_propositions = "Habit id: 1; Habit Title: Read for two hours each day; Habit Description: Set aside two hours each day to read one book per week. Start each day with a cup of coffee to help focus and stay motivated. Track progress and reward yourself for completing each book; Goal id: 8. Habit id: 2; Habit Title: Set aside a certain amount of money each month; Habit Description: Create a budget and set aside a certain amount of money each month to save for travel. Track progress and reward yourself for reaching milestones; Goal id: 9."


habit_sections = habit_propositions.split("Habit id: ")[1:]
new_habits = []
# Process each goal section
for habit_section in habit_sections:
    habit_info = habit_section.split("; ")
    goal = {"habit_id": int(habit_info[0]), "habit_title": habit_info[1].split(": ")[1],
            "habit_description": habit_info[2].split(": ")[1], "goal_id": int(habit_info[3].split(": ")[1].strip(". "))}
    new_habits.append(goal)
    print(goal)