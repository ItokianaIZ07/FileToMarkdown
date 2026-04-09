from markdown.Markdown import Markdown
import sys

def main():
    args = sys.argv

    if len(args) != 2:
        print("Only 1 file accepted")
        exit(1)
    
    file = args[1]

    if Markdown.isExtensionValid(file):
        Markdown.toMarkdown(file)
    else:
        print("Invalid format, please use .tmd format")

if __name__ == "__main__":
    main()