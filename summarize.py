def summarize(file_path):
    from datetime import datetime

    current_date = datetime.now()

    day = current_date.day
    month = current_date.month
    year = current_date.year

    money_difference = int(input())

    with open(file_path, 'r') as f:
        for line in f:
            pass
        last_line = line.split()
        last_line = int(last_line[0])
        if money_difference > 0:
            last_line = last_line + money_difference
        else:
            last_line = last_line - money_difference
        f.close()

    with open(file_path, 'a') as f:
        f.write(f"\n{str(last_line)} {day} {month} {year}")
        f.close()


