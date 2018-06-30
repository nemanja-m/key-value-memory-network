import argparse
import os

from colors import colorize
from core import Lucy
from constants import MODELS_DIR


def parse_args():
    parser = argparse.ArgumentParser(description='Start interactive chat with Lucy')
    parser.add_argument('-m', '--model', type=str,
                        default=os.path.join(MODELS_DIR, 'lucy'),
                        help='Path to bot model weights')
    return parser.parse_args()


def main():
    args = parse_args()
    lucy_bot = Lucy(model_path=args.model)

    print('Starting Lucy. Press {} to exit\n'.format(colorize('CTRL + C',
                                                              color='white')))

    try:
        while True:
            prompt = colorize('{:>5}: '.format('Me'))
            query = input(prompt).strip()

            response = lucy_bot.respond(query)
            lucy_prompt = colorize('{:>5}:'.format('Lucy'), color='red')
            print('{} {}'.format(lucy_prompt, response))

    except (EOFError, KeyboardInterrupt) as e:
        print('\n\nShutting down')


if __name__ == '__main__':
    main()
