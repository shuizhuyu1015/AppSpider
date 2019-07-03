"""
    create by Gray 2019-07-02
"""


def get_size(current_driver):
    width = current_driver.get_window_size()["width"]
    height = current_driver.get_window_size()["height"]
    return width, height
