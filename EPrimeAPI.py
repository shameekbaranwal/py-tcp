import socket
import threading
from GazepointAPI import eye_tracker_client


HOST = socket.gethostbyname(socket.gethostname())
PORT = 5555
ADDRESS = (HOST, PORT)
OPTION_LENGTH = 1
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

# initializing eye tracker client
et_client=eye_tracker_client();


collecting = False
collection = []

def collect_one_XML_record():
    print("peepeepoopoo")
    
def handle_server_eye_tracker(et_client):
  while collecting:
    rxdat = et_client.recv(1024)  
  
  

def handle_client(conn, addr):
  option = conn.recv(OPTION_LENGTH).decode(FORMAT)
  option = str(option)
  collecting =True
  
  
  while option:
    thread = threading.Thread(target=handle_server_eye_tracker;, args=(et_client)))
    thread.start()

    option=conn.recv(OPTION_LENGTH).decode(FORMAT)
    option = str(option)
    collecting=False
  

  


def start():
  
  print(f"[STARTING] Server listening on {HOST}:{PORT}")
  # connect to the eye-tracker here
  

  # e-prime studio
  server.listen()
  conn, addr = server.accept()
  handle_client(conn, addr);



start();
    