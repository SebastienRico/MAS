# -*-coding:Latin-1 -*
import null

from main.Constrainte import Constrainte

class ParserCTR:

    def __init__(self):
        """constructeur vide"""

    def parse(self, ctr_file):
        ctr_content = ctr_file.read()
        content_splited = ctr_content.split("\n")
        constrainte_list = []
        for line in content_splited:
            line_splited = line.split()
            if len(line_splited) != 0:
                constrainte = Constrainte()
                constrainte.variable_id = line_splited[0]
                constrainte.second_variable_id = line_splited[1]
                constrainte.constrainte_type = line_splited[2]
                constrainte.operator = line_splited[3]
                constrainte.deviation = line_splited[4]
                if len(line_splited) > 5:
                    constrainte.constrainte_weight = line_splited[5]
                constrainte_list.insert(len(constrainte_list), constrainte)
        print("nb contraintes : " + str(len(constrainte_list)))