import requests
import time


def parse_stack(fromdate, tagged, page):
    url = f'https://api.stackexchange.com//2.3/questions?page={page}&fromdate={fromdate}&order=desc&pagesize=100&' \
          f'sort=creation&tagged={tagged}&site=stackoverflow'
    response = requests.get(url)
    return response


def fromdate(period):
    real_time = time.time()
    res = real_time - period * 24 * 3600
    return res


def result():
    period = 2
    tag = 'python'
    j = 1
    while True:
        try:
            queues = parse_stack(int(fromdate(period)), tag, j)
            print(queues.status_code)
            # if queues.status_code == 200:
            for i in queues.json()['items']:
                print(f'Дата вопроса {time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(i["creation_date"]))} '
                      f'Вопрос: {i["title"]}')
            # else:
            #     break
            j += 1
        except:
            break


result()
