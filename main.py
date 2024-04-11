"""
Created by: Charlie Doherty and Jonathan Gott
HackKU - University of Kansas
4/11/2024

Run the main function in this file to begin the program
"""
from baseconverter import base_converter

if __name__ == "__main__":

    print("Hello, welcome to our base conversion project for HackKU")
    # Use input to force an input to continue
    input("Press 'enter' to continue...\n")

    in_base = 10
    in_number = int(input("What number would you like to translate: "))
    out_base = int(input(f"What base would you like to convert {in_number} to: "))

    out_number = base_converter(in_base, in_number, out_base)

    print(f"Base {in_base}: {in_number}\n"
          f"Base {out_base}: {out_number}")
