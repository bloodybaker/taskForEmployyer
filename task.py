import json

from result import Result


def main():
	file_input = open('input.txt', 'r')
	lines_input = file_input.readlines()
	file_input.close()
	
	file_main = open('main.txt', 'r')
	lines_main = file_main.readlines()
	file_main.close()
	
	#removed all duplications in 'input.txt'
	unique_input_rows = set(lines_input)
	input_length = len(lines_input)
	unique_input_length = len(unique_input_rows)

	# removed all duplications in 'main.txt'
	unique_main_rows = set(lines_main)
	main_length = len(lines_main)
	unique_main_length = len(unique_main_rows)
	
	#define amount of unique rows from input in main
	input_main = list(set(unique_main_rows).difference(set(unique_input_rows)))
	input_main_length = len(input_main)

	#store requested data into object
	result = Result(input_length, unique_input_length, main_length, unique_main_length, input_main_length)
	json_string = json.dumps(result.__dict__)

	#overriding files with unique rows and create json file
	with open("input.txt", "w") as text_file:
		text_file.write(''.join(unique_input_rows))
	with open("main.txt", "w") as text_file:
		text_file.write(''.join(unique_main_rows))
	with open("input-main.txt", "w") as text_file:
		text_file.write(''.join(input_main))
	with open("result.json", "w") as text_file:
		text_file.write(json_string)
if __name__ == "__main__":
	main()