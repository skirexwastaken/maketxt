from pathlib import Path
import sys

def main():
    if len(sys.argv) > 1:
        with open(f"{Path.cwd()}/{sys.argv[1]}.txt","w") as file:
            if len(sys.argv) == 2:
                file.write("")
    
                print(f"File '{sys.argv[1]}.txt' has been created.")
    
            else:
                textLine = " ".join(sys.argv[2:])
                textLines = textLine.split("/")
    
                for textLine in textLines:
                    file.write(f"{textLine}\n")
    
                print(f"File '{sys.argv[1]}.txt' has been created with content {textLines}.")
    else:
        print("Invalid filename.")
