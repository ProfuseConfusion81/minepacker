import os
import shutil
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[35m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    print(f'''
{bcolors.OKGREEN}  __  __ _           {bcolors.OKCYAN} _____           _             
{bcolors.OKGREEN} |  \/  (_)          {bcolors.OKCYAN}|  __ \         | |            
{bcolors.OKGREEN} | \  / |_ _ __   ___{bcolors.OKCYAN}| |__) __ _  ___| | _____ _ __ 
{bcolors.OKGREEN} | |\/| | | '_ \ / _ {bcolors.OKCYAN}|  ___/ _` |/ __| |/ / _ | '__|
{bcolors.OKGREEN} | |  | | | | | |  __{bcolors.OKCYAN}| |  | (_| | (__|   |  __| |   
{bcolors.OKGREEN} |_|  |_|_|_| |_|\___{bcolors.OKCYAN}|_|   \__,_|\___|_|\_\___|_|                                                                                                      
{bcolors.ENDC}''')
    PACKLIST = os.listdir('./mypacks')
    SAVELIST = os.listdir('./saves')
    print(f'Found {len(PACKLIST)} datapacks')
    print(f'Found {len(SAVELIST)} saves\n')
    Dict1 = {}
    for i in SAVELIST:
        paths = f'./saves/{str(i)}/datapacks'
        Dict1[f'{str(i)}'] = os.listdir(paths)
 
    Dict2 = {}
    for i in Dict1:
        Dict2[f'{str(i)}'] = []

    for i in Dict1:
        array2 = Dict1[i]
        for x in PACKLIST:
            if x in array2:
                pass
            else:
                Dict2[f'{str(i)}'] += [x]
        array2.clear()
    
    for i in Dict2:
        for j in Dict2[i]:
            try:
                print(f'    {bcolors.WARNING}[ WORKING ]{bcolors.ENDC} COPYING /mypacks/{j} --> /saves/{i}/datapacks/{j}')
                shutil.copy(src=f'./mypacks/{j}', dst=f'./saves/{i}/datapacks/{j}')
                print(f'    {bcolors.OKGREEN}[ SUCCESS ]{bcolors.ENDC} Successfully copied /mypacks/{j} --> /saves/{i}/datapacks/{j}')
            except:
                print(f'    {bcolors.FAIL}[ ERROR ]{bcolors.ENDC} ERROR COPYING /mypacks/{j} --> /saves/{i}/datapacks/{j}')

    print("\n")
    print(f'Finished in %s second(s)' % round((time.time() - start_time), 4))

start_time = time.time()
main()