# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:11:54 2021

@author: Anil
"""

import serial
import serial.tools.list_ports
import time 
import pandas as pd
import csv

#################################################################################
########## This function is to finding All Ports on the device. ################
def get_ports():   
    ports = serial.tools.list_ports.comports()
    
    return ports

###############################################################################################################
########## This function is  to finding the port which the Aduino was connected to the device. ################
def findArduino(portsFound): 
    commPort = 'None'
    numConnection = len(portsFound)
    
    for i in range(0, numConnection):
        port = portsFound[i]
        strPort = str(port)
        
        if 'CH340' in strPort:
            splitPort = strPort.split(" ")
            commPort = splitPort[0]
    
    return commPort

####################################################################################
######################## The Main Code ############################################

foundPorts = get_ports()
ArduinoPort = findArduino(foundPorts) 
print(ArduinoPort)


ser = serial.Serial(ArduinoPort, baudrate= 9600, timeout=(0.5))
ser.flushInput()
ser.close()
time.sleep(1)
ser.open()
time.sleep(2)

fields = ['ivmeX','ivmeY','ivmeZ','GyroX','GyroY','GyroZ','A0','A1']

with open('data.csv', 'w',newline='') as csvfile:
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    # writing the fields 
    csvwriter.writerow(fields) 



data = []
i = 0
while True:
    line = str(ser.readline().decode('ascii').strip())
    
    try:
        info=line.split(" ")
        info2=[info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7]]
        print(info2)
        data.append(info2)

    except:
        print("Reading Error")
        
    with open('data.csv', 'a',newline='') as csvfile:
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(data[i])
    
    i = i + 1

    
        

    