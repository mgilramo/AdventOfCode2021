import requests

COOKIE = {'cookie': '_ga=GA1.2.1127791646.1648802706; _gid=GA1.2.1391386004.1648802706; '
                    'session=53616c7465645f5f0e8db9f17434a336118c19b5f4b845d0fa9e7514dd0a6043e26823b924e877eb91dc3cd684385e1eca647f4fa0f8fcd81363e409c5532a51'}


def download_input(url, file_name):
    res = requests.get(url, headers=COOKIE)

    full_path = f'input_files\\{file_name}'

    with open(full_path, 'w') as f:
        f.write(res.text)
