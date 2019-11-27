# -*-coding:Latin-1 -*
import null

from main.Variable import Variable


class ParserVAR:

    @staticmethod
    def parse_var_file(var_file):
        var_content = var_file.read()
        content_splited = var_content.split("\n")
        variable_list = []
        for line in content_splited:
            line_splited = line.split()
            if len(line_splited) != 0:
                variable = Variable()
                variable.variable_id = line_splited[0]
                variable.domain_id = line_splited[1]
                if len(line_splited) >= 3:
                    variable.initial_value = line_splited[2]
                elif len(line_splited) == 4:
                    variable.modif_cost = line_splited[3]
                variable_list.insert(len(variable_list), variable)
        return variable_list
