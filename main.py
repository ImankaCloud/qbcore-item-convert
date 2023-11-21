def format_line(line):
    formatted_line = line.replace("['", "").replace("']", "")
    return formatted_line

def format_items(input_file_path, output_file_path):
    try:
        try:
            with open(input_file_path, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            with open(input_file_path, 'w') as file:
                file.write('')
            return "Input file not found. A new file has been created.\nInput your current items into input.lua."

        modified_lines = [format_line(line) for line in lines]

        with open(output_file_path, 'w') as output_file:
            for line in modified_lines:
                output_file.write(line)

        return "Items written to output.txt successfully."
    except Exception as error:
        return f"Error: {error}"

input_file_path = 'input.txt'
output_file_path = 'output.txt'

result = format_items(input_file_path, output_file_path)
print(result)
