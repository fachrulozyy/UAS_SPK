import string

# feel free to give any chatbot name you like
chatbot_name = "Idaman" + "Mamah"

# sentinel loop: a loop keeps going until reaching the end signal given by the user
while(True):
	
	# simple string preprocessing for given user message
	user_massage = input("you: ").lower().strip(string.punctuation+string.whitespace)
	
	# the response by the chatbot starts by printing its name 
	print(chatbot_name + ":", end=' ')
	
	# finish conversation by saying quit (or selesai)
	if user_massage == "quit" or user_massage == "selesai":
		print("Sampai ketemu lagi sayang")
		break
		
	# conditionals for conversation
	if user_massage == "hai kamu":
		print("hai juga kamu", end='')
	elif user_massage == "kamu apa kabar":
		print("baik kok, kalo kamu?", end='')
	elif "cuaca mendung" in user_massage: # check string contaiment
		print("loh kenapa?, aku kira cuaca cerah sesuai wajahmu yang cerah", end='')
	# mendung (= cloudy) flow
	elif "mendung" in user_massage:
		print("Apanya yang mendung?", end='')
	elif user_massage == "kepo":
		print("hmmmm", end='')
	elif user_massage == "cuaca":
		print("Cuma cuaca kan, bukan hati? hehe", end='')
	elif user_massage == "makasih" or user_massage == "thanks":
		print("masama", end='')
	# if none matches (aka the chatbot gets confused)
	else:
		print("Ehh2, gimana?", end='')
	print()