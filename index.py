import os
from PIL import Image
import imagehash
import shutil

input_folder = "images"
output_folder = "output"
similarity_threshold = 5 

os.makedirs(output_folder, exist_ok=True)

# Đọc ảnh và tạo hash
hash_map = {} 
for filename in os.listdir(input_folder):
    path = os.path.join(input_folder, filename)
    try:
        img = Image.open(path)
        hash_map[filename] = imagehash.average_hash(img)
    except Exception as e:
        print(f"Bỏ qua {filename}: {e}")

# Phân nhóm
groups = []
visited = set()

for fname, h in hash_map.items():
    if fname in visited:
        continue
    group = [fname]
    visited.add(fname)

    for other, h2 in hash_map.items():
        if other in visited:
            continue
        if abs(h - h2) <= similarity_threshold:
            group.append(other)
            visited.add(other)

    groups.append(group)

# Lưu ảnh và chia fodler
for i, group in enumerate(groups, 1):
    group_path = os.path.join(output_folder, f"group_{i}")
    os.makedirs(group_path, exist_ok=True)
    for img_name in group:
        shutil.copy(os.path.join(input_folder, img_name), os.path.join(group_path, img_name))

print(f"{len(groups)}")
