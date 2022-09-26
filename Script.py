# connect to eye tracker
# connect to e-prime
# create a boolean "collecting", and start the two threads, which run in parallel, and both have access to the boolean collecting, and the array collections[]
# call the eye-tracker thread teye and call the eprime thread tepr
# tepr:
#       > if collecting is false, then keep listening for one chunk of data, and once received, do the following:
#           >> parse the chunk data, and create a new file with the name according to that data
#           >> set collecting to true
#           >> empty the collections[] array
#       > if collecting is true, then keep listening for one chunk of data, and once received, do the following:
#           >> parse all the data from that chunk
#           >> use that, as well as the stuff currently in the collection[] array and append it all into the created file
#           >> set collecting to false
#           >> empty the collection[] array
# teye:
#       > while 1:
#       	>> grab the latest chunk of 240 bytes
#       	>> if collecting is true, then insert it into collection[], otherwise just ignore it.

from GazepointAPI import connect_to_eye_tracker, get_data_from_eye_tracker, disconnect_from_eye_tracker
from EPrimeAPI import start_eprime_server, get_data_from_eprime, disconnect_from_eprime
import threading
import atexit
import os

collecting = False
collections = []
FOLDER_NAMES = [
                "FishCongruent", 
                "FishIncongruent", 
                "RobotCongruent", 
                "RobotIncongruent", 
                "FishSingleFeatureInstruction", 
                "FishMultiFeatureInstruction", 
                "RobotSingleFeatureInstruction", 
                "RobotMultiFeatureInstruction"
              ]

def handle_eprime():
  while 1:
    data = get_data_from_eprime()
    
    if (data):
      (signal, subject, experiment_number, name, age, sex, list_cycle, experiment, serial_number, img_code, categorization) = data
      
      print(f"[DATA FROM E-PRIME] signal:{signal} subject:{subject} experiment_number:{experiment_number} name:{name} age:{age} sex:{sex} list_cycle:{list_cycle} experiment:{experiment} serial_number:{serial_number} img_code:{img_code} categorization:{categorization}")
      
      
      global collections, collecting
      
      if not collecting:
        if signal == "START":
          collecting = True
          collections = []
          print("[COLLECTING] Started collecting data.")
      else:
        if not os.path.exists(f".\\{FOLDER_NAMES[experiment_number]}\\{subject}_{experiment}"):
          os.mkdir(f".\\{subject}_{experiment}")
          print("[FOLDER CREATED] Created folder for subject : ", subject, " and object : ", experiment)
        
        collecting = False
        
        # store the data in csv not xml
        filename = f".\\{FOLDER_NAMES[experiment_number]}\\{subject}_{experiment}\\{subject}_{experiment_number}_{name}_{age}_{sex}_{list_cycle}_{experiment}_{serial_number}_{img_code}_{categorization}.xml"
        file = open(filename, "x")
        print("[FILE CREATED] Created file for for session : ", filename)
        
        for line in collections:
          file.write(line)
        print("[FILE WRITTEN] Wrote data to file.")
        
        file.close()
        print("[FILE CLOSED]")
        print("----------------------------------------")
  pass

def handle_eyetracker():
  while 1:
    data = get_data_from_eye_tracker()
    if collecting:
      collections.append(data)
  pass

def exit_handler():
  disconnect_from_eprime()
  print("[DISCONNECTED] Disconnected from E-Prime")
  disconnect_from_eye_tracker()
  print("[DISCONNECTED] Disconnected from Eye-Tracker")

tepr = threading.Thread(target=handle_eprime)
teye = threading.Thread(target=handle_eyetracker)
atexit.register(exit_handler)

ADDRESS = start_eprime_server()
print(f"[STARTING] Started E-Prime server on {ADDRESS}.")

connect_to_eye_tracker()
print("[STARTING] Established client's connection with Eye Tracker server.")

tepr.start()
teye.start()