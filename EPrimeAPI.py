import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5555
ADDRESS = (HOST, PORT)
OPTION_LENGTH = 1
FORMAT = 'utf-8'

# epr_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# epr_server.bind(ADDRESS)

# eyetrackerclient = None
# collecting = False
# collection = []

# def collect_one_XML_record():
#     print("peepeepoopoo")
    
# def handle_client(conn, addr):
#   option = conn.recv(OPTION_LENGTH).decode(FORMAT)
#   option = str(option)
  
#   if option:
#     if option == "1":
#       # start
#       collecting = True
#       collection = []
#     else:  
#       # stop
#       collecting = False
#       collection = []
    
#   if collecting:
#     collection.insert(collect_one_XML_record())
    


# def start():
#   epr_server.listen()
#   print(f"[STARTING] Server listening on {HOST}:{PORT}")
#   # connect to the eye-tracker here
#   conn, addr = epr_server.accept()
#   handle_client(conn, addr)
#   pass

epr_server = None
conn = None 
addr = None

# start the server
def start_eprime_server():
  global epr_server
  epr_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  epr_server.bind(ADDRESS)
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
    [signal, student_id, session_number, obj, image_number, image_type, expected_characterization, actual_characterization] = epr_data
    return (signal, student_id, session_number, obj, image_number, image_type, expected_characterization, actual_characterization)
  return []

# disconnect from the client
def disconnect_from_eprime():
  if conn:
    conn.close()