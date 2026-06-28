import json
import sys
from datetime import datetime

if len(sys.argv) >= 2:
    input_file = sys.argv[1]
else:
    input_file = "app.log"
important_file = "important.log"
summary_file = "important_summary.json"
script_log_file = "script.log"


def make_important_log():
    important_lines = []

    with open(input_file, "r") as file:
        for line in file:
            if "WARNING" in line or "ERROR" in line:
                important_lines.append(line)

    with open(important_file, "w") as file:
        for line in important_lines:
            file.write(line)


def count_important_logs():
    warning_count = 0
    error_count = 0

    with open(important_file, "r") as file:
        for line in file:
            if "WARNING" in line:
                warning_count += 1
            elif "ERROR" in line:
                error_count += 1

    total_important_count = warning_count + error_count

    if error_count > 0:
        status = "NG"
    else:
        status = "OK"

    summary_data = {
        "warning_count": warning_count,
        "error_count": error_count,
        "total_important_count": total_important_count,
        "status": status
    }

    return summary_data


def save_important_summary(summary_data):
    with open(summary_file, "w") as file:
        json.dump(summary_data, file, indent=4)


def write_script_log():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(script_log_file, "a") as file:
        file.write(f"{now} monitor.py executed\n")


def main():
    make_important_log()
    summary_data = count_important_logs()
    save_important_summary(summary_data)
    write_script_log()

    print("Log monitoring completed.")
    print(f"WARNING: {summary_data['warning_count']}")
    print(f"ERROR: {summary_data['error_count']}")
    print(f"STATUS: {summary_data['status']}")


if __name__ == "__main__":
    main()
