# -*-coding:Latin-1 -*
import null

from main.Domain import Domain

class ParserDOM:

    def __init__(self):
        """constructeur vide"""

    def parse_dom_file(self, dom_file):
        dom_content = dom_file.read()
        content_splited = dom_content.split("\n")
        domain_list = []
        for line in content_splited:
            line_splited = line.split()
            domain = Domain()
            if len(line_splited) > 3:
                domain.domain_id = line_splited[0]
                domain.cadinality = line_splited[1]
                domain.values_list = line_splited[2:]
                domain_list.insert(len(domain_list), domain)
