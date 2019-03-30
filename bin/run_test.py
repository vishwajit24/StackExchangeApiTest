import os


def run_all_test():

    current_directory = os.getcwd()
    file_name = os.environ.get('result_file_name') or "result"
    result_folder_name = os.environ.get("result_folder_name") or "../" + current_directory

    run_command = 'pytest ' + "../tst" + ' --junit-xml=' + result_folder_name + \
              '/' + file_name + '.xml'
    os.system(run_command)


if __name__ == '__main__' :
    run_all_test()

