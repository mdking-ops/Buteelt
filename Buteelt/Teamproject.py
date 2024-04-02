from datetime import datetime, timedelta

def calculate_study_time(start_date, end_date, hours_per_day):
    # Convert string inputs to datetime objects
    start = datetime.strptime(start_date, "%Y.%m.%d")
    end = datetime.strptime(end_date, "%Y.%m.%d")

    # Initialize study time counter
    total_study_hours = 0

    # Iterate through each day
    current_date = start
    while current_date <= end:
        # Check if the current day is not Sunday
        if current_date.weekday() != 6:  # 6 represents Sunday
            total_study_hours += hours_per_day

        # Move to the next day
        current_date += timedelta(days=1)

    return total_study_hours

if __name__ == "__main__":
    start_date = input(" Эхлэх Он сараа оруулна уу(Жил.Сар.Өдөр): ")
    end_date = input(" Төгсөх Он сараа оруулна уу(Жил.Сар.Өдөр): ")
    hours_per_day = float(input("Өдөрт хэдэн цаг сурах вэ?: "))

    total_study_hours = calculate_study_time(start_date, end_date, hours_per_day)

    print("Нийт сурсан цаг(Бүтэн сайныг оруулалгүйгээр): {:.2f} цаг".format(total_study_hours))
from datetime import datetime, timedelta

def calculate_study_time(start_date, end_date, hours_per_day):
    # Convert string inputs to datetime objects
    start = datetime.strptime(start_date, "%Y.%m.%d")
    end = datetime.strptime(end_date, "%Y.%m.%d")

    # Initialize study time counter
    total_study_hours = 0

    # Iterate through each day
    current_date = start
    while current_date <= end:
        # Check if the current day is not Sunday
        if current_date.weekday() != 6:  # 6 represents Sunday
            total_study_hours += hours_per_day

        # Move to the next day
        current_date += timedelta(days=1)

    return total_study_hours

if __name__ == "__main__":
    start_date = input(" Эхлэх Он сараа оруулна уу(Жил.Сар.Өдөр): ")
    end_date = input(" Төгсөх Он сараа оруулна уу(Жил.Сар.Өдөр): ")
    hours_per_day = float(input("Өдөрт хэдэн цаг сурах вэ?: "))

    total_study_hours = calculate_study_time(start_date, end_date, hours_per_day)

    print("Нийт сурсан цаг(Бүтэн сайныг оруулалгүйгээр): {:.2f} цаг".format(total_study_hours))