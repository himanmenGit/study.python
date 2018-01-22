
__all__ = (
        'play_game',
        'PLAY_MESSAGE',
)

PLAY_MESSAGE = 'Play game!'

def play_game():
    print(PLAY_MESSAGE)
def buy_game():
    print('Buy_game!')

if __name__ == '__main__':
    play_game()
    buy_game()
    print(f'game.py의 module name: {__name__}')
