import subprocess
import sys

from converter import parser

# from parser import parser as raw_parser

try:
    while True:
        # Function to parse input
        def parse_input(s):
            return parser.parse(s)

        # Example usage
        input_string = input("Input formula : ")
        ast = parse_input(input_string)
        print(ast)

        # Example shell command
        command = "make clean"

        # Run the command
        output = subprocess.run(command, shell=True, capture_output=True, text=True)
except EOFError:
    command = "rm -rf __pycache__"
    output = subprocess.run(command, shell=True, capture_output=True, text=True)
    sys.exit(1)

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
