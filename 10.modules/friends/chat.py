def send_message():
    name, msg = input('이름과 메세지를","기준으로 입력 하세요:').split(',')
    print(f'{name}님께 message({msg})를 보냈습니다')

