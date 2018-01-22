#import shop
#import game
#from game import play_game
#from game import *
from functions.game import *
# * 로 모두 임포트 할 경우 필요한 모듈(함수만) 문자열로 명시
#__all__ = (
#       'play_game',
#   )
#
#from shop import buy_item
from functions.shop import buy_item

from friends.chat import send_message

def Turn_on_game():
    # 1. 실행 메시지를 표시 (Turn on game)    
    print('= Turn on game =')
    # 2. 사용자에게 무엇을 할 것 인지 물어보기
    #   1. play game
    #   2. buy_item
    #   3. exit
    while True:
        try:
            selected = input('무엇을 실행 하시겠습니까?(1:play_game, 2:buy_item) : ')
            if int(selected) == 1: 
                #buy_gmae()
                play_game()
            elif int(selected) == 2:
                buy_item()
            elif int(selected) == 0:
                break
            elif int(selected) == 3:
                send_message()
            else:
                print('invalid input')
        except ValueError:
            print('must input number')

    print('Game Over')
    # 3. 1또는 2를 입력 시 해당 함수 실행후 다시 사용자에게 무엇을 할 지 물어보기
    # 4. 0을 입력하면 물어보는 반복문을 탈출하고 게임종료 메시지 표시(Game over)
#print(f'lol.py의 module name: {__name__}')

if __name__ == '__main__':
    Turn_on_game()

