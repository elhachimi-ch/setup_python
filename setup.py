import csv
import os
import re

BASE_NAME = os.path.abspath('.')


def read_commandes_list(delimiter=','):
    with open(os.path.join(BASE_NAME, 'data/commandes.csv'), 'r+', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=delimiter)
        return list(reader)


def set_pip_version(o, pip):
    return re.sub('pip', pip, o, 1)


class Setup:
    __commandes = []

    def __init__(self, pip='', python_version=''):
        self.read_commandes_list()
        commandes = self.get_commandes()
        if len(python_version) != 0:
            commandes[1] = re.sub('python', 'python3.6', commandes[1][0])
        if len(pip) != 0:
            for i in range(len(commandes)):
                commandes[i][0] = set_pip_version(commandes[i][0], pip)
        print("""
     _______. _______ .___________. __    __  .______   
    /       ||   ____||           ||  |  |  | |   _  \  
   |   (----`|  |__   `---|  |----`|  |  |  | |  |_)  | 
    \   \    |   __|      |  |     |  |  |  | |   ___/  
.----)   |   |  |____     |  |     |  `--'  | |  |      
|_______/    |_______|    |__|      \______/  | _|      
""")

    def get_commandes(self):
        return self.__commandes

    def set_commandes(self, new_commandes_list):
        self.__commandes = new_commandes_list

    @staticmethod
    def add_command(new_command):
        new_command = [new_command, 0]
        with open(os.path.join(BASE_NAME, 'data/commandes.csv'), 'a+', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(new_command)

    def read_commandes_list(self, delimiter=','):
        with open(os.path.join(BASE_NAME, 'data/commandes.csv'), 'r+', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=delimiter)
            self.set_commandes(list(reader))

    def update_commandes_list(self, file_name=os.path.join(BASE_NAME, 'data/commandes.csv'), delimiter=','):
        with open(file_name, 'w+', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=delimiter)
            for p in self.get_commandes():
                writer.writerow(p)

    def start(self, updtae=False, mac=0):
        commandes = list(self.get_commandes())
        for i in range(len(commandes)):
            os.system(commandes[i][0])
            commandes[i][1] = 1
        if mac == 1:
            os.system('pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.0-py3-none-any.whl')
        else:
            os.system('pip install --upgrade --ignore-installed tensorflow==1.5')
        os.system('rm -r get-pip.py')
        if updtae:
            self.__commandes.pop(0)
            self.__commandes.insert(0, ['commande', 'status'])
            self.update_commandes_list()
        print("""
 _______   ______   .__   __.  _______ 
|       \ /  __  \  |  \ |  | |   ____|
|  .--.  |  |  |  | |   \|  | |  |__   
|  |  |  |  |  |  | |  . `  | |   __|  
|  '--'  |  `--'  | |  |\   | |  |____ 
|_______/ \______/  |__| \__| |_______|
""")
