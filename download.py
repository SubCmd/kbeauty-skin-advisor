import shutil
from pathlib import Path

import kagglehub

# 데이터 다운로드
download_path = kagglehub.dataset_download(
    "nadyinky/sephora-products-and-skincare-reviews"
)

# 프로젝트 raw 경로
raw_path = Path("/Users/sublee/kbeauty-skin-advisor/data/raw")

raw_path.mkdir(parents=True, exist_ok=True)

# 다운로드한 파일 복사
for file in Path(download_path).iterdir():
    if file.is_file():
        shutil.copy2(file, raw_path / file.name)

print("데이터 저장 완료:", raw_path)
