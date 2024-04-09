import pandas as pd
from datetime import datetime

# Define the start and end dates for each grade
grade_dates = [
    (datetime(1978, 9, 1), datetime(1979, 5, 31)),
    (datetime(1979, 9, 1), datetime(1980, 5, 31)),
    (datetime(1980, 9, 1), datetime(1981, 5, 31))
]

grade_dates_middle = [
    (datetime(1981, 9, 1), datetime(1982, 5, 31)),
    (datetime(1982, 9, 1), datetime(1983, 5, 31)),
    (datetime(1983, 9, 1), datetime(1984, 5, 31)),
    (datetime(1984, 9, 1), datetime(1985, 5, 31)),
    (datetime(1985, 9, 1), datetime(1986, 5, 31))
]

grade_dates_high = [
    (datetime(1986, 9, 1), datetime(1987, 5, 31)),
    (datetime(1987, 9, 1), datetime(1988, 5, 31))
]
univercity_ix=[
    (datetime(1988, 9, 1), datetime(1989, 5, 31)),
    (datetime(1989, 9, 1), datetime(1990, 5, 31)),
    (datetime(1990, 9, 1), datetime(1991, 5, 31)),
    (datetime(1991, 9, 1), datetime(1992, 5, 31)),
    (datetime(1992 ,9,  1), datetime(1993, 5, 31))
]

new_generation_grades = [
    (datetime(2006, 9, 1), datetime(2007, 5, 31)),
    (datetime(2007, 9, 1), datetime(2008, 5, 31)),
    (datetime(2008, 9, 1), datetime(2009, 5, 31)),
    (datetime(2009, 9, 1), datetime(2010, 5, 31)),
    (datetime(2010, 9, 1), datetime(2011, 5, 31))
]

# Define the start and end dates for each grade in the new generation high school grades (6-12)
new_generation_high_grades = [
    (datetime(2011, 9, 1), datetime(2012, 5, 31)),
    (datetime(2012, 9, 1), datetime(2013, 5, 31)),
    (datetime(2013, 9, 1), datetime(2014, 5, 31)),
    (datetime(2014, 9, 1), datetime(2015, 5, 31)),
    (datetime(2015, 9, 1), datetime(2016, 5, 31)),
    (datetime(2016, 9, 1), datetime(2017, 5, 31)),
    (datetime(2017, 9, 1), datetime(2018, 5, 31)),
]
new_univer=[
    (datetime(2018, 9, 1), datetime(2019, 5, 31)),
    (datetime(2019, 9, 1), datetime(2020, 5, 31)),
    (datetime(2020, 9, 1), datetime(2021, 5, 31)),
    (datetime(2021, 9, 1), datetime(2022, 5, 31)),
]

#XIX -r zuunii 10 n jil
grade_data = []
def calculate_studied_time(grade_dates, hours_per_day, start_index, end_index):
    for i, (start_date, end_date) in enumerate(grade_dates, start=start_index):
        date_range = pd.date_range(start=start_date, end=end_date)
        working_days = len(date_range) - sum(1 for day in date_range if day.dayofweek >= 6)  
        total_studied_minutes = working_days * hours_per_day * 60
        grade_data.append({
            'Анги': f'{i} Анги',
            'Эхлэх жил': start_date.strftime('%Y-%m-%d'),
            'Төгсөх жил': end_date.strftime('%Y-%m-%d'),
            'Сурсан цаг (минут)': total_studied_minutes,
            'Ажлын өдөр': working_days,
            'Нийт өдөр': len(date_range),
            'Бүтэн долоо хоног': round(len(date_range)/7),
            'Сонирхосон хичээлийн цаг': round(len(date_range)/7)*4
        })
        

    return pd.DataFrame(grade_data)[start_index-1:end_index].sum()
#XIX -r zuunii ih surguuli
uni_data=[]
def calculate_studied_time_univercity(grade_dates,hours_per_day,start_index,end_index): 
     for i, (start_date, end_date) in enumerate(grade_dates, start=start_index):
        date_range = pd.date_range(start=start_date, end=end_date)
        working_days = len(date_range) - sum(1 for day in date_range if day.dayofweek >= 6)
        total_studied_minutes = working_days * hours_per_day * 60
        uni_data.append({
            'Курс': f'{i} Курс',
            'Эхлэх жил': start_date.strftime('%Y-%m-%d'),
            'Төгсөх жил': end_date.strftime('%Y-%m-%d'),
            'Сурсан цаг (минут)': total_studied_minutes,
            'Ажлын өдөр': working_days,
            'Нийт өдөр': len(date_range),
            'Бүтэн долоо хоног': round(len(date_range)/7),
            
        })


