# -*-coding:Latin-1 -*
import null

from main.Constraint import Constraint

class ParserCTR:

    def __init__(self):
        """constructeur vide"""

    def parse_ctr_file(self, ctr_file):
        ctr_content = ctr_file.read()
        content_splited = ctr_content.split("\n")
        constraint_list = []
        for line in content_splited:
            line_splited = line.split()
            if len(line_splited) != 0:
                constraint = Constraint()
                constraint.variable_id = line_splited[0]
                constraint.second_variable_id = line_splited[1]
                constraint.constrainte_type = line_splited[2]
                constraint.operator = line_splited[3]
                constraint.deviation = line_splited[4]
                if len(line_splited) > 5:
                    constraint.constrainte_weight = line_splited[5]
                constraint_list.insert(len(constraint_list), constraint)
