import yaml, os


class AnalysisData:
    @classmethod
    def get_yaml_data(cls, name):
        """
        返回yaml文件数据
        :param name: 读取yaml文件名字
        :return:
        """
        with open("./data" + os.sep + name, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def get_excel_data(self):
        """解析excel"""

    def get_db_data(self):
        """解析数据库"""