#XX - r zuunii 10 n jil
new_grade_data = []
def calculate_new_studied_time(grade_dates, hours_per_day, start_index, end_index):
    for i, (start_date, end_date) in enumerate(grade_dates, start=start_index):
        date_range = pd.date_range(start=start_date, end=end_date)
        working_days = len(date_range) - sum(1 for day in date_range if day.dayofweek >= 5)
        total_studied_minutes = working_days * hours_per_day * 60
        new_grade_data.append({
            'Анги': f'{i} Анги',
            'Эхлэх жил': start_date.strftime('%Y-%m-%d'),
            'Төгсөх жил': end_date.strftime('%Y-%m-%d'),
            'Сурсан цаг (минут)': total_studied_minutes,
            'Ажлын өдөр': working_days,
            'Нийт өдөр': len(date_range),
            'Бүтэн долоо хоног': round(len(date_range)/7),
            'Сонирхосон хичээлийн цаг': round(len(date_range)/7)*4
        })

    return pd.DataFrame(new_grade_data)

new_uni_data=[]
def  calculate_new_studied_time_univercity(grade_dates,hours_per_day,start_index,end_index): 
     for i, (start_date, end_date) in enumerate(grade_dates, start=start_index):
        date_range = pd.date_range(start=start_date, end=end_date)
        working_days = len(date_range) - sum(1 for day in date_range if day.dayofweek >= 5)  
        total_studied_minutes = working_days * hours_per_day * 60
        new_uni_data.append({
            'Курс': f'{i} Курс',
            'Эхлэх жил': start_date.strftime('%Y-%m-%d'),
            'Төгсөх жил': end_date.strftime('%Y-%m-%d'),
            'Сурсан цаг (минут)': total_studied_minutes,
            'Ажлын өдөр': working_days,
            'Нийт өдөр': len(date_range),
            'Бүтэн долоо хоног': round(len(date_range)/7),
            'Дадлагийн эзлэх хувь': 40/working_days
            
        })


    
grouped_grades = {
    '1-3 grades': calculate_studied_time(grade_dates, 3, 1, 3),
    '4-8 grades': calculate_studied_time(grade_dates_middle, 4.15, 4, 8),
    '9-10 grades': calculate_studied_time(grade_dates_high, 4.5, 9, 10)
}
print(pd.DataFrame(grade_data))
print("\n")
for group, values in grouped_grades.items():
    print(group)
    print(values[['Сурсан цаг (минут)', 'Ажлын өдөр', 'Нийт өдөр']])
    
print("\n")
hours_per_day_university = 4.5
university_grouped_grades = calculate_studied_time_univercity(univercity_ix, hours_per_day_university, 1, 5)
print(pd.DataFrame(uni_data))

print("\n")

new_university_grouped_grades = calculate_new_studied_time_univercity(new_univer, hours_per_day_university, 1, 4)
print(pd.DataFrame(new_uni_data))

print("\n")

new_grouped_grades = {
    '1-5 grades': calculate_new_studied_time(new_generation_grades, 2, 1, 5),
    '6-12 grades': calculate_new_studied_time(new_generation_high_grades, 3.5, 6, 12),
}
print(pd.DataFrame(new_grade_data))
print("\n")

for group, values in new_grouped_grades.items():
    print(group)
    print(values[['Сурсан цаг (минут)', 'Ажлын өдөр', 'Нийт өдөр']])
    
    
    
total_new_studied_minutes_sum = pd.DataFrame(new_grade_data)['Сурсан цаг (минут)'].sum()
print("2006-2018 оны нийт сурсан хугацаа:", total_new_studied_minutes_sum , "мин")

total_studied_minutes_sum = pd.DataFrame(grade_data)['Сурсан цаг (минут)'].sum()
print("1978-1988 оны нийт сурсан хугацаа:", total_studied_minutes_sum , "мин")

total_studied_minutes_sum_univercity = pd.DataFrame(uni_data)['Сурсан цаг (минут)'].sum()
print("1988 онд Их сургуульд орсон:", total_studied_minutes_sum_univercity, "мин")

total_studied_minutes_sum_univercity_XX = pd.DataFrame(new_uni_data)['Сурсан цаг (минут)'].sum()
print("2018 онд Их сургуульд орсон:", total_studied_minutes_sum_univercity_XX, "мин")

