import re
import json
import requests

def write_to_file(file, data, mode='w'):

    print('Writing to {}\n'.format(file))

    with open(file, mode) as newfile:
        newfile.write(data)


def read_file_data(file):

    print('Reading from {}\n'.format(file))

    try:
        opened_file = open(file)
        data = opened_file.read()
    finally:
        opened_file.close()

    return data

def get_service_data(url):

    result = requests.get(url)

    if result.status_code == 200:
        return result
    else:
        raise RuntimeError("Request from url = '{}' ended with code {}".format(url, result.status_code))


# ОСНОВАЯ ФУНКЦИЯ МОДУЛЯ
def main():

    print('***** TASK 9 part 1 *****\n')
    textdata = 'Hello, this is the example of the data!\nThis is the last line of this text\n'
    print('\nDATA TO SAVE IN FILE:',textdata)
    write_to_file('some_data.txt', textdata)
    print(read_file_data('some_data.txt'))

    print('\n***** TASK 9 part 2 *****\n')
    response = get_service_data('https://jsonplaceholder.typicode.com/')
    dict_for_json = {}
    for hdr, value in response.headers.items():
        dict_for_json[hdr] = value
        print('{}:{}\n'.format(hdr, value))

    print('\nJSON response saved in file \'site_response.json\'')
    write_to_file('site_response.json', json.dumps(dict_for_json, sort_keys=True, indent=4))


    print('\n***** TASK 9 part 3 *****\n')
    habrahabr_url = 'https://habrahabr.ru/'
    habrahabr_response = requests.get(habrahabr_url)
    if habrahabr_response.status_code == 200:
        link_pattern = r'<a[^><]*href=[\'"]([^><\'"]*)[\'"][^><]*>'
        print('Links from {} saved in file \'site_links.txt\''.format(habrahabr_url))
        write_to_file('site_links.txt', '')
        for link_string in re.findall(link_pattern, habrahabr_response.text):
            write_to_file('site_links.txt', link_string + '\n', mode = 'a')
            print(link_string)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')