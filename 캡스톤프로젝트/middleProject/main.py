#데이터셋 전처리

# 데이터셋 압출 파일 풀기
def unZip():
    import zipfile
    import os

    # 압축 파일이 들어 있는 루트 폴더
    camera_root = "C:/Users/User/PycharmProjects/Fall Dectection/data/Trial2Zip"

    # 압축 해제 결과를 저장할 루트 폴더
    extract_root = "C:/Users/User/PycharmProjects/Fall Dectection/data/Trial2"

    # 모든 Subject 폴더 순회
    for subject_folder in os.listdir(camera_root):
        subject_path = os.path.join(camera_root, subject_folder)

        if not os.path.isdir(subject_path):
            continue

        # Subject 폴더 안의 zip 파일 순회
        for file in os.listdir(subject_path):
            if file.lower().endswith(".zip"):
                zip_path = os.path.join(subject_path, file)

                # 압축 해제 폴더명 = zip 이름과 동일
                folder_name = os.path.splitext(file)[0]
                extract_path = os.path.join(extract_root, subject_folder, folder_name)

                os.makedirs(extract_path, exist_ok=True)
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)

                print(f"✅ {zip_path} → {extract_path} 압축 해제 완료")

# 데이터셋을 알파포즈 모델에 돌려 각 프레임별 JSON OUTPUT 생성
def getAlpaPoseJson():
    import os
    import subprocess

    # AlphaPose 설치 경로
    ALPHAPOSE_DIR = r"C:\Users\User\PycharmProjects\Fall Dectection\AlphaPose"
    ALPHAPOSE_SCRIPT = os.path.join(ALPHAPOSE_DIR, "scripts", "demo_inference.py")
    POSE_CFG = os.path.join(ALPHAPOSE_DIR, "configs", "coco", "resnet", "256x192_res50_lr1e-3_1x.yaml")
    POSE_MODEL = os.path.join(ALPHAPOSE_DIR, "pretrained_models", "fast_res50_256x192.pth")
    POSE_BATCH = "32"

    # 입력 및 출력 루트 경로
    input_root = r"C:\Users\User\PycharmProjects\Fall Dectection\data\Trial2"
    output_root = r"C:\Users\User\PycharmProjects\Fall Dectection\data\Trial2Json"

    # Subject 폴더 순회
    for subject in os.listdir(input_root):
        subject_path = os.path.join(input_root, subject)
        if not os.path.isdir(subject_path):
            continue

        for activity_folder in os.listdir(subject_path):
            activity_path = os.path.join(subject_path, activity_folder)
            if not os.path.isdir(activity_path):
                continue

            # 출력 경로 지정
            output_path = os.path.join(output_root, activity_folder)
            os.makedirs(output_path, exist_ok=True)

            # 명령어 구성
            command = [
                "python", ALPHAPOSE_SCRIPT,
                "--cfg", POSE_CFG,
                "--checkpoint", POSE_MODEL,
                "--indir", activity_path,
                "--outdir", output_path,
                "--posebatch", POSE_BATCH
            ]

            print(f" AlphaPose 실행: {activity_path}")
            subprocess.run(command, cwd=ALPHAPOSE_DIR)

def fileNameModify():
    import os
    import shutil

    # 원본 폴더
    source_root = r"C:\Users\User\PycharmProjects\Fall Dectection\data\Trial2Csv"

    # 대상 폴더
    destination = r"C:\Users\User\PycharmProjects\Fall Dectection\data\csv"

    # 대상 폴더가 없다면 생성
    os.makedirs(destination, exist_ok=True)

    # source_root 내의 모든 디렉토리를 탐색
    for subject_folder in os.listdir(source_root):
        subject_path = os.path.join(source_root, subject_folder)

        if os.path.isdir(subject_path):
            for file_name in os.listdir(subject_path):
                file_path = os.path.join(subject_path, file_name)

                if os.path.isfile(file_path):
                    # 'Trial2'가 파일명에 있다면 제거
                    new_file_name = file_name.replace("Trial2", "")
                    new_file_path = os.path.join(destination, new_file_name)

                    # 파일 이동
                    shutil.move(file_path, new_file_path)

    print("Trial2 제거 후 csv 폴더로 파일 이동 완료!")

def jsonFileMove():
    import os
    import shutil

    # 원본 루트 폴더
    source_root = r"C:\Users\User\PycharmProjects\Fall Dectection\data\Trial2Json"

    # 결과 저장할 폴더
    destination = r"C:\Users\User\PycharmProjects\Fall Dectection\data\json"

    # 목적지 폴더 생성 (없으면)
    os.makedirs(destination, exist_ok=True)

    # 모든 서브 폴더 탐색
    for folder_name in os.listdir(source_root):
        folder_path = os.path.join(source_root, folder_name)

        # 폴더인지 확인
        if os.path.isdir(folder_path):
            # alphapose-results.json 파일 경로
            json_file_path = os.path.join(folder_path, "alphapose-results.json")

            if os.path.isfile(json_file_path):
                # 'Trial2Camera1' 기준으로 앞부분 잘라서 새 파일 이름 만들기
                # new_file_name = folder_name.split("Trial2Camera1")[0] + ".json"
                destination_path = os.path.join(destination, folder_name)

                # 파일 복사 (이동하고 싶으면 shutil.move 사용)
                shutil.copy(json_file_path, destination_path)

    print("파일 이름 변경 후 json 폴더로 복사 완료!")

