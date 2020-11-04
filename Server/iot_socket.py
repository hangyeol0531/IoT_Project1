from pyfirmata import Arduino, util
import serial
import socket
import select
import time
ser = serial.Serial('/dev/ttyACM0', 9600)

# 통신 정보 설정
IP = ''
PORT = 8080
SIZE = 512
ADDR = (IP, PORT)

# 서버 소켓 설정
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("", PORT))  # 주소 바인딩
server_socket.listen()  # 클라이언트의 요청을 받을 준비
print('wait try connecting')

while True:
        client_socket, client_addr = server_socket.accept()  # 수신대기, 접속한 클라이언트 정보 (소켓, 주소) 반환
        data = client_socket.recv(SIZE)  # 클라이언트가 보낸 메시지 반환
        print('clinet connect')
        print("[{}] message : {}".format(client_addr,data))  # 클라이언트가 보낸 메시지 출력
        if data == b'red_on': ser.write(b'1')
        elif data == b'red_off': ser.write(b'2')
        elif data == b'blue_on': ser.write(b'3')
        elif data == b'blue_off': ser.write(b'4')
        elif data == b'green_on': ser.write(b'5')
        elif data == b'green_off': ser.write(b'6')
        elif data == b'all_on': ser.write(b'7');
        elif data == b'all_off'  : ser.write(b'8')
client_socket.close()  # 클라이언트 소켓 종료
    
