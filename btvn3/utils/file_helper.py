"""
utils/file_helper.py
Chứa các hàm tiện ích thao tác với file system.
"""
import os


def create_log_dir(dir_name: str) -> str:
    """
    Tạo thư mục log nếu chưa tồn tại.
    Dùng os.path.exists() kiểm tra trước để tránh FileExistsError.

    Args:
        dir_name: Tên (hoặc đường dẫn) thư mục cần tạo.

    Returns:
        Đường dẫn tuyệt đối của thư mục vừa tạo (hoặc đã tồn tại).
    """
    abs_path = os.path.abspath(dir_name)

    if not os.path.exists(abs_path):
        os.makedirs(abs_path)
        print(f"[INFO] Đã tạo thư mục log: '{abs_path}'")
    else:
        print(f"[INFO] Thư mục log đã tồn tại: '{abs_path}'")

    return abs_path