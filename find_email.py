#!/usr/bin/env python3
import csv
import sys

def populate_dictionary(filename):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        email_dict = {i[0].strip().lower(): i[1].strip() for i in reader}
    return email_dict


def find_email(argv):
  try:
    fullname = str(argv[1] + " " + argv[2])
    email_dict = populate_dictionary('/home/student-03-bac577e94407/data/user_emails.csv')
    if fullname.lower() in email_dict:
        return email_dict.get(fullname.lower())
    else:
        return "No email address found"
  except IndexError:
    return "Missing parameters"



def main():
    print(find_email(sys.argv))

if __name__ == "__main__":
    main()
