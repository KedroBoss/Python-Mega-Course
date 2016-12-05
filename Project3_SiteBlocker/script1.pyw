import time
from datetime import datetime as dt

DELAY = 5
H_START = 9
H_END = 16


hosts_path_temp = "hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=['www.facebook.com', 'facebook.com']


while True:
    working_t_start = dt(dt.now().year, dt.now().month,dt.now().day, H_START)
    working_t_end = dt(dt.now().year, dt.now().month,dt.now().day, H_END)
    if working_t_start < dt.now() < working_t_end:
        print('Working Hours')
        with open(hosts_path_temp, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' +website+ '\n')
    else:
        with open(hosts_path_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print('Free Hours')
    time.sleep(DELAY)
