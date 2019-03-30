import os


def run_all_test():

    current_directory = os.getcwd()
    file_name = os.environ('result_file_name') or "result"
    result_folder_name = os.environ("result_folder_name") or "../" + current_directory

    command = 'pytest' + "../tst" + ' --junit-xml=' + result_folder_name + \
              '/' + file_name + '.xml'
    os.system(command=command)

