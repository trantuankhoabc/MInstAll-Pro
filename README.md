# 🚀 MInstAll Pro v2.0 – Windows Software Auto-Installer

**MInstAll Pro** là công cụ mã nguồn mở mạnh mẽ giúp tự động hóa quá trình cài đặt hàng loạt phần mềm trên hệ điều hành Windows. Với giao diện trực quan và khả năng tùy biến cao, đây là giải pháp hoàn hảo cho kỹ thuật viên máy tính và người dùng muốn tiết kiệm thời gian thiết lập máy mới.

---

## ✨ Tính năng nổi bật

* 📦 **Kho phần mềm sẵn có:** Hỗ trợ cài đặt hơn **60+ phần mềm** phổ biến nhất hiện nay.
* 🛠️ **Công nghệ lõi:** Sử dụng các trình quản lý gói chính thống là **Winget** và **Chocolatey**.
* 🖥️ **Giao diện trực quan:** Được xây dựng bằng Python (Tkinter), dễ dùng cho mọi đối tượng.
* 🔍 **Tự động nhận diện:** Nhận biết phần mềm nào đã được cài đặt hoặc chưa có trên hệ thống.
* 🏃 **Portable:** Hoạt động ngay lập tức mà không cần cài đặt vào hệ thống.
* 🔓 **Full Source Code:** Dễ dàng chỉnh sửa, cá nhân hóa thương hiệu và danh sách phần mềm.

---

## 📂 Cấu trúc mã nguồn

Bộ công cụ bao gồm:

* `MInstAll_Pro.exe`: File thực thi chính để sử dụng ngay.
* `main.py`: Mã nguồn Python (dành cho việc chỉnh sửa).
* `build.bat`: File thực thi để tự động build lại từ mã nguồn sang file `.exe`.
* `icons/`: Thư mục chứa các icon để tùy biến giao diện.
* `dist/`: Thư mục chứa sản phẩm sau khi đóng gói.

---

## 🏗️ Công nghệ sử dụng

| Thành phần | Công nghệ |
| :--- | :--- |
| **Ngôn ngữ lập trình** | Python |
| **Thư viện GUI** | Tkinter |
| **Quản lý gói** | Winget / Chocolatey |
| **Đóng gói EXE** | PyInstaller |

---

## 🛠️ Hướng dẫn Tùy biến & Cá nhân hóa

Nếu bạn muốn tạo một phiên bản của riêng mình, hãy thực hiện theo các bước sau:

### 1. Chuẩn bị
* Cài đặt **Python** trên máy tính.
* Cài đặt thư viện hỗ trợ build: `pip install pyinstaller`.

### 2. Chỉnh sửa nội dung
* **Thay tên Tool:** Mở file `main.py`, nhấn `Ctrl + F` tìm từ khóa `MInstAll Pro` và thay thế bằng tên của bạn.
* **Thay đổi Icon:** Thay thế các file trong thư mục `icons/` bằng icon của bạn (giữ nguyên tên file).
* **Thêm phần mềm:** Bạn có thể copy nội dung file `.py` gửi cho AI và yêu cầu: *"Thêm code cài đặt phần mềm [Tên phần mềm] bằng Winget vào file này giúp tôi"*.

### 3. Đóng gói (Build)
* Chạy file `build.bat`.
* Đợi quá trình hoàn tất, file `.exe` mới của bạn sẽ nằm trong thư mục `dist/`.

---

## ⚠️ Lưu ý quan trọng

* 🛡️ **Quyền Administrator:** Nên chạy tool với quyền quản trị viên cao nhất để đảm bảo quá trình cài đặt không bị lỗi.
* ⚖️ **Bản quyền:** Công cụ này không chứa phần mềm lậu (crack). Toàn bộ phần mềm được tải từ nguồn chính thống của Microsoft (Winget) và cộng đồng Chocolatey.
* 🎓 **Mục đích:** Chia sẻ nhằm mục đích học tập, tham khảo và hỗ trợ cộng đồng kỹ thuật viên.

---

## 🤝 Hỗ trợ & Tham khảo
* Phiên bản Web: [Xem tại đây](https://example.com) *(Thay link của bạn vào đây)*
* Nếu bạn thấy hữu ích, đừng quên tặng một ⭐ cho dự án nhé!

---
Developed with ❤️ by YourName