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


def open_files_ctr():
    ctr_file = open(PATH_TO_FULLRFLAP + "FullRLFAP/" + PROBLEM_FOLDER + "/scen" + SCENE_NUMBER + "/ctr.txt", "r")
    global CONSTRAINT_LIST
    CONSTRAINT_LIST = ParserCTR.parse_ctr_file(ctr_file)
    ctr_file.close()


def open_files_dom():
    dom_file = open(PATH_TO_FULLRFLAP + "FullRLFAP/" + PROBLEM_FOLDER + "/scen" + SCENE_NUMBER + "/dom.txt", "r")
    global DOMAIN_LIST
    DOMAIN_LIST = ParserDOM.parse_dom_file(dom_file)
    dom_file.close()


def open_files_var():
    var_file = open(PATH_TO_FULLRFLAP + "FullRLFAP/" + PROBLEM_FOLDER + "/scen" + SCENE_NUMBER + "/var.txt", "r")
    global VARIABLE_LIST
    VARIABLE_LIST = ParserVAR.parse_var_file(var_file)
    var_file.close()


def create_XML_file():
    ProblemXMLFileController.create_file(PROBLEM_FOLDER + "_scen" + SCENE_NUMBER, DOMAIN_LIST, VARIABLE_LIST, CONSTRAINT_LIST)


def main():
    print("Hello Céline !")
    get_config()
    open_files_ctr()
    open_files_dom()
    open_files_var()
    create_XML_file()


if __name__ == "__main__":
    main()
