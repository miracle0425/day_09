from page.searchPage import SearchPage
from page.settingPage import SettingPage


class Page:

    @classmethod
    def get_setting(cls):
        """返回设置页面实例化对象"""
        return SettingPage()

    @classmethod
    def get_search(cls):
        """返回搜索页面实例化对象"""
        return SearchPage()
