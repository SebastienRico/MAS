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
    def create_agents(instance, VARIABLE_LIST):
        agents = ET.SubElement(instance, "agents", nbAgents=str(len(VARIABLE_LIST)))
        for v in VARIABLE_LIST:
            ET.SubElement(agents, "agent", name=str("agent" + str(v.variable_id)))
        return agents

    @staticmethod
    def create_domains(instance, DOMAIN_LIST):
        domains = ET.SubElement(instance, "domains", nbDomains=str(len(DOMAIN_LIST)))
        for d in DOMAIN_LIST:
            list = str(d.values_list).replace("[", "").replace("]", "").replace("'", "")
            ET.SubElement(domains, "domain", name=str(d.domain_id), nbValues=str(len(d.values_list))).text = list
        return domains

    @staticmethod
    def create_variables(instance, VARIABLE_LIST):
        variables = ET.SubElement(instance, "variables", nbVariables=str(len(VARIABLE_LIST)))
        for v in VARIABLE_LIST:
            ET.SubElement(variables, "variable", agent=str("agent" + str(v.variable_id)), domain=str(v.domain_id), name=str(v.variable_id))
        return variables

    @staticmethod
    def create_predicates(instance, CONSTRAINT_LIST):
        predicates = ET.SubElement(instance, "predicates", nbPredicates=str(len(CONSTRAINT_LIST)))
        predicateEquivalent = ET.SubElement(predicates, "predicate", name="Equiv")
        predicateGreaterThan = ET.SubElement(predicates, "predicate", name="GreatThan")
        for c in CONSTRAINT_LIST:
            if "=" in c.operator:
                ET.SubElement(predicateEquivalent, "parameters").text = str("int " + c.variable_id + " int " + c.second_variable_id)
                expression = ET.SubElement(predicateEquivalent, "expression")
                ET.SubElement(expression, "functional").text = \
                    "if(eq(abs(sub(" + str(c.variable_id) + "," + str(c.second_variable_id) + "))," + str(c.deviation) + "),0," + str(c.constraint_weight) + ")"
        for c in CONSTRAINT_LIST:
            if ">" in c.operator:
                ET.SubElement(predicateGreaterThan, "parameters").text = str("int " + c.variable_id + " int " + c.second_variable_id)
                expression = ET.SubElement(predicateGreaterThan, "expression")
                ET.SubElement(expression, "functional").text = \
                    "if(gt(abs(sub(" + str(c.variable_id) + "," + str(c.second_variable_id) + "))," + str(c.deviation) + "),0," + str(c.constraint_weight) + ")"
        return predicates

    @staticmethod
    def create_constraints(instance, CONSTRAINT_LIST):
        constraints = ET.SubElement(instance, "constraints", nbConstraints=str(len(CONSTRAINT_LIST)))
        for c in CONSTRAINT_LIST:
            if "=" in c.operator:
                constraint = ET.SubElement(constraints, "constraint", name=str(c.variable_id + "_equiv_" + c.second_variable_id),
                              arity=str(2),
                              scope=str(c.variable_id + " " + c.second_variable_id),
                              reference="Equiv")
                ET.SubElement(constraint, "parameters").text = str(c.variable_id + " " + c.second_variable_id)
            else:
                constraint = ET.SubElement(constraints, "constraint", name=str(c.variable_id + "_greaterThan_" + c.second_variable_id),
                              arity=str(2),
                              scope=str(c.variable_id + " " + c.second_variable_id),
                              reference="GreatThan")
                ET.SubElement(constraint, "parameters").text = str(c.variable_id + " " + c.second_variable_id)
        return constraints

    @staticmethod
    def write_file(instance, problem_name):
        tree = ET.ElementTree(instance)
        tree.write("../" + problem_name + ".xml")

    @staticmethod
    def create_file(problem_name, DOMAIN_LIST, VARIABLE_LIST, CONSTRAINT_LIST):
        instance = ProblemXMLFileController.create_root()
        presentation = ProblemXMLFileController.create_presentation(instance, problem_name)
        agents = ProblemXMLFileController.create_agents(instance, VARIABLE_LIST)
        domains = ProblemXMLFileController.create_domains(instance, DOMAIN_LIST)
        variables = ProblemXMLFileController.create_variables(instance, VARIABLE_LIST)
        predicates = ProblemXMLFileController.create_predicates(instance, CONSTRAINT_LIST)
        constraints = ProblemXMLFileController.create_constraints(instance, CONSTRAINT_LIST)

        ProblemXMLFileController.write_file(instance, problem_name)
