import requests

params = {
    'v': '5.68'
}


def get_friends(user_id):

    params['user_id'] = user_id
    response = requests.get('https://api.vk.com/method/friends.get', params)
    return response.json()['response']['items']


def get_user_names(friend_id):

    params['user_id'] = friend_id
    response = requests.get('https://api.vk.com/method/users.get', params)
    response = response.json()['response'][0]
    return '{} {}'.format(response['first_name'], response['last_name'])


def friends_list(user_id, friends_of_friends=0, number=0):

    for everyone, friends_id in enumerate(get_friends(user_id), 1):
        if number:
            print(number, end='_')
        print('{}. {}'.format(everyone, get_user_names(friends_id)))
        if friends_of_friends:
            friends_list(friends_id, number=everyone)


if __name__ == '__main__':
    MY_ID = 313360216
    friends_list(MY_ID, friends_of_friends=1)
