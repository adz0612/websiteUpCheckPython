import validators
from pythonping import ping
while(1):
	website = input("Enter website  ")
	if(validators.url("https://"+website)):	
		try:
			response = ping(website,verbose=False)
			print("Website up!")
		except:
			print("Website down :(")
	else:
		print("Enter valid URL")


