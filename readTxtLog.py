import time
from sendTextMessage import sendSmsNotification

def read_other_terminal_output(file_path):
    try:
        with open(file_path, 'r') as file:
            frame_time = 0
            messageSent = False
            while True:
                line = file.readline()
                if not line:
                    time.sleep(0.1)  # Sleep briefly to avoid consuming too much CPU
                    continue
                split_line = line.strip().split(' ')
                print(split_line)
                if(len(split_line) > 4):
                    print("frame",frame_time)
                    if(split_line[2] != '(no'):
                        # print("found some animal")
                        # check if split_line[4] can be converted to integer 
                        if 'ms' in split_line[4]:
                            frame_time+= int(split_line[4].split('.')[0])
                        if(frame_time > 2500):
                            print("animal detected:", split_line[3])
                            if messageSent == False:
                                messageSent = True
                                sendSmsNotification("Animal detected: "+split_line[3])
                                print("message sent")

                    else:
                        frame_time = 0
                        print("no animal found")

    except FileNotFoundError:
        print("File not found. Make sure the correct file path is provided.")

if __name__ == "__main__":
    file_path = 'logs.txt'
    read_other_terminal_output(file_path)
