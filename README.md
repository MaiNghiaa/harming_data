# Harming Data (ngắn gọn)

- Tạo aHash: resize 8×8, chuyển thang xám, mỗi điểm sáng hơn trung bình → 1, còn lại → 0 (được 64 bit).
- Độ giống: `abs(h1 - h2)` = số bit khác nhau (0…64). Nhỏ hơn hoặc bằng ngưỡng → cùng nhóm.
- Chạy:
```bash
pip install pillow imagehash
python index.py
```

<!-- Cái hiện tại đang dùng -->
hash_map[filename] = imagehash.average_hash(img)
Máy yếu, chỉ cần lọc trùng hệt
dùng trước để test
<!-- Thay thế -->
Perceptual Hash - phash()
hash_map[filename] = imagehash.phash(img)
Máy yếu, ảnh chụp thật, ánh sáng khác nhau
<!-- Thay thế 2 -->
Difference Hash - dHash()
hash_map[filename] = imagehash.dhash(img)
Cần tốc độ trung bình và cân bằng chính xác
