"""
Short command for apt update management.
Oishik M | 05 August 2022
"""

import os
import sys

class AU_Runner:
    available_options = [
        '-h',
        '-r',
        '-l',
        '-i',
        '--help'
    ]

    def usage(self):
        print(
            'Usage: au [options]',
            '\nOptions:',
            '\n-h, --help\t\tDisplay this information.',
            '\n-r\t\t\tRefresh available upgrades.',
            '\n-l\t\t\tList available upgrades.',
            '\n-i\t\t\tInstall available upgrades.'            
        )


    def run_au(self, option):
        
        if option == None:
            os.system('apt update && apt upgrade')
        
        elif option == '--help' or option == '-h':
            self.usage()

        elif option == '-r':
            os.system('apt update')

        elif option == '-l':
            os.system('apt list --upgradable')

        elif option == '-i':
            os.system('apt upgrade')

        else:
            print('Error : Check usage.')
            self.usage()


def main(option):
    au_runner = AU_Runner()
    au_runner.run_au(option)

if __name__ == '__main__':
    option = None
    if len(sys.argv) == 2:
        option = sys.argv[1]
    if len(sys.argv) > 2:
        option = "error"
    main(option)
