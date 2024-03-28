import requests

base_url = "http://localhost"
base_port = 3500

def getActions():
    response = requests.get(f"{base_url}:{base_port}/ucb/init")
    arms = int(response.content.decode('utf-8'))
    print(f"There are: {str(arms)} compositions! From 0 to {str(arms-1)}.")

def getPerceptionData():
    response = requests.get(f"{base_url}:{base_port}/ucb/perception-data")
    if (response.content.decode('utf-8') == "NOT FOUND"):
        print("Something went wrong!")
    action, average_response_time = response.content.decode('utf-8').split("|")
    print(f"Action {action} with average response time {average_response_time}")

def setComposition(index):
    requests.post(f"{base_url}:{base_port}/ucb/composition", data=str(index))

if __name__ == "__main__":
    readInput = ""
    while (readInput != "exit"):
        readInput = input("Distributor API> ")
        if (readInput == "actions"):
            getActions()
        elif (readInput == "perception"):
            getPerceptionData()
        elif (readInput == "composition"):
            readInput = input("Type a number from 0 to 3: ")
            setComposition(readInput)
        elif (readInput == "exit"):
            print("See you later aligator!")
        else:
            print("Wrong command!\nType: \n\t exit\n\tactions\n\tperception\n\tcomposition\n")
