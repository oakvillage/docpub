import sys, json

def output_files(file_info):
    print(json.dumps(file_info))

if __name__ == '__main__':
    args = sys.argv
    raw_file_info = args[1]
    file_info = json.loads(raw_file_info)
    output_files(file_info)
