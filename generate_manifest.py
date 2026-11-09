import os
import json
import re

def extract_title(filepath):
    """마크다운 파일에서 최상단 1단계 제목(#)을 추출합니다."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# '):
                    return line[2:].strip()
                # YAML 프론트매터의 title 추출 (옵션)
                m = re.match(r'^title:\s*"?([^"]+)"?', line)
                if m:
                    return m.group(1).strip()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        
    # 파일 내에 제목이 없으면 확장자를 제외한 파일명을 사용합니다.
    return os.path.splitext(os.path.basename(filepath))[0]

def generate_manifest():
    manifest = []
    
    for root, dirs, files in os.walk('.'):
        # 1. 숨김 폴더(.), 언더바(_)로 시작하는 폴더, 특정 제외 폴더 필터링
        dirs[:] = [d for d in dirs if not d.startswith('.') and not d.startswith('_') and d not in ['assets', 'images']]

        # 파일을 이름순으로 정렬하여 목차 순서를 일정하게 유지
        for file in sorted(files):
            if file.endswith('.md') or file.endswith('.html'):
                # 루트 디렉토리의 README.md나 뷰어 index.html은 목차에서 제외
                if file in ['README.md', 'index.html']:
                    continue

                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, '.')
                # 윈도우 환경 등에서 역슬래시(\)가 들어갈 경우 웹 표준인 슬래시(/)로 변환
                rel_path = rel_path.replace('\\', '/')

                title = extract_title(filepath)
                # 상대 경로를 기반으로 고유 id 생성 (영문, 숫자, 하이픈만 허용)
                doc_id = re.sub(r'[^a-zA-Z0-9-]', '-', os.path.splitext(rel_path)[0]).strip('-')

                manifest.append({
                    "id": doc_id,
                    "title": title,
                    "file": rel_path
                })

    # manifest.json 파일 쓰기 (한글 깨짐 방지를 위해 ensure_ascii=False)
    with open('manifest.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"✅ Successfully generated manifest.json with {len(manifest)} items.")

if __name__ == "__main__":
    generate_manifest()
