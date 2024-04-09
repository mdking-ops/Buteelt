import pandas as pd
from datetime import datetime, timedelta

grade_dates = [
    (datetime(1978, 9, 1), datetime(1979, 5,31)),
    (datetime(1979, 9, 1), datetime(1980, 5,31)),
    (datetime(1980, 9, 1), datetime(1981, 5,31))
]

grade_dates_middle = [
    (datetime(1981, 9, 1), datetime(1982, 5,31)),
    (datetime(1982, 9, 1), datetime(1983, 5,31)),
    (datetime(1983, 9, 1), datetime(1984, 5,31)),
    (datetime(1984, 9, 1), datetime(1985, 5,31)),
    (datetime(1985, 9, 1), datetime(1986,5,31))
]

grade_dates_high = [
    (datetime(1986, 9, 1), datetime(1987, 5,31)),
    (datetime(1987, 9, 1), datetime(1988, 5,31))
]

univercity_ix=[
    (datetime(1988, 9, 1), datetime(1989, 5,31)),
    (datetime(1989, 9, 1), datetime(1990, 5,31)),
    (datetime(1990, 9, 1), datetime(1991, 5,31)),
    (datetime(1991, 9, 1), datetime(1992, 5,31)),
    (datetime(1992 ,9,  1), datetime(1993, 5,31))
]

new_generation_grades = [
    (datetime(2006, 9, 1), datetime(2007, 5,31)),
    (datetime(2007, 9, 1), datetime(2008, 5,31)),
    (datetime(2008, 9, 1), datetime(2009, 5,31)),
    (datetime(2009, 9, 1), datetime(2010, 5,31)),
    (datetime(2010, 9, 1), datetime(2011, 5,31))
]

new_generation_high_grades = [
    (datetime(2011, 9, 1), datetime(2012, 5,31)),
    (datetime(2012, 9, 1), datetime(2013, 5,31)),
    (datetime(2013, 9, 1), datetime(2014, 5,31)),
    (datetime(2014, 9, 1), datetime(2015, 5,31)),
    (datetime(2015, 9, 1), datetime(2016, 5,31)),
    (datetime(2016, 9, 1), datetime(2017, 5,31)),
    (datetime(2017, 9, 1), datetime(2018, 5,31)),
]

new_univer=[
    (datetime(2018, 9, 1), datetime(2019, 5,31)),
    (datetime(2019, 9, 1), datetime(2020, 5,31)),
    (datetime(2020, 9, 1), datetime(2021, 5,31)),
    (datetime(2021, 9, 1), datetime(2022, 5,31)),
]

grade_data = []
uni_data = []
new_grade_data = []
new_uni_data = []


def calculate_full_weeks_and_extra_days(year):
    start_date = datetime(year, 9, 1)  
    end_date = datetime(year + 1, 6, 1)  
    
    while start_date.weekday() != 0:
        start_date += timedelta(days=1)

    last_day = end_date - timedelta(days=1)
    while last_day.weekday() != 6:
        last_day -= timedelta(days=1)


    full_weeks1 = (end_date-start_date).days // 7 

    extra_days_before = (start_date - datetime(year, 9, 1)).days

    extra_days_after = (datetime(year + 1, 6, 1) - last_day - timedelta(days=1)).days
    
    if extra_days_before == 0 :
        full_weeks=full_weeks1
    else:
     full_weeks=full_weeks1-1

    return full_weeks, extra_days_before, extra_days_after

def calculate_studied_time(grade_dates, hours_per_day, start_index, end_index):
    for i, (start_date, end_date) in enumerate(grade_dates, start=start_index):
        date_range = pd.date_range(start=start_date, end=end_date)
        working_days = len(date_range) - sum(1 for day in date_range if day.dayofweek >= 6)
        total_studied_minutes = working_days * hours_per_day * 60

        real, extra_days_before, extra_days_after = calculate_full_weeks_and_extra_days(start_date.year)
        
        grade_data.append({
            'Анги': f'{i} Анги',
            'Эхлэх жил': start_date.strftime('%Y-%m-%d'),
            'Төгсөх жил': end_date.strftime('%Y-%m-%d'),
            'Сурсан цаг (минут)': total_studied_minutes,
            'Ажлын өдөр': working_days,
            #'Нийт өдөр': len(date_range),
            'Бүтэн долоо хоног': real,
             'Сонирхосон хичээлийн цаг': real * 4,
            #'1нээс эхний даваа хүртэл': extra_days_before,
            #'сүүлийн нямаас 1-н хүртэл': extra_days_after
        })
        
    return pd.DataFrame(grade_data)[start_index-1:end_index].sum()


