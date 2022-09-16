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
  print(f"[STARTING] E-Prime Server listening on {HOST}:{PORT}")
  pass

# connect to eprime client
def connect_to_eprime():
  global conn, addr
  conn, addr = epr_server.accept()
	
# handle the client, and return the parsed data (<start/stop>, <student id>, <session number>, <robot/fish>, <image number>, <image type>, <expected characterization>, <actual characterization>)
def get_data_from_eprime():
  if conn == None:
    connect_to_eprime()
    
  epr_data = conn.recv(1024).decode(FORMAT)
  if (epr_data):
    epr_data = epr_data.split("_")
    [signal, student_id, obj, image_number, image_type, categorization] = epr_data
    return (signal, student_id, obj, image_number, image_type, categorization)
  return ()
  # return epr_data

# disconnect from the client
def disconnect_from_eprime():
  if conn:
    conn.close()