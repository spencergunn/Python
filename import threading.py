import threading
import time

pos =0

# This function simulates a long-running task
def forward(steps):
    global pos
    counter=0
    print("Forward Task started. Type 'stop' to end the task.")
    while not stop_event.is_set():
        print("Task is running...")
        time.sleep(1)
        pos +=1
        counter+=1
        if counter == steps:
            break
    stop_event.clear()
    print("forward Task has been stopped.", pos)

def backward(steps):
    global pos
    counter =0
    print("backward Task started. Type 'stop' to end the task.")
    while not stop_event.is_set():
        print("Task is running...")
        time.sleep(1)
        pos -=1
        counter+=1
        if counter == steps:
            break

    stop_event.clear()
    print("backward Task has been stopped.", pos)


def home():
    global pos
    print("home Task started. Type 'stop' to end the task.")
    while not stop_event.is_set():
        print("Task is running...")
        time.sleep(1)
        pos -=1
        if pos== 0 :
            print("home now " ,pos)
            break
    stop_event.clear()
    print("Task has been stopped.")



# Create an event object to signal the task to stop
stop_event = threading.Event()

task_thread = threading.Thread(target=forward, args={10})
# Wait for user input
while True:
    user_input = input("Enter command: ")
    if user_input.lower() == "stop":
        stop_event.set()  # Signal the task to stop
        task_thread.join()  # Wait for the task to finish
        print("Task stopped by user.")
        print (pos )

    if user_input.lower() == "quit":
        if task_thread.is_alive():
            stop_event.set()
            task_thread.join()
        print("quitting")
        break
        
    if user_input.startswith("fw"):
        if task_thread.is_alive():
            stop_event.set()
            task_thread.join()
        
        task_thread = threading.Thread(target=forward, args={100})
        task_thread.start( )

        print( user_input)
        
    if user_input.startswith("bw"):
        if task_thread.is_alive():
            stop_event.set()
            task_thread.join()
        
        task_thread = threading.Thread(target=backward, args={100})
        task_thread.start( )
        print( user_input)
        

    if user_input.startswith("home"):
        if task_thread.is_alive():
            stop_event.set()
            task_thread.join()
        print (pos)
        task_thread = threading.Thread(target=home)
        task_thread.start( )
        print( user_input)
        print (pos)
        