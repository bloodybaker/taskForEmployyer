from string import ascii_letters, digits
from random import choice, randint

alphabet = ascii_letters + digits
rand_str = lambda l: "".join(choice(alphabet) for i in range(l))

some_mails = [
	f"{rand_str(6)}@eu.at:{rand_str(6)}\n"
		for i in range(randint(1000, 100000))
]

def main():
	file_input = open("input.txt", "w")
	file_main = open("main.txt", "w")

	for i in range(int(1e6)*3):
		file_input.write(
			choice(some_mails) if randint(0, 100) > 60 else\
				f"{rand_str(6)}@eu.at:{rand_str(6)}\n"
		)

		file_main.write(
			choice(some_mails) if randint(0, 100) > 30 else\
				f"{rand_str(6)}@eu.at:{rand_str(6)}\n"
		)

	file_input.close()
	file_main.close()

if __name__ == "__main__":
	main()