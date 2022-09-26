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
	
# handle the client, and return the parsed data [START/STOP]_[Subject]_[ExperimentNumber]_[Name]_[Age]_[Sex]_[List1.Cycle]_[Experiment]_[SlNo]_[Hands][Head][Antenna][Legs][Chest]_[Categorization]

def get_data_from_eprime():
  if conn == None:
    connect_to_eprime()
    
  epr_data = conn.recv(1024).decode(FORMAT)
  
  if (epr_data):
    epr_data = epr_data.split("_")
    [signal, subject, experiment_number, name, age, sex, list_cycle, experiment, serial_number, img_code, categorization] = epr_data
    return (signal, subject, experiment_number, name, age, sex, list_cycle, experiment, serial_number, img_code, categorization)
  return ()

# disconnect from the client
def disconnect_from_eprime():
  if conn:
    conn.close()