# history.py

history_log = []

def log_return(user, title, date):
    history_log.append({
        'user': user,
        'title': title,
        'date': date
    })
    print(f"Logged: {user} returned '{title}' on {date}")

def show_history():
    if not history_log:
        print("No history records found.")
    else:
        print("Library Return History:")
        for entry in history_log:
            print(f"{entry['user']} returned '{entry['title']}' on {entry['date']}")

# Example usage
log_return("Karabo", "The Hobbit", "2025-07-02")
log_return("Thandi", "1984", "2025-07-01")
show_history()

def add_number(num1, num2):
    return num1 + num2