def calculate_studied_time_univercity(grade_dates, hours_per_day, start_index, end_index): 
    for i, (start_date, end_date) in enumerate(grade_dates, start=start_index):
        date_range = pd.date_range(start=start_date, end=end_date)
        working_days = len(date_range) - sum(1 for day in date_range if day.dayofweek >= 6)
        total_studied_minutes = working_days * hours_per_day * 60
        
     
        real, extra_days_before, extra_days_after = calculate_full_weeks_and_extra_days(start_date.year)
        
        uni_data.append({
            'Курс': f'{i} Курс',
            'Эхлэх жил': start_date.strftime('%Y-%m-%d'),
            'Төгсөх жил': end_date.strftime('%Y-%m-%d'),
            'Сурсан цаг (минут)': total_studied_minutes,
            'Ажлын өдөр': working_days,
            'Нийт өдөр': len(date_range),
            'Бүтэн долоо хоног': real,
            'Дадлагийн эзлэх хувь': 48 / working_days
        })

def calculate_new_studied_time(grade_dates, hours_per_day, start_index, end_index):
    for i, (start_date, end_date) in enumerate(grade_dates, start=start_index):
        date_range = pd.date_range(start=start_date, end=end_date)
        working_days = len(date_range) - sum(1 for day in date_range if day.dayofweek >= 5)
        total_studied_minutes = working_days * hours_per_day * 60

        real, extra_days_before, extra_days_after = calculate_full_weeks_and_extra_days(start_date.year)
        
        new_grade_data.append({
            'Анги': f'{i} Анги',
            'Эхлэх жил': start_date.strftime('%Y-%m-%d'),
            'Төгсөх жил': end_date.strftime('%Y-%m-%d'),
            'Сурсан цаг (минут)': total_studied_minutes,
            'Ажлын өдөр': working_days,
            'Нийт өдөр': len(date_range),
            'Бүтэн долоо хоног': real,
        #'Сонирхосон хичээлийн цаг': real * 4,
            '1нээс эхний даваа хүртэл': extra_days_before,
            'сүүлийн нямаас 1-н хүртэл': extra_days_after
        })

def calculate_new_studied_time_univercity(grade_dates, hours_per_day, start_index, end_index): 
    for i, (start_date, end_date) in enumerate(grade_dates, start=start_index):
        date_range = pd.date_range(start=start_date, end=end_date)
        working_days = len(date_range) - sum(1 for day in date_range if day.dayofweek >= 5)
        total_studied_minutes = working_days * hours_per_day * 60
        

        real, extra_days_before, extra_days_after = calculate_full_weeks_and_extra_days(start_date.year)
        
        new_uni_data.append({
            'Курс': f'{i} Курс',
            'Эхлэх жил': start_date.strftime('%Y-%m-%d'),
            'Төгсөх жил': end_date.strftime('%Y-%m-%d'),
            'Сурсан цаг (минут)': total_studied_minutes,
            'Ажлын өдөр': working_days,
            'Нийт өдөр': len(date_range),
            'Бүтэн долоо хоног': real,
            'Дадлагийн эзлэх хувь': 40 / working_days
        })

grouped_grades = {
    '1-3 grades': calculate_studied_time(grade_dates, 3, 1, 3),
    '4-8 grades': calculate_studied_time(grade_dates_middle, 4.15, 4, 8),
    '9-10 grades': calculate_studied_time(grade_dates_high, 4.5, 9, 10)
}

hours_per_day_university = 4.5
calculate_studied_time_univercity(univercity_ix, hours_per_day_university, 1, 5)


calculate_new_studied_time(new_generation_grades, 2, 1, 5)


calculate_new_studied_time_univercity(new_univer, hours_per_day_university, 1, 4)

new_grouped_grades = {
    '1-5 grades': calculate_new_studied_time(new_generation_grades, 2, 1, 5),
    '6-12 grades': calculate_new_studied_time(new_generation_high_grades, 3.5, 6, 12),
}

print("1978-1988 оны нийт сурсан хугацаа:", pd.DataFrame(grade_data)['Сурсан цаг (минут)'].sum(), "мин")
print("1988 онд Их сургуульд орсон:", pd.DataFrame(uni_data)['Сурсан цаг (минут)'].sum(), "мин")
print("2006-2018 оны нийт сурсан хугацаа:", pd.DataFrame(new_grade_data)['Сурсан цаг (минут)'].sum(), "мин")
print("2018 онд Их сургуульд орсон:", pd.DataFrame(new_uni_data)['Сурсан цаг (минут)'].sum(), "мин")


print("1978-1988 оны нийт сурсан хугацаа:")
print(pd.DataFrame(grade_data))
print("\n")

print("1988 онд Их сургуульд орсон:")
print(pd.DataFrame(uni_data))
print("\n")

print("2006-2018 оны нийт сурсан хугацаа:")
print(pd.DataFrame(new_grade_data))
print("\n")

print("2018 онд Их сургуульд орсон:")
print(pd.DataFrame(new_uni_data))


#03:50