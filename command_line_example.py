# Xcalibyte Vulnerability Static Analyzer Scanner 1.0
# Copyright (c) 2018-2019 Xcalibyte Limited
# Confidential under the terms of the NDA between Xcalibyte and the licensee.
# For the use of the licensee only. Internal use only. No redistribution.

import os
import argparse
import time
import shutil

def _print_err(x):
    print("[ERROR]: " + x)


def _print_info(x):
    print("[INFO]: " + x)


def _print_dbg(x):
    print("[DEBUG]: " + x)

def get_parser():
    parser = argparse.ArgumentParser(description = 'learn how to use parser')

    parser.add_argument('--project-id', '-pid', dest = 'project_id', required = True,
                        help = 'the unique id of the project, will display on UI')
    parser.add_argument('--project-path', '-ppath', dest = 'project_path', required = True,
                        help = 'project source code path')
    parser.add_argument('--server-url', '-surl', dest = 'server_url', required = True,
                        help = 'server url, for example: http://host:port')
    parser.add_argument('--scan-result', '-sr', dest = 'scan_result', metavar = 'xxx.v', required = True,
                        help = '.v scan result file')
    parser.add_argument('--upload-source-code', '-usc', dest = 'upload_source_code', action = 'store_true',
                        default = False, help = 'upload source code to server')
    parser.add_argument('--debug', '-d', dest = 'debug', action = 'store_true',
                        help = 'debug mode')  # not implemented yet
    parser.add_argument('--verbose', '-v', dest = 'verbose', action = 'store_true',
                        help = 'verbose mode')  # not implemented yet
    return parser

def command_line_runner():
    start = time.time()

    parser = get_parser()
    arguments = parser.parse_args()

    server_url = arguments.server_url
    project_id = arguments.project_id
    project_path = arguments.project_path
    scan_result = arguments.scan_result
    upload_source_code = arguments.upload_source_code
    # debug_mode = arguments.debug

    if not os.path.exists(project_path):
        _print_err("%s not exist" % project_path)
        return

    if not os.path.exists(scan_result) or not os.path.isfile(scan_result):
        _print_err("%s not exist or not a file" % scan_result)
        return

    end = time.time()

    _print_info("------------------------------------------------------------------------")
    _print_info("EXECUTION SUCCESS")
    _print_info("------------------------------------------------------------------------")
    _print_info("Total time: %ss" % (end - start))
    _print_info("------------------------------------------------------------------------")
    return


if __name__ == "__main__":
    command_line_runner()
