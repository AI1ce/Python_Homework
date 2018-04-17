import json
import requests
import sys
import time

VERSION = '5.69'

with open('token_file.json', encoding='utf-8') as file:
    data = json.load(file)
    USER_ID = data[0]['user_id']
    TOKEN = data[0]['token']


def about_user(user_id, query):
    params = {
        'v': VERSION,
        'user_id': user_id,
        'access_token': TOKEN,
    }
    response = requests.get(f"https://api.vk.com/method/{query}.get", params)
    return response.json()


def about_group(group_id):
    params = {
        'v': VERSION,
        'access_token': TOKEN,
        'group_id': group_id,
        'fields': 'members_count',
    }
    response = requests.get("https://api.vk.com/method/groups.getById", params)
    return response.json()


def output_to_user(*args):
    sys.stdout.write('\r')
    msg = args[0]
    calc = None
    if len(args) > 1:
        calc = args[1]
        op = '_-_\\'
        calc = 0 if calc == 3 else calc
        out = op[calc]
        calc += 1
        sys.stdout.write(f"{msg} {out}")
    else:
        sys.stdout.write(f"{msg}")
    sys.stdout.flush()
    return calc


def about_friends_group():
    groups_of_friends = []
    friends_info = about_user(USER_ID, 'friends')
    friends_ids = friends_info['response']['items']
    calc = 1
    for friend_id in friends_ids:
        status = 'error'
        while status != 'ok':
            try:
                unordered_friend_groups = about_user(friend_id, 'groups')
                calc = output_to_user('There is a request for data, please wait', calc)
                if 'response' in unordered_friend_groups:
                    friend_groups_ids = unordered_friend_groups['response']['items']
                    groups_of_friends += friend_groups_ids
                status = 'ok'
            except:
                status = 'error'
                time.sleep(2)
    set_of_groups = set(groups_of_friends)
    return set_of_groups


def main():
    time.sleep(2)
    list_of_group = []
    unordered_groups = about_user(USER_ID, 'groups')
    ordered_groups = set(unordered_groups['response']['items'])
    friends_groups_set = about_friends_group()
    ordered_groups.difference_update(friends_groups_set)
    output_to_user('Receiving data. Status: complete.\n')
    calc = 1
    for group_id in ordered_groups:
        status = 'error'
        while status != 'ok':
            try:
                calc = output_to_user('Data processing:', calc)
                dict_of_group = {}
                group_info = about_group(group_id)
                dict_of_group['gid'] = group_info['response'][0]['id']
                dict_of_group['name'] = group_info['response'][0]['name']
                if 'deactivated' in group_info['response'][0]:
                    dict_of_group['members_count'] = 'group banned'
                elif 'members_count' in group_info['response'][0]:
                    dict_of_group['members_count'] = group_info['response'][0]\
                                                ['members_count']
                else:
                    dict_of_group['members_count'] = 'Not available'
                list_of_group.append(dict_of_group)
                status = 'ok'
            except:
                status = 'error'
                # time.sleep(2)
    with open('result_1.json', 'w', encoding='utf-8') as file:
        json.dump(list_of_group, file, sort_keys=True,
                  indent=2, ensure_ascii=False)
        output_to_user('Write to file. Status: complete.\n')


if __name__ == '__main__':
    try:
        main()
    except:
        print('\tError')
        raise