import psutil
import datetime
import shutil
import time



def log_system_health( log_file = "System_health_log.txt"):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print (f"timestamp: {timestamp}")

    cpu_usage = psutil.cpu_percent(interval=1)

    #disk usage in c drive 
    
    
    total,used,free = shutil.disk_usage("C:/")
   # print(f"CPU Usage: {cpu_usage}%")
    print("Space in c drive:")
    print(f"TOTAL: , {total//(2**30)}, GB | USED: , {used//(2**30)}, GB | FREE: , {free//(2**30)}, GB")

    total,used,free = shutil.disk_usage("D:/")
    print("Space in D drive:")
    print(f"TOTAL: , {total//(2**30)}, GB | USED: , {used//(2**30)}, GB | FREE: , {free//(2**30)}, GB")

    total,used,free = shutil.disk_usage("E:/")
    print("Space in E drive:")
    print(f"TOTAL: , {total//(2**30)}, GB | USED: , {used//(2**30)}, GB | FREE: , {free//(2**30)}, GB") 

    with open(log_file, "a") as f:
        f.write(f"{timestamp} | CPU Usage: {cpu_usage}%\n")
        f.write(f"Disk Usage (C:/): Total: {total//(2**30)} GB | Used: {used//(2**30)} GB | Free: {free//(2**30)} GB\n")
        f.write(f"Disk Usage (D:/): Total: {total//(2**30)} GB | Used: {used//(2**30)} GB | Free: {free//(2**30)} GB\n")
        f.write(f"Disk Usage (E:/): Total: {total//(2**30)} GB | Used: {used//(2**30)} GB | Free: {free//(2**30)} GB\n")

    print(f"System_health_log written at {timestamp}")
    time.sleep(60)

log_system_health()  
             




    


     
