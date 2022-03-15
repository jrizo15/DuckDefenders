import json
import grequests
import fuzzTest

"""___________ Configuration ___________"""
numClients = 1 #change this to modify number of clients 
numMessages = 1 #Change this to modify number of messages sent by each client
ID = "ADC1" #if you want to change id, you can
fileOutput = "dataOut"

url = "http://192.168.1.1/formSubmit.json"
dataOut = open(fileOutput,"w")

i = 1 
j = 0
for i in range(numMessages):
    values = []
    invalid = [{"INVALID" : 1, "INVALID" : fuzzTest.fuzzer(10,32,95)}]
    invalid2 = [{"hello","HI"}]
    for j in range(numClients):
        msg = fuzzTest.fuzzer(10,0,128)
        values.append({"clientID": ID,
                        "message" : msg})

    #change the parameter in post call to change what type of packet we are sending
    # values are valid packets, invalid and invalid2 are packets not formed correctly.
    rs = (grequests.post(url,params=p,timeout=2) for p in invalid2)
    ret = grequests.map(rs)
    print(ret)
    dataOut.write("Message #"+str(i)+"\n")
    for response in ret:
        if(response != None):
            dataOut.write("Response " +str(response.status_code))
            dataOut.write("\tTime elapsed: "+str(response.elapsed)+ "\n") 

    dataOut.write("\n\n")
    #print(grequests.map(rs))
