import asyncio
import ctypes
import json
import os
import random
import tkinter
from tkinter import filedialog
from InquirerPy import inquirer
from InquirerPy.separator import Separator
import colorama

import requests
from colorama import Fore, Style

import checker
from codeparts import checkers, systems, validsort
from codeparts.systems import system

check = checkers.checkers()
sys = systems.system()
valid = validsort.validsort()


class program():
    def __init__(self) -> None:
        self.count = 0
        self.checked = 0
        self.version = '3.15.2'
        self.riotlimitinarow = 0
        path = os.getcwd()
        self.parentpath = os.path.abspath(os.path.join(path, os.pardir))
        try:
            self.lastver = requests.get(
                'https://api.github.com/repos/lil-jaba/valchecker/releases').json()[0]['tag_name']
        except:
            self.lastver = self.version

    def start(self):
        try:
            print('Cursor Checker is checking Internet Connection')
            requests.get('https://github.com')
        except requests.exceptions.ConnectionError:
            print('No internet connection was detected by Cursor Checker')
            os._exit(0)
        os.system('cls')
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color not in ['BLACK']]
        colored_name = [random.choice(colors) + char for char in f'CursorBeta by ParvXDD']
        print(f'''
 ██████╗██╗   ██╗██████╗ ███████╗ ██████╗ ██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██║   ██║██╔══██╗██╔════╝██╔═══██╗██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║     ██║   ██║██████╔╝███████╗██║   ██║██████╔╝    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║     ██║   ██║██╔══██╗╚════██║██║   ██║██╔══██╗    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝██║  ██║███████║╚██████╔╝██║  ██║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                           ⇜ Made By ParvXDD ⇝
                                      ↬ https://discord.gg/cursor ↫                               
                                         « Discord ID: its.parv » ''')
        print()
        r = requests.get('https://api.github.com/repos/lil-jaba/valchecker4')
        try:
            r.json()['message']
        except:
            print(sys.center(f'{Fore.GREEN}Good news! CursorBeta is out!'))
            print(sys.center(f'{Fore.GREEN}Please join the Discord Server to use!'))
            print(sys.center(f'{Fore.GREEN}https://discord.gg/cursor{Fore.WHITE}'))
        if 'devtest' in self.version:
            print(sys.center(f'{Fore.YELLOW}Greetings from ParvXDD'))
        elif 'beta' in self.version:
            print(sys.center(f'{Fore.YELLOW}You have downloaded the BETA version. It can work unstable and contain some bugs.'))
            print(sys.center(f'Join https://discord.gg/cursor to download the latest stable release{Fore.RESET}'))
        elif self.lastver != self.version:
            print(sys.center(
                f'\nnext version {self.lastver} is available!'))
            if inquirer.confirm(
                message="{}Would you like to download it now?".format(system.get_spaces_to_center('Would you like to download it now? (Y/n)')), default=True,qmark=''
            ).execute():
                os.system(f'{self.parentpath}/updater.bat')
                os._exit(0)
        menu_choices = [
            Separator(),
            '➤ Start Cursor Checker',
            '➤ Single-Account Checker',
            '➤ Edit Cursor Settings',
            '➤ Sort the Working Accounts',
            '➤ Test the Selected Proxies',
            f'https://discord.gg/cursor',
            Separator(),
            'Close Cursor Checker'
        ]
        print(sys.center(' '))
        res = inquirer.select(
            message="» Select The Feature You Wish To Use:",
            choices=menu_choices,
            default=menu_choices[0],
            pointer='➠',
            qmark=''
        ).execute()
        if res == menu_choices[1]:
            self.main()
            input('» Cursor Checker Has Finished Checking. Press ENTER to exit the Checker')
            pr.start()
        elif res == menu_choices[2]:
            slchecker = checker.singlelinechecker()
            slchecker.main()
            pr.start()
        elif res == menu_choices[3]:
            sys.edit_settings()
            pr.start()
        elif res == menu_choices[4]:
            valid.customsort()
            input('Done. Press ENTER to exit Cursor Checker')
            pr.start()
        elif res == menu_choices[5]:
            sys.checkproxy()
            pr.start()
        elif res == menu_choices[6]:
            os.system('cls')
            print(f'''
    [⤲] ➨ Cursor Checker v{self.version} by ParvXDD

    If you have any questions about valchecker's source code, feel free to ask me in discord
    https://discord.gg/cursor (its.parv)

    You can also open pull requests if you have some updates, I will check them all

    Happy coding :)

  [⤲] ➨ Press the ENTER key to Return!
            ''')
            input()
            pr.start()
        elif res == menu_choices[8]:
            os._exit(0)

    def get_accounts(self):
        root = tkinter.Tk()
        file = filedialog.askopenfile(parent=root, mode='rb', title='» Select the Accounts File to be checked (login:password)',
                                      filetype=(("txt", "*.txt"), ("All files", "*.txt")))
        root.destroy()
        os.system('cls')
        if file == None:
            os._exit(0)
        filename = str(file).split("name='")[1].split("'>")[0]
        with open(str(filename), 'r', encoding='UTF-8', errors='replace') as file:
            lines = file.readlines()
            ret = []
            if len(lines) > 100000:
                if inquirer.confirm(
                    message=f"You have more than 100k accounts ({len(lines)}). Do you want to skip the sorting part? [Skipping is Recommended]",
                    default=True,
                    qmark='!',
                    amark='!'
                ).execute():
                    self.count = len(lines)
                    return lines
            for logpass in lines:
                logpass = logpass.strip()
                # remove doubles
                if logpass not in ret and ':' in logpass:
                    self.count += 1
                    ctypes.windll.kernel32.SetConsoleTitleW(
                        f'Cursor Checker {self.version} by ParvXDD | Loading the selected Valorant Accounts ({self.count})')
                    ret.append(logpass)
            return ret

    def main(self):
        ctypes.windll.kernel32.SetConsoleTitleW(
            f'Cursor Checker {self.version} by ParvXDD | Cursor Checker is Loading the Settings')
        print('⤄ Cursor Checker is Loading the Settings')
        settings = sys.load_settings()

        ctypes.windll.kernel32.SetConsoleTitleW(
            f'Cursor Checker {self.version} by ParvXDD | Cursor Checker is Loading the Selected Proxies')
        print('⤄ Cursor Checker is Loading the Selected Proxies')
        proxylist = sys.load_proxy()

        if proxylist == None:
            path = os.getcwd()
            file_path = f"{os.path.abspath(os.path.join(path, os.pardir))}\\proxy.txt"

            print(Fore.YELLOW, end='')
            response = input('No amount of proxies have been selected. Do you want Cursor Checker to scrape Proxies? (y/n): ')
            print(Style.RESET_ALL, end='')

            if response.lower() == 'y':
                f = open('system\\settings.json', 'r+')
                data = json.load(f)
                proxyscraper = data['proxyscraper']
                f.close()

                # Scrape proxies
                url = proxyscraper
                proxies = requests.get(url).text.split('\r\n')

                # Save proxies to file
                with open(file_path, 'w') as f:
                    f.write("\n".join(proxies))

                # Print number of proxies saved
                num_proxies = len(proxies)
                print(f'{num_proxies} Selected Proxies have been saved to "proxy.txt" file.')
                proxylist = sys.load_proxy()
            else:
                print('⇔ Cursor Checker is Running without Proxies')

        if inquirer.confirm(
            message="⟳ Do you wish to check Default Accounts of Cursor Checker!", default=True
        ).execute():
            root = tkinter.Tk()
            file = filedialog.askopenfile(parent=root, mode='rb', title='» Select the file which has to be checked (login:password)',
                                          filetype=(("vlchkr", "*.vlchkr"), ("All files", "*.vlchkr")))
            root.destroy()
            if file == None:
                filename = 'None'
            else:
                filename = str(file).split("name='")[1].split("'>")[0]
                valkekersource = systems.vlchkrsource(filename)
                accounts=None
        else: 
            valkekersource = None
            ctypes.windll.kernel32.SetConsoleTitleW(
                f'CursorBeta {self.version} by ParvXDD | Loading the Selected Accounts')
            print('Accounts are being loaded in the Checker')
            accounts = self.get_accounts()

        print('≠ Cursor Checker is Loading the Assets')
        ctypes.windll.kernel32.SetConsoleTitleW(
            f'CursorBeta {self.version} by ParvXDD | Loading the necessary Assets')
        sys.load_assets()

        print('⟴ Cursor Checker is Loading Itself!')
        ctypes.windll.kernel32.SetConsoleTitleW(
            f'CursorBeta {self.version} by ParvXDD | Loading Cursor Checker')
        scheck = checker.simplechecker(settings, proxylist, self.version)
        asyncio.run(scheck.main(accounts, self.count, valkekersource))
        return


pr = program()
if __name__ == '__main__':
    print('⟴ Cursor Checker is Starting Itself!')
    pr.start()
