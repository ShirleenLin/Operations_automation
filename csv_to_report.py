#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
    with open(csv_file_location) as f:
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        f = csv.DictReader(f, dialect='empDialect')
        employee_list = [data for data in f]
    return employee_list

def process_data(employee_list):
    department_list = [employee['Department'] for employee in employee_list]
    department_dict = {department: department_list.count(department) for department in set(department_list)}
    return department_dict

def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        f.writelines(f"{k}:{v}\n" for k, v in sorted(dictionary.items()))
    print(dictionary)

if __name__ == "__main__":
    csv_file_location = "/home/student-03-5ef644d4b08f/data/employees.csv"
    report_file = "/home/student-03-5ef644d4b08f/data/report.txt"
    employee_list = read_employees(csv_file_location)
    dictionary = process_data(employee_list)
    write_report(dictionary, report_file)
