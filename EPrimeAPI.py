from asyncio.windows_events import NULL
import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5555
ADDRESS = (HOST, PORT)
OPTION_LENGTH = 1
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

eyetrackerclient = NULL
collecting = False
collection = []

def collect_one_XML_record():
    print("peepeepoopoo")
    
def handle_client(conn, addr):
  option = conn.recv(OPTION_LENGTH).decode(FORMAT)
  option = str(option)
  
  if option:
    if option == "1":
      # start
      collecting = True
      collection = []
    else:  
      # stop
      collecting = False
      collection = []
    
  if collecting:
    collection.insert(collect_one_XML_record())
    


def start():
  server.listen()
  print(f"[STARTING] Server listening on {HOST}:{PORT}")
  # connect to the eye-tracker here
  conn, addr = server.accept()
  handle_client(conn, addr)
  pass
    