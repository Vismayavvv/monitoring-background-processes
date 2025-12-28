import psutil
import time
from datetime import datetime
import json
import os
import platform

cpu_highest=5
# process_name =""
process_lists=[]

def log_directory():
    print(platform.system())
    try:
        system = platform.system()

        if system == "Windows":
            base_path = os.path.join(os.environ.get("USERPROFILE", os.path.expanduser("~")), "Desktop")
        else: 
            base_path = os.path.join(os.path.expanduser("~"), "Desktop")

        log_dir = os.path.join(base_path, "monitor_logs")
        os.makedirs(log_dir, exist_ok=True)
        return log_dir

    except Exception as e:
        print(f"Failed to create log directory: {e}")
    

def file_operation(top_process,log_dir):
     file_name = "cpu_report_" + str(datetime.now()) + ".log"
     file_name = file_name.replace(" ", "-").replace(":", "-")
     file_path = os.path.join(log_dir,file_name)
     
     print(file_name)
     print(file_path)
          
     with open (file_path, "a") as f:
          for i in top_process:      
            f.write(json.dumps(i) +"\n")
     garbage_clenaing(log_dir)

def cpu_utilisation(log_dir):
    process_lists=[]
    for p in psutil.process_iter():
        p.cpu_percent(interval=None)
    time.sleep(1)
        

    for p in psutil.process_iter(['cpu_percent' , 'pid', 'name' ]):
        try:
            cpu_utilisations = p.info['cpu_percent']
            process_id = p.info['pid']
            process_name = p.info['name']
            # print(f"Cpu utilisation{cpu_utilisations} , process_id{process_id} , process_name{process_name}")
            process_lists.append({f"process_name": process_name , "process_id":process_id ,"cpu_percent":cpu_utilisations})
            #print(str(process_lists))
            if cpu_utilisations > cpu_highest:
                    print(f"process_name: {process_name}")  
                    choice = input("Do you want to kill a process yes/No ")
                    try:
                        if choice == "yes" or choice == "YES":
                            print(f"The  process id is : {process_id} please kill it manually")
                        else:
                            print("Skipping termination")
                    except Exception as e:
                            print(e)
                            pass

        except(psutil.NoSuchProcess):
            print("Please try again")

    process_lists.sort(key=lambda x:x["cpu_percent"] , reverse=True)
    top_process = process_lists[:10]
    print(top_process)
    file_operation(top_process,log_dir)
    # print(process_lists)


def garbage_clenaing(log_dir):
     try:
        # current_path = os.getcwd()
        # print(current_path)
        for file in os.listdir(log_dir):
          path_clog_file = os.path.join(log_dir , file)
          print(path_clog_file)
          if file.startswith("cpu_report") and file.endswith(".log"):
               try:
                 if os.path.getmtime(path_clog_file) < time.time() - 86400:
                    os.remove(path_clog_file)
                    print(f"File Delete: {file}")
               except FileNotFoundError:
                   print(f"file not found: {file}")
               except PermissionError:
                   print(f"Unauthorized to access the file")
     except Exception as e:
         print(f"Error in garbage cleaning : {e} ")


log_dir = log_directory()
cpu_utilisation(log_dir)





