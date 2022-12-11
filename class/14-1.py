import socket

s_ip = "127.0.0.1"
s_port = 12345
s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s_sock.bind(("127.0.0.1", 12345))
s_sock.listen(2)
print("Ready to Access...")
client, c_adder = s_sock.accept()
print("Client Acceses.")
client.send(b"Hi Cleint")

while 1:
  data = client.recv(1024).decode('utf-8-sig')
  if data == "end":
    print("Client be closed...")
    break
  else:
    print('Recieve data : ', data)

client.close()
s_sock.close()