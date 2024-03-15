import csv
import sys


def convert_todoist_to_ticktick(todoist_file, list_name):
    ticktick_template = """
"Date: {{date}}+0000"
"Version: 3.0"
"Status: 
0 Normal
0 Completed
0 Archived"
"List Name","Title","Content","Is Checklist","Start Date","Due Date","Reminder","Repeat","Priority","Status","Completed Time","Order","Timezone","Is All Day"\n
"""
    # ticktick_template = '"List Name","Title","Content","Is Checklist","Start Date","Due Date","Reminder","Repeat","Priority","Status","Completed Time","Order","Timezone","Is All Day"\n'

    with open(todoist_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) > 1 and row[0] == "task":
                title = row[1]
                content = row[2]
                ticktick_template += f'"{list_name}","{title}","{content}",False,,,,,,,Pending,,,America/New_York,\n'

    return ticktick_template


def save_to_csv(data, output_file):
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        csvfile.write(data)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py todoist.csv ticktick.csv")
        sys.exit(1)

    todoist_file = sys.argv[1]
    ticktick_list_name = sys.argv[2]

    ticktick_tasks = convert_todoist_to_ticktick(todoist_file, ticktick_list_name)
    save_to_csv(ticktick_tasks, "ticktick_to_import.csv")
    print("Tasks converted and saved to ticktick_to_import.csv")
