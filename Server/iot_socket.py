from pyfirmata import Arduino, util
import serial
import socket
ser = serial.Serial('/dev/ttyACM1', 9600)

HOST = '127.0.0.1'
PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen()

client_socket, addr = server_socket.accept()
print('Connected by', addr)

while True:
    # 클라이언트가 보낸 메시지를 수신하기 위해 대기합니다. 
    data = client_socket.recv(1024)
    # 빈 문자열을 수신하면 루프를 중지합니다. 
    if not data:
        break
    # 수신받은 문자열을 출력합니다.
    print('Received from', addr, data.decode())

    if data == 'red_on' ser.write(b'1')
    elif data == 'red_on' ser.write(b'2')
    elif data == 'blue_on' ser.write(b'3');
    elif data == 'blue_off' ser.write(b'4');
    elif data == 'green_on' ser.write(b'5');
    elif data == 'green_off' ser.write(b'6');
    elif data == 'all_on' ser.write(b'7');
    elif data == 'all_off' ser.write(b'8');
    # 받은 문자열을 다시 클라이언트로 전송해줍니다.(에코) 
    #client_socket.sendall(data)
# 소켓을 닫습니다.
client_socket.close()
server_socket.close()


