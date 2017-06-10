#!/usr/bin/env python
# ManSort -- provides a tool for sort and removing irrelavant tweets

import json


def load_tweets():
    with open('tweets.json') as f:
        return f.readlines()


def print_tweet(l, num):
    raw = l[num]

    text = json.loads(raw)['text']

    author = json.loads(raw)['user']['screen_name']
    create_date = json.loads(raw)['created_at']

    final = ('\nAuthor: {}, Date: {}\n#{}: {}')
    print(final.format(author, create_date, num+1, text))


def delete_tweet(l, num):
    l[num] = None
    print('Tweet {} has been deleted'.format(num+1))


def save_changes(l):
    with open('tweets_sorted.json', 'w+') as f:
        for num in range(500):
            if l[num] is not None:
                f.write(l[num])

    print('Saving...')


def loop():
    data = load_tweets()

    for num in range(500):
        print_tweet(data, num)
        cmd = input('> ')

        if cmd is 'd':
            delete_tweet(data, num)
        elif cmd is 'q':
            print('Exiting...')
            return

    print('Reached end of tweets.')
    save_changes(data)


if __name__ == '__main__':
    print('ManSort')
    print('`d` to Delete, `Return` to continue, `q` to quit')

    loop()
