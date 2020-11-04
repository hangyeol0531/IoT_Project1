from pyfirmata import Arduino, util
import serial
import socket
ser = serial.Serial('/dev/ttyACM1', 9600)

# 통신 정보 설정
IP = ''
PORT = 8080
SIZE = 1024
ADDR = (IP, PORT)

# 서버 소켓 설정
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#     server_socket.bind(ADDR)  # 주소 바인딩
#     server_socket.listen()  # 클라이언트의 요청을 받을 준비

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("", socketPort))
server.listen(10)

while True:
        client_socket, client_addr = server_socket.accept()  # 수신대기, 접속한 클라이언트 정보 (소켓, 주소) 반환
        data = client_socket.recv(SIZE)  # 클라이언트가 보낸 메시지 반환
        print("[{}] message : {}".format(client_addr,data))  # 클라이언트가 보낸 메시지 출력

        client_socket.sendall("welcome!".encode())  # 클라이언트에게 응답

client_socket.close()  # 클라이언트 소켓 종료
    # if data == 'red_on': ser.write(b'1')
    # elif data == 'red_on': ser.write(b'2')
    # elif data == 'blue_on': ser.write(b'3')
    # elif data == 'blue_off': ser.write(b'4')
    # elif data == 'green_on': ser.write(b'5')
    # elif data == 'green_off': ser.write(b'6')
    # elif data == 'all_on': ser.write(b'7');
    # elif data == 'all_off'  : ser.write(b'8')


