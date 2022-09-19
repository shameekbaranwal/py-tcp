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


def handle_eprime():
  while 1:
    # (signal, student_id, session_number, obj, image_number, image_type, expected_characterization, actual_characterization) = get_data_from_eprime()
    data = get_data_from_eprime()
    
    if (data):
      (signal, student_id, trial_block, obj, image_number, image_type, categorization) = data
      
      print(f"[DATA FROM E-PRIME] signal:{signal} student_id:{student_id} trial_block:{trial_block} image_number:{image_number} image_type:{image_type} categorization:{categorization}")
      
      
      global collections, collecting
      
      if not collecting:
        if signal == "START":
          collecting = True
          collections = []
          print("[COLLECTING] Started collecting data.")
      else:
        if not os.path.exists(f".\\{student_id}_{obj}"):
          os.mkdir(f".\\{student_id}_{obj}")
          print("[FOLDER CREATED] Created folder for student : ", student_id, " and object : ", obj)
        
        collecting = False
        
        # store the data in csv not txt
        filename = f".\\{student_id}_{obj}\\{student_id}_{trial_block}_{obj}_{image_number}_{image_type}_{categorization}.txt"
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