import os
import datetime

path = '/Users/baegono/Desktop/Python/PythonBlog/TextFile'

today = datetime.datetime.now()

for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        # 파일 생성 시간 출력
        file_creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        # 파일 경과된 날짜 출력
        days_ago_created = (today - file_creation_date).days
        if days_ago_created > 10:
            print(f"{file_path} : 파일이 삭제됩니다.")
            os.remove(file_path)