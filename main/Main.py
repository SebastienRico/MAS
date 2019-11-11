# -*-coding:Latin-1 -*
from main.ParserCTR import ParserCTR

def open_files_ctr():
    ctr_file = open("../../FullRLFAP/CELAR/scen01/ctr.txt", "r")
    parser_CTR = ParserCTR()
    parser_CTR.parse(ctr_file)
    ctr_file.close()

def main():
    print("Hello Céline !")
    open_files_ctr()

if __name__ == "__main__":
    main()