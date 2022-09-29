import os,glob
import pandas as pd

attributes=["CNT","TIME","TIME_TICK","FPOGX","FPOGY","FPOGS","FPOGD","FPOGID","FPOGV","LPOGX","LPOGY","LPOGV","RPOGX","RPOGY","RPOGV","BPOGX","BPOGY","BPOGV","LPCX","LPCY","LPD","LPS","LPV","RPCX","RPCY","RPD","RPS","RPV","LEYEX","LEYEY","LEYEZ","LPUPILD","LPUPILV","REYEX","REYEY","REYEZ","RPUPILD","RPUPILV","CX","CY","CS","BKID","BKDUR","BKPMIN","LPMM","LPMMV","RPMM","RPMMV","DIAL","DIALV","GSR","GSRV","HR","HRV","TTL0","TTL1","TTLV","PIXX","PIXY","PIXS","PIXV"]


    
path=".\\Text_files"       #Path of the folder which contains text files

for file in os.listdir(path): 
    f = open(f"{path}\\{file}", "r") 
    filename=os.path.splitext(file)[0]
   
    attribute_destructure = filename.split("_")
    [subject, experiment_number, name, age, sex, list_cycle, experiment, serial_number, img_code, categorization] = attribute_destructure    
    
    for item in attributes:  #creating array for each of the attribute
        vars()[item]=[]

    
    for line in f.readlines():  #reading line by line        
        
        new_arr=line.split()
        length=len(new_arr)
        for i in range(1,length-1):
            temp=new_arr[i].split("=")
            vars()[temp[0]].append(float(temp[1][1:-1]));
        
        # Creating Empty DataFrame and Storing it in variable df
    df = pd.DataFrame()

    for item in attributes:
        df[item]=vars()[item];
  
               
    df.to_csv(f".\\{subject}_{experiment_number}_{name}_{age}_{sex}_{list_cycle}_{experiment}_{serial_number}_{img_code}_{categorization}.csv", index=False);    





#print(vars()[attributes[0]])




