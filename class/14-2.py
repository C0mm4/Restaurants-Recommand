import socket
s_ip = "127.0.0.1"
s_port = 12345

c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Trying server connect...")
c_sock.connect((s_ip, s_port))

data = c_sock.recv(1024)
print("Recieve Data : ", data.decode('utf-8-sig'))

while 1:
  text = input()
  if text == "exit":
    c_sock.send(b'end')
    break
  c_sock.send(text.encode(('utf-8-sig')))

c_sock.close()