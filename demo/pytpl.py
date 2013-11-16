#!/usr/bin/python v3.3.0
#pyTpl.py
#vim ~/.bashrc; alias pyfile="python pytpl.py" 

import sys 
from string import Template


def main():
    '''create a template python file'''
    if len(sys.argv) < 2:
        print('Invalid input, at least two parameters!')
        raise SystemExit

    tpl = '''#!{0} v{1} 
#{2}.py
#{3}
    
def main():
    pass
    
if __name__ == '__main__':
    main()'''

    content = tpl.format('/usr/bin/python', 
                         sys.version.split(' ')[0], 
                         sys.argv[1] if len(sys.argv) > 1 else 'newfile',
                         ' '.join(sys.argv[2:]) if len(sys.argv) > 2 else 'something_about_this_file')
    #print(content)
    f = open(sys.argv[1] + '.py', 'x')
    f.write(content)
    f.close()
    print('The operation was successful')
            
if __name__ == '__main__':
        main()
            
