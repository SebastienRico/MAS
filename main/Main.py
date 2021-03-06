# -*-coding:Latin-1 -*
from main.ParserCTR import ParserCTR
from main.ParserDOM import ParserDOM
from main.ParserVAR import ParserVAR
from main.ConfigController import ConfigController
from main.ProblemXMLFileController import ProblemXMLFileController


def get_config():
    global PATH_TO_FULLRFLAP
    PATH_TO_FULLRFLAP = ConfigController.get_problem_folder()
    global PROBLEM_FOLDER
    PROBLEM_FOLDER = ConfigController.get_scene_number()
    global SCENE_NUMBER
    SCENE_NUMBER = ConfigController.get_path()


def open_files_ctr(i):
    ctr_file = open(PATH_TO_FULLRFLAP + "FullRLFAP/" + PROBLEM_FOLDER + "/scen" + i + "/ctr.txt", "r")
    global CONSTRAINT_LIST
    CONSTRAINT_LIST = ParserCTR.parse_ctr_file(ctr_file)
    ctr_file.close()


def open_files_dom(i):
    dom_file = open(PATH_TO_FULLRFLAP + "FullRLFAP/" + PROBLEM_FOLDER + "/scen" + i + "/dom.txt", "r")
    global DOMAIN_LIST
    DOMAIN_LIST = ParserDOM.parse_dom_file(dom_file)
    dom_file.close()


def open_files_var(i):
    var_file = open(PATH_TO_FULLRFLAP + "FullRLFAP/" + PROBLEM_FOLDER + "/scen" + i + "/var.txt", "r")
    global VARIABLE_LIST
    VARIABLE_LIST = ParserVAR.parse_var_file(var_file)
    var_file.close()


def create_XML_file(i):
    ProblemXMLFileController.create_file(PROBLEM_FOLDER + "_scen" + i, DOMAIN_LIST, VARIABLE_LIST, CONSTRAINT_LIST)


def main():
    print("Hello C�line !")
    get_config()
    list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]
    for i in list:
        open_files_ctr(i)
        open_files_dom(i)
        open_files_var(i)
        create_XML_file(i)


if __name__ == "__main__":
    main()
