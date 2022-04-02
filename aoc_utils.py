import requests

COOKIE = {'cookie': '_ga=GA1.2.1127791646.1648802706; _gid=GA1.2.1391386004.1648802706; '
                    'session=53616c7465645f5f0e8db9f17434a336118c19b5f4b845d0fa9e7514dd0a'
                    '6043e26823b924e877eb91dc3cd684385e1eca647f4fa0f8fcd81363e409c5532a51'}

URL_BASE = 'https://adventofcode.com/2021/day/{}/input'
PATH_BASE = 'input_files\\day{}_input.txt'


def download_input(day):
    res = requests.get(URL_BASE.format(day), headers=COOKIE)

    with open(PATH_BASE.format(day), 'w') as f:
        f.write(res.text)
