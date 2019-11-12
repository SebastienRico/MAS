# -*-coding:Latin-1 -*
from main.ParserCTR import ParserCTR
from main.ParserDOM import ParserDOM
from main.ParserVAR import ParserVAR

def open_files_ctr():
    ctr_file = open("../../FullRLFAP/CELAR/scen01/ctr.txt", "r")
    parser_CTR = ParserCTR()
    parser_CTR.parse_ctr_file(ctr_file)
    ctr_file.close()

def open_files_dom():
    dom_file = open("../../FullRLFAP/CELAR/scen01/dom.txt", "r")
    parser_DOM = ParserDOM()
    parser_DOM.parse_dom_file(dom_file)
    dom_file.close()

def open_files_var():
    var_file = open("../../FullRLFAP/CELAR/scen01/var.txt", "r")
    parser_VAR = ParserVAR()
    parser_VAR.parse_var_file(var_file)
    var_file.close()

def main():
    print("Hello Céline !")
    open_files_ctr()
    open_files_dom()
    open_files_var()

if __name__ == "__main__":
    main()