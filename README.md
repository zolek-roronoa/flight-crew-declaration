# Flight Crew Declaration Generator

Công cụ tự động chuyển đổi dữ liệu lịch bay từ file Excel sang biểu mẫu General Declaration (PDF).

## 📋 Tính năng

✅ Đọc dữ liệu từ file Excel (Daily Flight Schedule)  
✅ Tự động điền thông tin chuyến bay vào biểu mẫu  
✅ Xuất ra file PDF có định dạng chuẩn ICAO  
✅ Hỗ trợ đa chuyến bay trong một tài liệu  
✅ Giao diện dòng lệnh đơn giản  

## 📊 Cấu trúc file Excel đầu vào

File Excel phải có các cột sau:
| Cột | Nội dung |
|-----|----------|
| A | DATE (Ngày bay) |
| B | FLT (Số hiệu chuyến bay) |
| C | TYPE (Loại máy bay) |
| D | REG (Mã đăng ký máy bay) |
| E | DEP (Sân bay xuất phát) |
| F | STD (Giờ cất cánh dự kiến) |
| G | STA (Thời gian bay) |
| H | ETA (Giờ hạ cánh dự kiến) |
| K | Crew # (Số thành viên tổ bay) |
| L | Crew (Danh sách phi hành đoàn) |

## 🚀 Cài đặt

### Yêu cầu
- Python 3.7+
- pip

### Bước 1: Clone repository
```bash
git clone https://github.com/zolek-roronoa/flight-crew-declaration.git
cd flight-crew-declaration
```

### Bước 2: Cài đặt dependencies
```bash
pip install -r requirements.txt
```

## 💻 Sử dụng

### Chạy chương trình
```bash
python main.py
```

### Hướng dẫn từng bước

1. **Nhập đường dẫn file Excel:**
   ```
   📁 Enter Excel file path (or press Enter for 'flight_schedule.xlsx'): your_file.xlsx
   ```

2. **Nhập tên file PDF output:**
   ```
   📄 Enter PDF output filename (or press Enter for 'General_Declaration.pdf'): output_file.pdf
   ```

3. Chương trình sẽ:
   - ✅ Đọc dữ liệu từ file Excel
   - ✅ Xử lý thông tin tổ bay
   - ✅ Tạo biểu mẫu General Declaration
   - ✅ Xuất file PDF

### Ví dụ

```bash
$ python main.py
============================================================
FLIGHT CREW DECLARATION GENERATOR
============================================================

📁 Enter Excel file path (or press Enter for 'flight_schedule.xlsx'): flight_data.xlsx
📄 Enter PDF output filename (or press Enter for 'General_Declaration.pdf'): declaration_2026.pdf

⏳ Processing flight data...
✅ Loaded 4 flights from Excel
✅ PDF generated successfully: declaration_2026.pdf

✅ Success! PDF saved as: declaration_2026.pdf
```

## 📄 Output PDF

File PDF được tạo sẽ chứa:
- **Thông tin chuyến bay:** Ngày, số hiệu, máy bay, sân bay
- **Danh sách tổ bay:** Tên, chức vụ, hộ chiếu, ngày sinh
- **Biểu mẫu ICAO Annex 9, Appendix 1:** Định dạng chuẩn quốc tế

## 🛠️ Các thành phần chính

### `FlightCrewDeclaration` class

```python
# Khởi tạo
declaration = FlightCrewDeclaration('flight_schedule.xlsx')

# Tạo PDF
declaration.generate_pdf('output.pdf')
```

#### Các method:
- `load_data()` - Đọc dữ liệu từ Excel
- `generate_pdf(output_file)` - Tạo file PDF
- `parse_crew_list(crew_text)` - Phân tích danh sách tổ bay
- `_airport_code(airport)` - Chuyển đổi mã sân bay

## 📝 Tùy chỉnh

### Thay đổi định dạng PDF

Chỉnh sửa trong `main.py`:
```python
doc = SimpleDocTemplate(output_file, pagesize=A4,
                      topMargin=0.5*inch, bottomMargin=0.5*inch,
                      leftMargin=0.5*inch, rightMargin=0.5*inch)
```

### Thêm logo công ty

```python
img = Image('logo.png', width=1*inch, height=1*inch)
story.append(img)
```

## 🐛 Xử lý sự cố

### Lỗi: "File not found"
- Đảm bảo file Excel tồn tại và đường dẫn chính xác
- Sử dụng đường dẫn tuyệt đối hoặc tương đối

### Lỗi: "Missing columns"
- Kiểm tra file Excel có đủ các cột cần thiết
- Đảm bảo dữ liệu bắt đầu từ dòng 5 (theo template)

### PDF không có dữ liệu
- Kiểm tra định dạng Excel có đúng không
- Xem log output để tìm lỗi chi tiết

## 📞 Hỗ trợ

Nếu bạn gặp vấn đề:
1. Kiểm tra [Issues](https://github.com/zolek-roronoa/flight-crew-declaration/issues)
2. Tạo issue mới với chi tiết lỗi
3. Cung cấp file Excel mẫu (nếu có thể)

## 📄 Giấy phép

MIT License - Xem file LICENSE để chi tiết

## 👨‍💻 Tác giả

Tạo bởi: **zolek-roronoa**  
Ngày tạo: 2026-09-04

---

**Made with ❤️ for aviation crew management**
