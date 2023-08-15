import json

# JSON 파일 경로
json_file_path = 'crawl_yhn.json'  # JSON 파일 경로 수정

# 쓸 파일 경로
output_file_path = 'parsed_output.json'  # 출력 파일 경로 수정

# JSON 파일 열기
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# 파싱 및 출력 파일 생성
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for item in data:
        parsed_item = [
            {"index": {"_index": "crawl", "_id": item["_id"]}},
            {"writer": item["writer"],"write_date": item["write_date"],"category_one_depth": item["category_one_depth"],"category_two_depth": item["category_two_depth"],"title": item["title"],"url": item["url"],"thumbnail_url": item["thumbnail_url"],"contents": item["contents"]}

        ]

        for item in parsed_item:
            output_file.write(json.dumps(item, ensure_ascii=False) + '\n')


print("Parsing and output complete.")

