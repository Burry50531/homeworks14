import time
import json
from datetime import datetime, timedelta

def load_reminders(file="reminders.json"):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_reminders(reminders, file="reminders.json"):
    with open(file, "w") as f:
        json.dump(reminders, f, indent=4)

def check_reminders(reminders):
    now = datetime.now()
    updated = []
    for r in reminders:
        event_time = datetime.strptime(r["datetime"], "%Y-%m-%d %H:%M")
        if now >= event_time:
            print(f"🔔 Reminder: {r['title']}")

            # Повторювані події
            if r["repeat"] != "once":
                delta = get_timedelta(r["repeat"], r.get("interval", 1))
                r["datetime"] = (event_time + delta).strftime("%Y-%m-%d %H:%M")
                updated.append(r)
        else:
            updated.append(r)
    return updated

def get_timedelta(freq, interval):
    if freq == "hourly":
        return timedelta(hours=interval)
    elif freq == "daily":
        return timedelta(days=interval)
    elif freq == "weekly":
        return timedelta(weeks=interval)
    elif freq == "monthly":
        return timedelta(days=30 * interval)  # спрощено
    return timedelta(0)

if __name__ == "__main__":
    while True:
        reminders = load_reminders()
        updated_reminders = check_reminders(reminders)
        save_reminders(updated_reminders)
        time.sleep(60)  # перевіряє щохвилини
