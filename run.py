import praw
import prawcore
import configparser


config = configparser.ConfigParser()
config.read('conf.ini')
client_id = config['REDDIT']['client_id']
client_secret = config['REDDIT']['client_secret']


def main():
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent='Username checker (by u/impshum)',
                         timeout=3)

    with open('usernames_in.txt') as f:
        targets = f.read().splitlines()

    winners = []

    for target in targets:
        try:
            user = reddit.redditor(target)
            if user.id:
                print(f'{target} is not available')
        except prawcore.exceptions.NotFound as e:
            winners.append(target)
            print(f'{target} is available')

    with open('usernames_out.txt', 'w+') as f:
        f.write('\n'.join(winners))

    print(f'\n{len(winners)}/{len(targets)} usernames available\n')


if __name__ == '__main__':
    main()
