from datetime import datetime, timedelta

def calculate_study_time(start_date, end_date, minutes_per_day):
   
    start = datetime.strptime(start_date, "%Y.%m.%d")
    end = datetime.strptime(end_date, "%Y.%m.%d")


    total_study_minutes = 0

   
    current_date = start
    while current_date <= end:
        
        if current_date.weekday() != 6: 
            total_study_minutes += minutes_per_day

       
        current_date += timedelta(days=1)

    return total_study_minutes

if __name__ == "__main__":
    total_minutes_all_periods = 0
    while True:
        total_minutes_current_grade = 0
        start_date = input("Enter start date (YYYY.MM.DD) (type 'exit' to finish): ")
        if start_date.lower() == "exit":
            break
        end_date = input("Enter end date (YYYY.MM.DD): ")
        hours_per_day_input = input("Enter hours per day (hh.mm): ")

    
        hours, minutes = map(int, hours_per_day_input.split('.'))
        total_minutes_per_day = hours * 60 + minutes

        total_minutes_current_grade = calculate_study_time(start_date, end_date, total_minutes_per_day)
        
        total_hours = total_minutes_current_grade // 60
        total_minutes = total_minutes_current_grade % 60
        print("Total studied time for this period: {} hours {} minutes".format(total_hours, total_minutes))

        
        total_minutes_all_periods += total_minutes_current_grade

    
    total_hours_all_periods = total_minutes_all_periods // 60
    total_minutes_all_periods = total_minutes_all_periods % 60
    print("Total studied time for all periods: {} hours {} minutes".format(total_hours_all_periods, total_minutes_all_periods))