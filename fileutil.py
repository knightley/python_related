# python 3.5.2
import os
import logging


def get_files_size_and_line_number(file_path, file_format):
    """
    return the size and line number of all the files end with file_format in file_path
    :param file_path:
    :param file_format: calculate the file with specific file format
    :return: size and line number of all files with specific file format
    """
    logging.info("[get_file_size_and_line_number] file_path: %s, file_format: %s", file_path, file_format)
    size = 0
    lines = 0
    for root, dirs, files in os.walk(file_path):
        for file in files:
            for one_format in file_format:
                if file.endswith(one_format):
                    size += os.path.getsize(os.path.join(root, file))
                    lines += get_file_lines(os.path.join(root, file))
    return size, lines


def get_file_lines(filename):
    """
    Get number of lines of the file
    :param filename: file path
    :return: the number of lines of the file
    """
    if not os.path.isfile(filename):
        logging.error("[get_file_lines] %s not found", filename)
        return -1

    if not os.access(filename, os.R_OK):
        logging.error("[get_file_lines] %s cannot be read", filename)
        return -1

    i = -1
    with open(filename) as f:
        try:
            for i, l in enumerate(f):
                pass
        except UnicodeDecodeError:
            return -1
    return i + 1
