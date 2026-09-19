# Informasi Pribadi
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name

address = '123 Main Street'
address += ', Apartment 4B'

employee_age = 28
employee_info = f'{full_name} is {employee_age} years old'
print(employee_info)

# Pengalaman Kerja
experience_years = 5
experience_info = f'Experience: {experience_years} years'
print(experience_info)

# Detail Pekerjaan & Kartu Karyawan
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

# Kode Karyawan & Slicing
employee_code = 'DEV-2026-JD-001'

department = employee_code[0:3]
print(department)

year_code = employee_code[4:8]
print(year_code)

initials = employee_code[9:11]
print(initials)

last_three = employee_code[-3:]
print(last_three)