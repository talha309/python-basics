import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    raise ValueError(f"Invalid email: {email}")

def validate_phone(phone):
    pattern = r'^\+?[1-9]\d{1,14}$'
    if re.match(pattern, phone):
        return True
    raise ValueError(f"Invalid phone number: {phone}")

def validate_url(url):
    pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
    if re.match(pattern, url):
        return True
    raise ValueError(f"Invalid URL: {url}")

def validate_date(date):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(pattern, date):
        return True
    raise ValueError(f"Invalid date: {date}")

def validate_time(time):
    pattern = r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$'
    if re.match(pattern, time):
        return True
    raise ValueError(f"Invalid time: {time}")

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
    if re.match(pattern, password):
        return True
    raise ValueError(f"Invalid password: {password}")

# --------- INPUTS AND VALIDATION -----------

validators = [
    ("email", validate_email),
    ("password", validate_password),
    ("phone number", validate_phone),
    ("URL", validate_url),
    ("date (YYYY-MM-DD)", validate_date),
    ("time (HH:MM)", validate_time)
]

for label, validator_func in validators:
    user_input = input(f"Enter a {label}: ")
    try:
        if validator_func(user_input):
            print(f"✅ Valid {label}")
    except ValueError as e:
        print(f"❌ {e}")
