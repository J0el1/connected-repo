#import module and setting up scanner object
import nmap

scanner = nmap.PortScanner()
#Non-flashy promt information

print('Garcia J Final, 1.2')

ip_addr = input('Please enter the IP address you want to scan: ')

print('The IP you entered is:', ip_addr)
type(ip_addr)

#Scan selection
resp = input("""\nPlease enter the type of scan you want to run
			1)SYN ACK Scan
			2)UDP Scann
			3)Comprehensive scan\n""")
			
print("You have selected option: ", resp, '\nCommencing scan...')

if resp == '1':
	
	print('Nmap Version: ', scanner.nmap_version())
	scanner.scan(ip_addr, '1-1024', '-v -sS')
	print(scanner.scaninfo())
	print('IP Status: ', scanner[ip_addr].state())
	print(scanner[ip_addr].all_protocols())
	print('Open Ports: ', scanner[ip_addr]['tcp'].keys())
	
	
elif resp == '2':
	print('Nmap Version: ', scanner.nmap_version())
	scanner.scan(ip_addr, '1-1024', '-v -sU')
	print(scanner.scaninfo())
	print('IP Status: ', scanner[ip_addr].state())
	print(scanner[ip_addr].all_protocols())
	print('Open Ports: ', scanner[ip_addr]['udp'].keys())
	
elif resp == '3':
	print('Nmap Version: ', scanner.nmap_version())
	scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
	print(scanner.scaninfo())
	print('IP Status: ', scanner[ip_addr].state())
	print(scanner[ip_addr].all_protocols())
	print('Open Ports: ', scanner[ip_addr]['tcp'].keys())
	
#regardless of type of scan conducted, print the results and .csv
	
print(scanner.csv(),file=open('ScanResults.csv', 'w'))

print('Scan succesful, results saved.')
