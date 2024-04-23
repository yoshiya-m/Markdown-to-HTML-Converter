# python3 file-converter.py markdown inputfile outputfile
import sys
import markdown
# html = markdown.markdown(your_text_string)

if len(sys.argv) < 4:
    print(str(4 - len(sys.argv)) + ' more arguments needed')
    exit()

command = sys.argv[1]
if command != "markdown":
    print('no such command "' + command + '"')
    exit()

inputFile = sys.argv[2]

with open(inputFile) as f:
    contents = f.read()

html = markdown.markdown(contents)
outputFile = sys.argv[3]

with open(outputFile, 'w') as f:
    f.write(html)

