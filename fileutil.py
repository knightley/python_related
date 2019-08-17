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


def extract_file(fname, dirs):
    """

    :param fname: file to be extracted
    :param dirs: extract file to where
    :return:
    """
    if fname.endswith('.tar') or fname.endswith('.tar.gz') or fname.endswith('.tar.bz2') or fname.endswith(
            '.tar.xz'):
        logging.info("begin to extract tar file %s", fname)
        import tarfile
        t = tarfile.open(fname)
        t.extractall(path = dirs)
        t.close()
        logging.info("end to extract tar file %s", fname)
    elif fname.endswith('.zip'):
        logging.info("begin to extract zip file %s", fname)
        import zipfile
        with zipfile.ZipFile(fname) as z:
            z.extractall(path = dirs)
            z.close()
        logging.info("end to extract zip file %s", fname)
    else:
        logging.warning("Something goes wrong! It shouldn't be here!")
    os.remove(fname)

def package_result(file_path, file_format, result_file):
    """
    :param file_path: directory to be packaged
    :param file_format: which file format need to be packaged into result_file.tar.gz
    :param result_file: package file, result_file.tar.gz
    :return: how many files has been packaged
    """
    file_num = 0
    with tarfile.open(result_file, "w:gz") as tar:
        for root, dirs, files in os.walk(file_path):
            for file in files:
                if file.endswith(file_format) and os.path.join(root, file) != result_file and file != result_file:
                    logging.debug("file %s add to %s", file, result_file)
                    file_num += 1
                    tar.add(os.path.join(root, file))
    return file_num
