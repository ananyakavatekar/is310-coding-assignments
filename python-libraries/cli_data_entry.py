from rich.console import Console
from rich.table import Table
import csv
import os

console = Console()

def show_example_data():
    console.print("Here is some initial data:", style="bold cyan")

    table = Table(title="Women Influencing Politics in U.S. History")
    table.add_column("Name", style="magenta")
    table.add_column("Time Period", style="cyan")
    table.add_column("Political Role / Influence", style="green")
    table.add_column("Major Contribution", style="yellow")

    table.add_row(
        "Susan B. Anthony",
        "1800s",
        "Suffrage activist",
        "Helped lead the women's suffrage movement"
    )
    table.add_row(
        "Shirley Chisholm",
        "1900s",
        "Congresswoman / presidential candidate",
        "First Black woman elected to Congress"
    )
    table.add_row(
        "Kamala Harris",
        "2000s-present",
        "Vice President",
        "First woman Vice President of the United States"
    )

    console.print(table)

def get_entry():
    name = console.input("Enter the person's name: ")
    time_period = console.input("Enter the time period: ")
    political_role = console.input("Enter the political role or influence: ")
    major_contribution = console.input("Enter the major contribution: ")

    return {
        "name": name,
        "time_period": time_period,
        "political_role_or_influence": political_role,
        "major_contribution": major_contribution
    }

def confirm_entry(entry):
    console.print("\nYou entered:", style="bold yellow")
    console.print(f"Name: {entry['name']}")
    console.print(f"Time Period: {entry['time_period']}")
    console.print(f"Political Role / Influence: {entry['political_role_or_influence']}")
    console.print(f"Major Contribution: {entry['major_contribution']}")

    confirm = console.input("Is this correct? (yes/no): ").strip().lower()
    return confirm == "yes"

def save_to_csv(entries, filename="women_politics_data.csv"):
    full_path = os.path.abspath(filename)

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "name",
                "time_period",
                "political_role_or_influence",
                "major_contribution"
            ]
        )
        writer.writeheader()
        writer.writerows(entries)

    return full_path

def main():
    show_example_data()
    console.print(
        "\nNow you can enter your own data about women influencing politics in U.S. history.",
        style="bold cyan"
    )

    confirmed_entries = []

    while True:
        entry = get_entry()

        while not confirm_entry(entry):
            console.print("Please re-enter the data.\n", style="bold red")
            entry = get_entry()

        confirmed_entries.append(entry)

        another = console.input("Do you want to add another entry? (yes/no): ").strip().lower()
        if another != "yes":
            break

    file_path = save_to_csv(confirmed_entries)
    console.print(f"\nData saved successfully to: {file_path}", style="bold green")

if __name__ == "__main__":
    main()
