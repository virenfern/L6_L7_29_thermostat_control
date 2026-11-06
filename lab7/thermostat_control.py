
def parse_setpoint(text):
    if not isinstance(text, str) or len(text) < 2:
        return None

    unit = text[-1].upper()

    if unit not in ('C', 'F'):
        return None

    try:
        value = float(text[:-1])
    except ValueError:
        return None

    if unit == 'F':
        value = (value - 32) * 5 / 9

    return round(value, 1)


def average_temperature(readings_csv):
    if not isinstance(readings_csv, str) or not readings_csv.strip():
        return None

    try:
        values = [float(r.strip()) for r in readings_csv.split(',')]

        if not values:
            return None

        return sum(values) / len(values)

    except ValueError:
        return None


def schedule_slot(time_text):
    if not isinstance(time_text, str):
        return None

    try:
        parts = time_text.split(':')

        if len(parts) != 2:
            return None

        hour_text, minute_text = parts

        if len(hour_text) != 2 or len(minute_text) != 2:
            return None

        hour = int(hour_text)
        minute = int(minute_text)

        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            return None

    except ValueError:
        return None

    if hour < 6:
        return 'night'

    return 'day'


def main():
    print("==== Running parse_setpoint ====")
    user_input = input("Enter a setpoint (e.g. 21.5C or 70F): ")
    result = parse_setpoint(user_input)
    print("Setpoint in Celsius:", result)

    print("\n==== Running average_temperature ====")
    user_input = input(
        "Enter sensor readings as CSV (e.g. 20.5,21,22.5): "
    )
    result = average_temperature(user_input)
    print("Average Temperature:", result)

    print("\n==== Running schedule_slot ====")
    user_input = input("Enter a time as HH:MM (e.g. 07:30): ")
    result = schedule_slot(user_input)
    print("Schedule Slot:", result)


if __name__ == "__main__":
    main()
