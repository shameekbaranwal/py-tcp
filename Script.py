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

collecting = False
collections = []


def handle_eprime():
  while 1:
    (signal, student_id, session_number, obj, image_number, image_type, expected_characterization, actual_characterization) = get_data_from_eprime()
    global collections, collecting
    
    if not collecting:
      if signal == "START":
        collecting = True
        collections = []
    else:
      file = open(f"{student_id}_{session_number}_{obj}_{image_number}_{image_type}_{expected_characterization}{actual_characterization}.txt", "x")
      for line in collections:
        file.write(line)
      file.close()
  pass

def handle_eyetracker():
  while 1:
    data = get_data_from_eye_tracker()
    if collecting:
      collections.insert(data)
  pass


tepr = threading.Thread(target=handle_eprime)
teye = threading.Thread(target=handle_eyetracker)

start_eprime_server()
connect_to_eye_tracker()
tepr.start()
teye.start()