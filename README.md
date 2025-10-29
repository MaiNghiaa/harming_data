# Harming Data (ngắn gọn)

- Tạo aHash: resize 8×8, chuyển thang xám, mỗi điểm sáng hơn trung bình → 1, còn lại → 0 (được 64 bit).
- Độ giống: `abs(h1 - h2)` = số bit khác nhau (0…64). Nhỏ hơn hoặc bằng ngưỡng → cùng nhóm.
- Chạy:
```bash
pip install pillow imagehash
python index.py
```