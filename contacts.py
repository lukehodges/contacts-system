import json
contacts = {
	"luke" : {
		"emails" : ["email1@gmail.com","anotheremail@gmail.com"],
		"address" : "101mainstreet",
		"telephone" : '07771234567',
	},
	"ddg" : {
		"emails" : ["email1@gmail.com","anotheremail@gmail.com"],
		"address" : "101mainstreet",
		"telephone" : '07771234567',
	},
	"ben" : {
		"emails" : ["email2@gmail.com","anotheremail@gmail.com"],
		"address" : "101mainstreet",
		"telephone" :'07771234567',
	},
	"john" : {
		"emails" : ["email1@gmail.com","anotheremail@gmail.com"],
		"address" : "101mainstreet",
		"telephone" : '07771234567',
	}
}
def founduser(name,dic):
	if name in dic:
		return True
while 1:
	name = input('enter the contacts name\n> ')
	if founduser(name,contacts):
		print('the user has been found')

		information = contacts[name]
		emails = information['emails']
		emails = str(emails)
		address = information['address']
		telephone = information['telephone']
		print('emails:' + emails)
		print('\naddress: ' + address)
		print('telephone: ' + telephone)
	if founduser == False:
		print('contact not found')
	print('any other contacts')
	repeat = input("> ")
	if repeat == 'no' or 'n':
		break
while 1:
	name = input('enter the new contacts name\n> ')
	emails = []
	while True:
		email = input('enter the email')
		emails.append(email)
		if input('any more emails').upper == 'N' or 'NO':
			break
	address = input('enter the contacts address\n> ')
	telephone = input('enter the contacts telephone number\n> ')
	contacts[name] = {
		"emails" : emails,
		"address" : address,
		"telephone" : telephone
	}
	print(contacts)
