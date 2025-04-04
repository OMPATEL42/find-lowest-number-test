# The script will find the lowest number in a file and write it to another file.
#
# Run as: python3 find_lowest_number.py <input_file> <output_file>
#
# Example: python3 find_lowest_number.py numbers.txt lowest_number.txt
#
# If python is setup to run as "python" instead of "python3" on the machine, 
# then we should use "python" instead of "python3" in the above.
#
# The input file should contain one number per line. The output file will 
# contain the lowest number.
#
# If the input file is blank, the output file will contain the text: "No 
# numbers found in file".

import sys

def find_lowest_number(input_file, output_file):
    lowest = None

    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    num = float(line)
                    if (lowest is None) or (num < lowest):
                        lowest = num
                except ValueError:
                    pass  # Ignore lines that aren't numbers

    with open(output_file, 'w') as out:
        if lowest is None:
            out.write("No numbers found in file\n")
        else:
            out.write(f"{float(lowest)}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 find_lowest_number.py <input_file> <output_file>")
    else:
        find_lowest_number(sys.argv[1], sys.argv[2])