# 이미지 내 SCORE가 높은 골격만 남기고 제거
def jsonFiltering():
    import os
    import json
    from collections import defaultdict

    # JSON 파일이 들어있는 폴더
    json_dir = r"C:\Users\User\PycharmProjects\Fall Dectection\data\json"

    # 폴더 내 모든 JSON 파일 순회
    for filename in os.listdir(json_dir):
        if not filename.endswith(".json"):
            continue

        file_path = os.path.join(json_dir, filename)

        # JSON 로드
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # image_id 기준으로 그룹핑
        grouped = defaultdict(list)
        for item in data:
            grouped[item["image_id"]].append(item)

        # score 기준으로 최고 항목만 추출
        filtered_data = []
        for image_id, items in grouped.items():
            if len(items) == 1:
                filtered_data.append(items[0])
            else:
                best = max(items, key=lambda x: x.get("score", 0))
                filtered_data.append(best)

        # 덮어쓰기 저장
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(filtered_data, f, indent=2)

        print(f"✅ 필터링 완료: {filename} ({len(data)} → {len(filtered_data)} 개)")

# 라벨별 CSV를 TIMESTAMP 와 LABEL 만 남겨두는 작업
def csvFitering():
    import os
    import pandas as pd

    csv_dir = r"C:\Users\User\PycharmProjects\Fall Dectection\data\csv"

    for file in os.listdir(csv_dir):
        if not (file.endswith(".csv") and file.startswith("Subject")):
            continue

        input_path = os.path.join(csv_dir, file)
        output_path = os.path.join(csv_dir, f"_{file}")

        # 1. 줄 단위로 읽기
        with open(input_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # 2. 헤더에 , 추가 + 두 번째 줄 삭제
        if len(lines) > 1:
            if not lines[0].strip().endswith(","):
                lines[0] = lines[0].strip() + ",\n"  # 헤더 수정
            del lines[1]  # 2번째 줄 삭제

        # 3. 임시 저장
        temp_path = os.path.join(csv_dir, "_temp.csv")
        with open(temp_path, "w", encoding="utf-8") as f:
            f.writelines(lines)

        # 4. pandas로 읽기
        df = pd.read_csv(temp_path)

        # 5. TimeStamps + 마지막 컬럼만 추출
        if "TimeStamps" not in df.columns or len(df.columns) < 2:
            print(f"⚠️ TimeStamps 없음 or 컬럼 부족: {file}")
            continue

        label_col = df.columns[-1]
        df = df[["TimeStamps", label_col]]
        df.rename(columns={label_col: "Label"}, inplace=True)

        # 6. 저장 (덮어쓰기 or 생성)
        df.to_csv(output_path, index=False, encoding="utf-8-sig")
        print(f"✅ 처리 완료: {output_path}")

    # 7. 임시 파일 제거
    os.remove(temp_path)

# CSV의 TIMESTAMP와 JSON 데이터의 이미지 이름을 비교해 JSON에 LABEL 추가
def addLabel():
    import os
    import json
    import pandas as pd

    # 경로 설정
    csv_dir = r"C:\Users\User\PycharmProjects\Fall Dectection\data\csv"
    json_dir = r"C:\Users\User\PycharmProjects\Fall Dectection\data\json"
    output_dir = r"C:\Users\User\PycharmProjects\FinalTrial"
    os.makedirs(output_dir, exist_ok=True)

    # _파일만 필터링
    csv_files = [f for f in os.listdir(csv_dir) if f.startswith("_") and f.endswith(".csv")]

    for csv_file in csv_files:
        # 파일명에서 SubjectXActivityY 추출
        base_name = csv_file.lstrip("_").replace("Trial2", "").replace(".csv", "")
        json_file = base_name + ".json"

        csv_path = os.path.join(csv_dir, csv_file)
        json_path = os.path.join(json_dir, json_file)
        output_path = os.path.join(output_dir, base_name + ".json")

        # 파일 존재 확인
        if not os.path.exists(json_path):
            print(f"⚠️ JSON 파일 없음: {json_path}")
            continue

        # CSV 로드
        df = pd.read_csv(csv_path)
        df["image_id"] = df["TimeStamps"].str.replace(":", "_") + ".png"

        label_map = dict(zip(df["image_id"], df["Label"]))

        # JSON 로드
        with open(json_path, "r", encoding="utf-8") as f:
            json_data = json.load(f)

        # JSON에 label 추가
        for item in json_data:
            img_id = item.get("image_id")
            if img_id in label_map:
                item["label"] = int(label_map[img_id])

        # 저장
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2)

        print(f"✅ 병합 완료: {output_path}")


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    addLabel()
# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
