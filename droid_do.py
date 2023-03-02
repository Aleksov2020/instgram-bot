import os
import time
from Utils.Point import Point

path_to_memu_folder = "D:/Microvirt/MEmu"


def click(x_coordinate: int, y_coordinate: int, device_index: int) -> None:
    """
    :param x_coordinate: point to click x vertex
    :param y_coordinate: point to click y vertex
    :param device_index: index of device, which we want click
    """

    os.system(
        f"D: && cd {path_to_memu_folder} && memuc -i {device_index} adb shell input tap {x_coordinate} {y_coordinate}")
    time.sleep(0.5)


def click_point(point: Point, device_index: int) -> None:
    """
    :param x_coordinate: point to click x vertex
    :param y_coordinate: point to click y vertex
    :param device_index: index of device, which we want click
    """

    os.system(
        f"D: && cd {path_to_memu_folder} && memuc -i {device_index} adb shell input tap {point.x_vertex} {point.y_vertex}")
    time.sleep(0.5)


def swipe(x_coordinate_start: int, y_coordinate_start: int, x_coordinate_end: int, y_coordinate_end: int,
          device_index: int) -> None:
    """
    :param x_coordinate_start:
    :param y_coordinate_start:
    :param x_coordinate_end:
    :param y_coordinate_end:
    :param device_index:
    :return: None
    """
    os.system(
        f'D: && cd {path_to_memu_folder} && memuc -i {device_index} adb shell input touchscreen swipe {x_coordinate_start} {y_coordinate_start} {x_coordinate_end} {y_coordinate_end}')
    time.sleep(1)


def home_button(device_index: int) -> None:
    """
    :param device_index: index of device, which we want to click "Home" button
    :return: none
    """

    os.system(f'D: && cd {path_to_memu_folder} && memuc sendkey -i {device_index} home')
    time.sleep(0.5)


def back_button(device_index: int) -> None:
    """
    :param device_index: index of device, which we want to click "Home" button
    :return: none
    """

    os.system(f'D: && cd {path_to_memu_folder} && memuc sendkey -i {device_index} back')
    time.sleep(0.5)


def input_text(device_index: int, input_text: str) -> None:
    """
    :param device_index:
    :param input_text: text to input in focused field
    :return:
    """

    os.system(f'D: && cd {path_to_memu_folder} && memuc -i {device_index} adb shell input text {input_text}')
    time.sleep(1)

def start_emulator(device_index: int) -> None:
    """
    :param device_index:
    :param input_text: text to input in focused field
    :return:
    """

    os.system(f'D: && cd {path_to_memu_folder} && memuc start -i {device_index}')
    time.sleep(1)
