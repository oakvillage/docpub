import sys, json
from jsonschema import validate, ValidationError

def main():
    args = sys.argv
    contents = getJsonFromArgs(args)
    # jsonが取得できたか確認
    if contents is None:
        sys.exit('json error.')
    

    with open('schema.json') as schemaObj:
        schema = json.load(schemaObj)
        try:
            validate(contents, schema)
            output_files(contents)
        except ValidationError as e:
            print(json validate error)


# 取得したjsonからファイル情報を読み込み
# 指定のディレクトリへ出力する
def output_files(file_info):
    for info in file_info:
        

# コマンドライン引数からjsonを取得する
def getJsonFromArgs(args):
    if 2 == len(args):
        try:
            json = json.loads(args[1])
            return json
        except json.JSONDecodeError as e:
            print(e)
    else:
        print('Argments are not valid.')
    return None

# メイン処理
if __name__ == '__main__':
    main()
