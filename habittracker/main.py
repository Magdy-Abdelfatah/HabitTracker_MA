"""
Simple command-line Habit Tracker.

Profiles (separate JSON files):
- Real user  -> habits.json
- Demo user  -> demo_user_habits.json

Rules:
- Daily: one check-off per calendar day
- Weekly: one check-off per ISO week
- No future dates
"""
from habittracker.time_utils import parse_iso
from datetime import datetime
from habittracker.storage import init_storage, set_profile, load_habits
from habittracker.domain import add_habit, delete_habit, check_off, predefined_habits
from habittracker.analytics import (
    list_all_habits, list_by_periodicity,
    streak_summary_for, longest_daily_streak, longest_weekly_streak
)

def pause():
    """Wait for user to press ENTER before continuing."""
    input("\nPress ENTER to continue...")

def choose_profile():
    """Ask the user which profile to use."""
    print("\nChoose profile:")
    print("1) Real user")
    print("2) Demo user")
    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice == "1":
            set_profile("real")
            print("Using real user profile.")
            return
        elif choice == "2":
            set_profile("demo")
            print("Using demo user profile.")
            return
        else:
            print("Invalid input. Please try again.")

def choose_periodicity():
    """Ask if the habit is daily or weekly."""
    print("\nChoose habit type:")
    print("1) Daily")
    print("2) Weekly")

    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice == "1":
            return "daily"
        elif choice == "2":
            return "weekly"
        else:
            print("Invalid input. Please try again.")

def show_habits(habits):
    """Print all habits with index numbers."""
    if not habits:
        print("\nNo habits available.")
        return None

    print("\nYour habits:")
    for i in range(len(habits)):
        h = habits[i]
        print(f"{i + 1}) {h.name} ({h.periodicity})")
    print("0) Back")

    while True:
        choice = input("Choose number: ").strip()
        if choice == "0" or choice == "":
            return None
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(habits):
                return index
        print("Invalid input. Try again.")

def choose_check_date():
    """Ask when to check off (today or custom date)."""
    print("\nWhen do you want to check off this habit?")
    print("1) Today")
    print("2) Enter a custom date (YYYY-MM-DD)")
    print("0) Back")

    while True:
        choice = input("Enter choice: ").strip()
        if choice == "1":
            return datetime.now()
        elif choice == "2":
            date_str = input("Enter date (YYYY-MM-DD): ").strip()
            try:
                return parse_iso(date_str)
            except:
                print("Invalid format. Please try again.")
        elif choice == "0" or choice == "":
            return None
        else:
            print("Invalid input. Please try again.")


def run():
    """Run the main menu loop."""
    print("Welcome to Habit Tracker!")
    choose_profile()
    init_storage()

    while True:
        print("\n=== MAIN MENU ===")
        print("1) List all habits")
        print("2) List habits by type")
        print("3) Add a habit")
        print("4) Delete a habit")
        print("5) Check off a habit")
        print("6) Show habit details")
        print("7) Show longest streaks")
        print("0) Exit")

        choice = input("Enter choice: ").strip()

        # Exit program
        if choice == "0":
            print("Goodbye!")
            break

        # 1) List all habits
        elif choice == "1":
            habits = load_habits()
            pairs = list_all_habits(habits)
            print("\nAll habits:")
            if not pairs:
                print("No habits yet. Add one first.")
            else:
                for name, p in pairs:
                    print(f"- {name} ({p})")
            pause()

        # 2) List habits by periodicity
        elif choice == "2":
            period = choose_periodicity()
            habits = load_habits()
            filtered = list_by_periodicity(habits, period)
            print(f"\n{period.capitalize()} habits:")
            if not filtered:
                print("No habits of this type yet.")
            else:
                for h in filtered:
                    print(f"- {h.name}")
            pause()

        # 3) Add a new habit
        elif choice == "3":
            print("\nAdd a new habit")
            print("1) Create custom habit")
            print("2) Choose from predefined")
            print("0) Back")

            sub_choice = input("Enter choice: ").strip()

            if sub_choice == "1":
                name = input("Habit name: ").strip()
                if not name:
                    print("Habit name cannot be empty.")
                else:
                    period = choose_periodicity()
                    ok = add_habit(name, period)
                    print("Habit added." if ok else "Habit already exists.")
                pause()


            elif sub_choice == "2":
                while True:
                    presets = predefined_habits()
                    print("\nPredefined habits:")
                    for i in range(len(presets)):
                        ph = presets[i]
                        print(f"{i + 1}) {ph['name']} ({ph['periodicity']})")
                    print("0) Back")
                    pick = input("Choose number: ").strip()
                    if pick in ("", "0"):  # go back to previous menu
                        break
                    if pick.isdigit():
                        n = int(pick)
                        if 1 <= n <= len(presets):
                            ph = presets[n - 1]
                            ok = add_habit(ph["name"], ph["periodicity"])
                            print("Habit added." if ok else "Habit already exists.")
                        else:
                            print("Invalid number.")
                    else:
                        print("Invalid input. Try again.")
                    pause()

        # 4) Delete habit
        elif choice == "4":
            habits = load_habits()
            index = show_habits(habits)
            if index is not None:
                name = habits[index].name
                ok = delete_habit(name)
                print("Habit deleted." if ok else "Habit not found.")
            pause()

        # 5) Check off habit
        elif choice == "5":
            habits = load_habits()
            index = show_habits(habits)
            if index is None:
                pause()
                continue

            habit = habits[index]
            date = choose_check_date()
            if date is None:
                pause()
                continue

            ok, msg = check_off(habit.name, when_dt=date)
            print(msg)
            pause()

        # 6) Habit details
        elif choice == "6":
            habits = load_habits()
            index = show_habits(habits)
            if index is None:
                pause()
                continue

            habit = habits[index]
            summary = streak_summary_for(habit)
            created = parse_iso(habit.created_at)
            print(f"\nHabit: {habit.name}")
            print(f"Type: {habit.periodicity}")
            print(f"Created at: {created.strftime('%Y-%m-%d')}")
            print(f"Current streak: {summary['current_streak']} {summary['unit']}")
            print(f"Longest streak: {summary['longest_streak']} {summary['unit']}")
            print(f"Completions: {len(habit.completions)} times")
            pause()

        # 7) Show longest streaks
        elif choice == "7":
            habits = load_habits()
            d_name, d_val, d_unit = longest_daily_streak(habits)
            w_name, w_val, w_unit = longest_weekly_streak(habits)

            print("\nLongest streaks:")
            if d_name:
                print(f"- Daily:  {d_name} with {d_val} {d_unit}")
            else:
                print("- Daily:  no daily habits yet.")
            if w_name:
                print(f"- Weekly: {w_name} with {w_val} {w_unit}")
            else:
                print("- Weekly: no weekly habits yet.")
            pause()

        else:
            print("Invalid input. Please choose from the menu.")


if __name__ == "__main__":
    run()