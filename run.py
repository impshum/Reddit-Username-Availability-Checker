import praw
import configparser

config = configparser.ConfigParser()
config.read('conf.ini')
client_id = config['REDDIT']['client_id']
client_secret = config['REDDIT']['client_secret']


class C:
    W, G, R, P, Y, C = '\033[0m', '\033[92m', '\033[91m', '\033[95m', '\033[93m', '\033[36m'


def main():
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent='Username checker (by /u/impshum)')

    with open('usernames_in.txt') as f:
        targets = f.readlines()

    winners = []

    for target in targets:
        try:
            target = target.strip()
            user = reddit.redditor(target)
            if user.id:
                print(f'{C.R}{target} is not available{C.W}')
        except Exception:
            winners.append(target)
            print(f'{C.G}{target} is available{C.W}')

    with open('usernames_out.txt', 'w') as f:
        f.write('\n'.join(winners))

    print(f'\n{len(winners)} winners\n')


if __name__ == '__main__':
    main()
