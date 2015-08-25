import os
import shutil

def main():
    txt = os.environ['HOME'] + '/.zshrc'
    baktxt = os.environ['HOME'] + '/.zshrc.bak'
    tmptxt = os.environ['HOME'] + '/.zshrc.tmp'

    with open(tmptxt, 'w') as outfile:
        with open(txt, 'r') as infile:
            rowIter= iter(infile)
            for row in rowIter:
                if row.startswith('#anaena'): # Start of next section
                    outfile.write('anaena\n')
                else:
                    outfile.write(row)
    os.remove(baktxt)
    shutil.copy2(txt, baktxt)
    os.remove(txt)
    shutil.move(tmptxt, txt)

if __name__ == '__main__':
    main()

