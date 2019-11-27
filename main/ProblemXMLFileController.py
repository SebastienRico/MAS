import xml.etree.cElementTree as ET


class ProblemXMLFileController:

    @staticmethod
    def create_root():
        instance = ET.Element("instance")
        return instance

    @staticmethod
    def create_presentation(instance, problem_name):
        presentation = ET.SubElement(instance, "presentation", name=str(problem_name), maxConstraintArity="2", maximize="false", format="XCSP 2.1_FRODO")
        return presentation

    @staticmethod
    def create_agents(instance):
        agent = ""
        return agent

    @staticmethod
    def create_variables(instance):
        variables = ""
        return variables

    @staticmethod
    def create_domains(instance, DOMAIN_LIST):
        domains = ET.SubElement(instance, "nbAgents", nbDomains=str(len(DOMAIN_LIST)))
        for d in DOMAIN_LIST:
            list = str(d.values_list).replace("[", "").replace("]", "").replace("'", "")
            ET.SubElement(domains, "domain", name=str(d.domain_id), nbValues=str(len(d.values_list))).text = list
        return domains

    @staticmethod
    def create_relations(instance):
        relations = ""
        return relations

    @staticmethod
    def create_probabilities(instance):
        probabilities = ""
        return probabilities

    @staticmethod
    def create_constraints(instance):
        constraints = ""
        return constraints

    @staticmethod
    def write_file(instance, problem_name):
        tree = ET.ElementTree(instance)
        tree.write("../out/" + problem_name + ".xml")

    @staticmethod
    def create_file(problem_name, DOMAIN_LIST):
        instance = ProblemXMLFileController.create_root()
        presentation = ProblemXMLFileController.create_presentation(instance, problem_name)
        #agents = ProblemXMLFileController.create_agents(instance)
        domains = ProblemXMLFileController.create_domains(instance, DOMAIN_LIST)
        #variables = ProblemXMLFileController.create_variables(instance)
        #realations = ProblemXMLFileController.create_relations(instance)
        #probabilities = ProblemXMLFileController.create_probabilities(instance)
        #constraints = ProblemXMLFileController.create_constraints(instance)

        ProblemXMLFileController.write_file(instance, problem_name)
