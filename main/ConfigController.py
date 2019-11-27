import xml.dom.minidom


class ConfigController:

    @staticmethod
    def get_problem_folder():
        doc = xml.dom.minidom.parse("../config.xml")
        path_to_fullRFLAP = doc.getElementsByTagName("PathToFullRFLAP")
        return path_to_fullRFLAP[0].getAttribute("name")

    @staticmethod
    def get_scene_number():
        doc = xml.dom.minidom.parse("../config.xml")
        problemPath = doc.getElementsByTagName("ProblemPath")
        return problemPath[0].getAttribute("name")

    @staticmethod
    def get_path():
        doc = xml.dom.minidom.parse("../config.xml")
        sceneNumber = doc.getElementsByTagName("SceneNumber")
        return sceneNumber[0].getAttribute("name")
