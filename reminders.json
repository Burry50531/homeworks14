def add_reminder(title, datetime_str, repeat="once", interval=1):
    reminders = load_reminders()
    reminders.append({
        "title": title,
        "datetime": datetime_str,
        "repeat": repeat,
        "interval": interval
    })
    save_reminders(reminders)

# Приклад
add_reminder("Зустріч з командою", "2025-05-29 17:00", repeat="weekly", interval=1)
