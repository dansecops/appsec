#!/usr/bin/env python
import sys,os, unittest
from urllib.parse import quote



def main():
    if len(sys.argv) != 3:
        print('usage url_encoder-file <input> <output>')
        sys.exit(2)

    print("Running url encoder...")
    with open(sys.argv[1]) as f1:
        content = f1.readlines()
        try:
            os.remove(sys.argv[2])
        except OSError:
            print("Could not remove file!")
        with open(sys.argv[2], 'w') as f2:
            for line in content:
                line = line.replace('\n', '')
                encodedLine = quote(line)
                f2.write(encodedLine + "\n")
            print("Done")

def testMainMethod():
    testFileName = "testInput.txt"
    testFileNameOut = "testOutput.txt"
    try:
        os.remove(testFileName)
        os.remove(testFileNameOut)
    except OSError:
        pass

    with open(testFileName, 'w') as testFile:
        testFile.write('\"\' and --#\n')
        testFile.write('\"\' or --#')
    with open(testFileNameOut, 'w') as testFileOut:
        testFileOut.write("output to be overriden")

    sys.argv[1] = testFileName
    sys.argv[2] = testFileNameOut
    main()

    with open(testFileNameOut) as testFile:
        lines = testFile.readlines()
        assert len(lines) == 2
        assert lines[0] == '%22%27%20and%20--%23\n'
        assert lines[1] == '%22%27%20or%20--%23\n'

if __name__  == "__main__": testMainMethod()