import requests


def find_by_tag(comment):
    params = {'comments': comment}
    headers = {
        'Accept': 'Application/json'
    }
    url = 'https://jsonplaceholder.typicode.com/comments'
    r = requests.get(url, params=params, headers=headers)
    print(r.status_code, r.headers)
    print(r.content)


def get_site():
    r = requests.get('https://jsonplaceholder.typicode.com')
    with open('comments.json', 'a', encoding='utf-8') as file:
        file.write(str(r.headers))
        file.write('\n')
        file.write(str(r.content))
        file.write('\n')


def write_to_file(data, content, mode='w'):
    with open(data, mode=mode, encoding="utf-8") as file:
        file.write(content)


if __name__ == '__main__':
    find_by_tag('string')
    get_site()
    write_to_file('comments.json', 'The end', 'a')
