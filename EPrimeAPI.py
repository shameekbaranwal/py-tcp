import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5555
ADDRESS = (HOST, PORT)
OPTION_LENGTH = 1
FORMAT = 'utf-8'

epr_server = None
conn = None 
addr = None

# start the server
def start_eprime_server():
  global epr_server
  epr_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  epr_server.bind(ADDRESS)
  epr_server.listen()
  return f"{HOST}:{PORT}"

# connect to eprime client
def connect_to_eprime():
  global conn, addr
  conn, addr = epr_server.accept()
  print("[CONNECTED] E-Prime client connected to server")
	
# handle the client, and return the parsed data (<start/stop>, <student id>, <trial block>, <robot/fish>, <image number>, <image type>, <categorization>)
def get_data_from_eprime():
  if conn == None:
    connect_to_eprime()
    
  epr_data = conn.recv(1024).decode(FORMAT)
  
  if (epr_data):
    epr_data = epr_data.split("_")
    [signal, student_id, trial_block, obj, image_number, image_type, categorization] = epr_data
    return (signal, student_id, trial_block, obj, image_number, image_type, categorization)
  return ()

# disconnect from the client
def disconnect_from_eprime():
  if conn:
    conn.close()