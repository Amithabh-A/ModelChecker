import subprocess

from converter import parser

# from parser import parser as raw_parser

while True:
    # Function to parse input
    def parse_input(s):
        return parser.parse(s)

    # Example usage
    input_string = input("Input formula : ")
    ast = parse_input(input_string)
    print(ast)

    # Example shell command
    command = "./del.sh"

    # Run the command
    output = subprocess.run(command, shell=True, capture_output=True, text=True)

#
# # Check if the command executed successfully
# if output.returncode == 0:
#     print("Command executed successfully!")
#     # Print the output
#     print("Output:")
#     print(output.stdout)
# else:
#     print("Error executing command:")
#     # Print the error message
#     print(output.stderr)
