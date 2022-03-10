from datetime import date


def get_birth_year():
    print("Enter Birth Day (YYYY) \n")
    while True:
        try:
            birth_year = input()
            # birth_year = i
            if (len(birth_year) == 4) and (int(birth_year) > 0):
                birth_year = int(birth_year)
                if (birth_year % 4 == 0) and (birth_year % 100 != 0) or (birth_year % 400 == 0):
                    global isLeapYear
                    isLeapYear = True
                else:
                    isLeapYear = False
                break
            else:
                raise ValueError
        except ValueError as v:
            print("Enter in Correct format (YYYY)")
            continue
    return birth_year


def get_birth_month():
    print("Enter Birth Month (MM) \n")
    while True:
        try:
            birth_month = input()
            # birth_month='0'+i
            if (len(birth_month) == 2) and (int(birth_month) <= 12) and (int(birth_month) > 0):
                birth_month = int(birth_month)
                break
            else:
                raise ValueError
        except ValueError as v:
            print("Enter in Correct format (MM)")
            continue
    return birth_month


def get_birth_day():
    print("Enter Birth Day (DD) \n")
    while True:
        try:
            birth_day = input()
            # birth_day=i
            if (len(birth_day) == 2) and (int(birth_day) <= 31):
                birth_day = int(birth_day)
                print(isLeapYear)
                if (user_birth_month == 2) and (birth_day == 29) and isLeapYear == False:
                    raise ValueError
                break
            else:
                raise ValueError

        except ValueError as v:
            print("Enter in Correct format (DD)")
            continue
    return birth_day


isLeapYear = False


def main():
    user_birth_year = get_birth_year()

    if user_birth_year != 0:
        global user_birth_month
        user_birth_month = get_birth_month()
    if user_birth_month != 0:
        global user_birth_day
        user_birth_day = get_birth_day()
    today = date.today()
    print("Your Current age :{year} Years {month} Month {Days} Days".format(year=today.year-user_birth_year,month=abs(today.month-user_birth_month),Days=abs(today.day-user_birth_day)))


if __name__ == "__main__":
    main()

# for i in range(10, 32):
#     x = get_birth_day(str(i))
#     print(x)
#     print(isLeapYear)
