import requests
import datetime


def parse_stack(fromdate, tagged, page):
    url = f'https://api.stackexchange.com/2.3/questions?page={page}&fromdate={fromdate}&order=desc&pagesize=100&' \
          f'sort=creation&tagged={tagged}&site=stackoverflow'
    response = requests.get(url)
    return response


def from_date(period):
    today = datetime.datetime.now()
    day_ago = datetime.timedelta(days=period)
    res = today.combine(today.date(), today.min.time()) - day_ago
    return res.date()


def result():
    period = 2
    tag = 'python'
    j = 1
    all_questions = []
    while True:
        try:
            queues = parse_stack(from_date(period), tag, j)
            if len(queues.json()['items']) > 0:
                for i in queues.json()['items']:
                    all_questions.append(f'Вопрос: {i["title"]}')
                j += 1
            else:
                break
        except KeyError:
            break
    for j in all_questions:
        print(j)
    print(len(all_questions))


result()
