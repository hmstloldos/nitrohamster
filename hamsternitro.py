import requests
import random
import string
import time
import os


class NitroGen:
	def __init__(file):
		file.fileName = "generated.txt"

	def main(cons):
		os.system('cls' if os.name == 'nt' else 'clear')
		print("""

☁  ☁  ☀  ☁
 |Hamster|
   /   \
  /     \
 /       \
/        \
""")
		cons.slowType(
		    "Made By Hamster\n",
		    .02)
		time.sleep(1)
		cons.slowType(
		    "Boa Sorte Pra Gerar.\n.\n",
		    .02)
		time.sleep(1)
		cons.slowType(
		    "Hamster © 2021",
		    .02)
		print("""☠️
""")
		time.sleep(1)
		cons.slowType(
		    "\nQuantos Códigos De Nitro Deseja Testar A Sorte?: ",
		    .02,
		    newLine=False)
		gencode = int(input(''))
		cons.slowType("\nAperte Enter Para Continuar: ", .02, newLine=False)
		vercode = input('')
		vercode = vercode if vercode != "" else None
		cons.generator(gencode)
		cons.checker(notify=vercode)
		input("\nEsse Foi O Fim, E aí Como Foi?")
		[input(input_thing) for input_thing in range(4, 0, -1)]

	def slowType(main, text, sleep_time, newLine=True):
		for i in text:
			print(i, end="", flush=True)
			time.sleep(sleep_time)
		if newLine:
			print()

	def generator(file, amount):
		with open(file.fileName, "w", encoding="utf-8") as txtfile:
			print("Aguarde, Eu demoro um pouco...")
			timeTaken = time.time()
			for i in range(amount):
				code = "".join(
				    random.choices(string.ascii_uppercase + string.digits +
				                   string.ascii_lowercase,
				                   k=16))
				txtfile.write(f"https://discord.gift/{code}\n")
			print(
			    f"Generated {amount} codes | Time taken: {round(time.time() - timeTaken, 5)}s\n"
			)

	def checker(fileimport, notify=None):
		with open(fileimport.fileName, "r", encoding="utf-8") as txtfile:
			with open("list.md", "w", encoding="utf-8") as mdfile:
				for line in txtfile.readlines():
					raw_code = line.strip("\n")
					strip_code = raw_code.strip("https://discord.gift/")
					req = requests.get(
					    f"https://discordapp.com/api/v6/entitlements/gift-codes/{strip_code}?with_application=false&with_subscription_plan=true"
					)
					if req.status_code == 200:
						print(f" Valid | {raw_code} ")
						mdfile.write(
						    f"> ![VALID](assets/yes.png) Valid: {raw_code}\n\n-\n\n"
						)
					elif req.status_code == 429:
						print(f" [INVALID] | ( code {raw_code} ) ")
						mdfile.write(
						    f"> ![RATELIMITED](assets/warn.png) Rate-limited: {raw_code}\n\n-\n\n"
						)
					else:
						print(f" Invalid | {raw_code} ")
						mdfile.write(
						    f"> ![INVALID](assets/no.png) Invalid: {raw_code}\n\n-\n\n"
						)


if __name__ == '__main__':
	Gen = NitroGen()
	Gen.main()