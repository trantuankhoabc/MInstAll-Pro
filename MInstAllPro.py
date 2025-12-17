"""
MInstAll Pro - Trình cài đặt phần mềm TỰ ĐỘNG
Version: 1.0.0 - COMPLETE FINAL
"""

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import threading
import webbrowser
import sys
import os
import ctypes
from PIL import Image, ImageTk


class MInstAllPro:
    def __init__(self, root):
        self.root = root
        self.root.title("MInstAll v1.0.0")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f8fafc")

        self.icons = {}
        self._img_cache = {}
        self.set_app_icon()

        self.has_winget = self.check_command("winget")
        self.has_choco = self.check_command("choco")

        self.checkbox_vars = {}
        self.badge_labels = {}

        self.software_db = self.create_database()
        # Remove GAME category (requested)
        self.software_db.pop("🎮 GAME", None)

        self.create_ui()

    def check_command(self, cmd):
        try:
            flags = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
            subprocess.run(
                [cmd, "--version"], capture_output=True, timeout=3, creationflags=flags
            )
            return True
        except:
            return False

    def create_database(self):
        return {
            "⚙️ RUNTIME": [
                {
                    "name": "Visual C++ 2015-2022",
                    "desc": "Runtime quan trọng nhất",
                    "winget": "Microsoft.VCRedist.2015+.x64",
                    "icon": "🔧",
                    "check_path": ["C:\\Windows\\System32\\vcruntime140.dll"],
                },
                {
                    "name": ".NET Runtime 8.0",
                    "desc": "Runtime .NET mới nhất",
                    "winget": "Microsoft.DotNet.DesktopRuntime.8",
                    "icon": "⚙️",
                    "check_path": ["C:\\Program Files\\dotnet\\dotnet.exe"],
                },
                {
                    "name": ".NET Framework 4.8",
                    "desc": "Framework cũ quan trọng",
                    "winget": "Microsoft.DotNet.Framework.DeveloperPack_4",
                    "icon": "🔩",
                },
                {
                    "name": "DirectX Runtime",
                    "desc": "Runtime cho game",
                    "winget": "Microsoft.DirectX",
                    "icon": "🎮",
                },
            ],
            "📦 NÉN FILE": [
                {
                    "name": "7-Zip",
                    "desc": "Nén file miễn phí tốt nhất",
                    "winget": "7zip.7zip",
                    "choco": "7zip",
                    "icon": "📦",
                    "check_path": ["C:\\Program Files\\7-Zip\\7zFM.exe"],
                },
                {
                    "name": "WinRAR",
                    "desc": "WinRAR phổ biến (Trial)",
                    "winget": "RARLab.WinRAR",
                    "choco": "winrar",
                    "icon": "📚",
                    "check_path": ["C:\\Program Files\\WinRAR\\WinRAR.exe"],
                },
                {
                    "name": "PeaZip",
                    "desc": "Nén file đa năng miễn phí",
                    "winget": "Giorgiotani.Peazip",
                    "choco": "peazip",
                    "icon": "🗜️",
                },
                {
                    "name": "Bandizip",
                    "desc": "Nén file nhẹ từ Hàn Quốc",
                    "winget": "Bandisoft.Bandizip",
                    "icon": "📁",
                },
            ],
            "⌨️ BỘ GÕ": [
                {
                    "name": "Unikey",
                    "desc": "Bộ gõ tiếng Việt phổ biến nhất",
                    "winget": "Unikey.Unikey",
                    "choco": "unikey",
                    "icon": "⌨️",
                    "check_path": [
                        "C:\\Program Files\\Unikey\\Unikey.exe",
                        "C:\\Program Files (x86)\\Unikey\\Unikey.exe",
                    ],
                },
                {
                    "name": "EVKey",
                    "desc": "Bộ gõ tiếng Việt hiện đại",
                    "winget": "lamquangminh.EVKey",
                    "icon": "🔤",
                    "check_path": ["C:\\Program Files\\EVKey\\EVKey.exe"],
                },
                {"name": "GoTiengViet", "desc": "Bộ gõ mã nguồn mở", "icon": "📝"},
                {"name": "VietIME", "desc": "Bộ gõ Telex/VNI", "icon": "🔠"},
            ],
            "📄 OFFICE": [
                {
                    "name": "LibreOffice",
                    "desc": "Thay thế Microsoft Office miễn phí",
                    "winget": "TheDocumentFoundation.LibreOffice",
                    "choco": "libreoffice-fresh",
                    "icon": "📊",
                    "check_path": [
                        "C:\\Program Files\\LibreOffice\\program\\soffice.exe"
                    ],
                },
                {
                    "name": "OnlyOffice",
                    "desc": "Office tương thích MS Office",
                    "winget": "ONLYOFFICE.DesktopEditors",
                    "choco": "onlyoffice",
                    "icon": "📈",
                },
                {
                    "name": "WPS Office",
                    "desc": "Office miễn phí giao diện đẹp",
                    "winget": "Kingsoft.WPSOffice",
                    "icon": "📋",
                },
                {
                    "name": "FreeOffice",
                    "desc": "Office nhẹ miễn phí",
                    "winget": "SoftMaker.FreeOffice.2024",
                    "icon": "📑",
                },
                {
                    "name": "OpenOffice",
                    "desc": "Office mã nguồn mở",
                    "winget": "Apache.OpenOffice",
                    "choco": "openoffice",
                    "icon": "📃",
                },
            ],
            "📕 PDF": [
                {
                    "name": "Adobe Reader",
                    "desc": "Đọc PDF chính hãng từ Adobe",
                    "winget": "Adobe.Acrobat.Reader.64-bit",
                    "choco": "adobereader",
                    "icon": "🔴",
                },
                {
                    "name": "Foxit Reader",
                    "desc": "PDF mạnh mẽ có chỉnh sửa",
                    "winget": "Foxit.FoxitReader",
                    "choco": "foxitreader",
                    "icon": "🟠",
                },
                {
                    "name": "Sumatra PDF",
                    "desc": "PDF siêu nhẹ siêu nhanh",
                    "winget": "SumatraPDF.SumatraPDF",
                    "choco": "sumatrapdf",
                    "icon": "🟡",
                },
                {
                    "name": "PDF-XChange",
                    "desc": "Chỉnh sửa PDF chuyên nghiệp",
                    "winget": "TrackerSoftware.PDF-XChangeEditor",
                    "icon": "🟢",
                },
                {
                    "name": "PDF24",
                    "desc": "Tạo và ghép PDF miễn phí",
                    "winget": "geeksoftwareGmbH.PDF24Creator",
                    "choco": "pdf24",
                    "icon": "🔵",
                },
            ],
            "🖥️ REMOTE": [
                {
                    "name": "TeamViewer",
                    "desc": "Remote Desktop số 1 thế giới",
                    "winget": "TeamViewer.TeamViewer",
                    "choco": "teamviewer",
                    "icon": "🔵",
                    "check_path": ["C:\\Program Files\\TeamViewer\\TeamViewer.exe"],
                },
                {
                    "name": "AnyDesk",
                    "desc": "Remote nhanh ổn định",
                    "winget": "AnyDeskSoftwareGmbH.AnyDesk",
                    "choco": "anydesk",
                    "icon": "🔴",
                    "check_path": ["C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe"],
                },
                {
                    "name": "UltraViewer",
                    "desc": "Remote Việt Nam miễn phí",
                    "icon": "🟢",
                },
                {
                    "name": "RustDesk",
                    "desc": "Remote mã nguồn mở",
                    "winget": "RustDesk.RustDesk",
                    "choco": "rustdesk",
                    "icon": "🟣",
                },
                {
                    "name": "Chrome Remote",
                    "desc": "Remote qua Chrome",
                    "winget": "Google.ChromeRemoteDesktop",
                    "icon": "🟡",
                },
            ],
            "🌐 BROWSER": [
                {
                    "name": "Chrome",
                    "desc": "Google Chrome phổ biến nhất",
                    "winget": "Google.Chrome",
                    "choco": "googlechrome",
                    "icon": "🔴",
                    "check_path": [
                        "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                    ],
                },
                {
                    "name": "Firefox",
                    "desc": "Mozilla Firefox mã nguồn mở",
                    "winget": "Mozilla.Firefox",
                    "choco": "firefox",
                    "icon": "🟠",
                    "check_path": ["C:\\Program Files\\Mozilla Firefox\\firefox.exe"],
                },
                {
                    "name": "Brave",
                    "desc": "Browser bảo mật riêng tư",
                    "winget": "Brave.Brave",
                    "choco": "brave",
                    "icon": "🟡",
                },
                {
                    "name": "Edge",
                    "desc": "Microsoft Edge",
                    "winget": "Microsoft.Edge",
                    "icon": "🔵",
                    "check_path": [
                        "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                    ],
                },
                {
                    "name": "Opera",
                    "desc": "Browser có VPN miễn phí",
                    "winget": "Opera.Opera",
                    "choco": "opera",
                    "icon": "🔴",
                },
                {
                    "name": "Vivaldi",
                    "desc": "Browser tùy biến cao",
                    "winget": "VivaldiTechnologies.Vivaldi",
                    "choco": "vivaldi",
                    "icon": "🟣",
                },
                {
                    "name": "Cốc Cốc",
                    "desc": "Trình duyệt Việt Nam",
                    "winget": "CocCoc.CocCoc",
                    "icon": "🟢",
                },
            ],
            "🎬 MEDIA": [
                {
                    "name": "VLC",
                    "desc": "Phát mọi định dạng video/audio",
                    "winget": "VideoLAN.VLC",
                    "choco": "vlc",
                    "icon": "🟠",
                    "check_path": ["C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"],
                },
                {
                    "name": "K-Lite Codec",
                    "desc": "Bộ codec đầy đủ nhất",
                    "winget": "CodecGuide.K-LiteCodecPack.Full",
                    "choco": "k-litecodecpackfull",
                    "icon": "🔵",
                },
                {
                    "name": "PotPlayer",
                    "desc": "Player mạnh từ Hàn Quốc",
                    "winget": "Daum.PotPlayer",
                    "choco": "potplayer",
                    "icon": "🔴",
                },
                {
                    "name": "MPC-HC",
                    "desc": "Media Player Classic nhẹ",
                    "winget": "clsid2.mpc-hc",
                    "choco": "mpc-hc",
                    "icon": "🟢",
                },
                {
                    "name": "AIMP",
                    "desc": "Nghe nhạc chất lượng cao",
                    "winget": "AIMP.AIMP",
                    "choco": "aimp",
                    "icon": "🔵",
                },
                {
                    "name": "Spotify",
                    "desc": "Nghe nhạc streaming",
                    "winget": "Spotify.Spotify",
                    "choco": "spotify",
                    "icon": "🟢",
                },
            ],
            "🛠️ TIỆN ÍCH": [
                {
                    "name": "PowerToys",
                    "desc": "Bộ công cụ Windows từ Microsoft",
                    "winget": "Microsoft.PowerToys",
                    "choco": "powertoys",
                    "icon": "⚡",
                    "check_path": ["C:\\Program Files\\PowerToys\\PowerToys.exe"],
                },
                {
                    "name": "Everything",
                    "desc": "Tìm kiếm file siêu tốc",
                    "winget": "voidtools.Everything",
                    "choco": "everything",
                    "icon": "🔍",
                },
                {
                    "name": "CCleaner",
                    "desc": "Dọn dẹp và tối ưu Windows",
                    "winget": "Piriform.CCleaner",
                    "choco": "ccleaner",
                    "icon": "🧹",
                },
                {
                    "name": "Revo Uninstaller",
                    "desc": "Gỡ phần mềm tận gốc",
                    "winget": "RevoUninstaller.RevoUninstaller",
                    "choco": "revo-uninstaller",
                    "icon": "🗑️",
                },
                {
                    "name": "Glary Utilities",
                    "desc": "Tối ưu hệ thống đa năng",
                    "winget": "Glarysoft.GlaryUtilities",
                    "choco": "glaryutilities",
                    "icon": "🔧",
                },
                {
                    "name": "Wise Care 365",
                    "desc": "Bảo trì Windows toàn diện",
                    "winget": "WiseCleaner.WiseCare365",
                    "icon": "💊",
                },
                {
                    "name": "TreeSize",
                    "desc": "Phân tích dung lượng ổ đĩa",
                    "winget": "JAMSoftware.TreeSize.Free",
                    "icon": "📊",
                },
            ],
            "💻 CODE": [
                {
                    "name": "VS Code",
                    "desc": "Code editor tốt nhất thế giới",
                    "winget": "Microsoft.VisualStudioCode",
                    "choco": "vscode",
                    "icon": "💻",
                    "check_path": ["C:\\Program Files\\Microsoft VS Code\\Code.exe"],
                },
                {
                    "name": "Notepad++",
                    "desc": "Text editor mạnh mẽ",
                    "winget": "Notepad++.Notepad++",
                    "choco": "notepadplusplus",
                    "icon": "📝",
                },
                {
                    "name": "Sublime",
                    "desc": "Text editor nhanh và đẹp",
                    "winget": "SublimeHQ.SublimeText.4",
                    "choco": "sublimetext4",
                    "icon": "📄",
                },
                {
                    "name": "Git",
                    "desc": "Version control phổ biến nhất",
                    "winget": "Git.Git",
                    "choco": "git",
                    "icon": "🔀",
                },
                {
                    "name": "GitHub Desktop",
                    "desc": "Git GUI dễ sử dụng",
                    "winget": "GitHub.GitHubDesktop",
                    "choco": "github-desktop",
                    "icon": "🐙",
                },
                {
                    "name": "Python 3",
                    "desc": "Ngôn ngữ lập trình Python",
                    "winget": "Python.Python.3.12",
                    "choco": "python",
                    "icon": "🐍",
                },
                {
                    "name": "Node.js",
                    "desc": "JavaScript runtime",
                    "winget": "OpenJS.NodeJS",
                    "choco": "nodejs",
                    "icon": "🟢",
                },
            ],
            "🎨 ĐỒ HỌA": [
                {
                    "name": "GIMP",
                    "desc": "Thay thế Photoshop miễn phí",
                    "winget": "GIMP.GIMP",
                    "choco": "gimp",
                    "icon": "🎨",
                },
                {
                    "name": "Inkscape",
                    "desc": "Thay thế Illustrator miễn phí",
                    "winget": "Inkscape.Inkscape",
                    "choco": "inkscape",
                    "icon": "✏️",
                },
                {
                    "name": "Krita",
                    "desc": "Vẽ digital art chuyên nghiệp",
                    "winget": "KDE.Krita",
                    "choco": "krita",
                    "icon": "🖼️",
                },
                {
                    "name": "Blender",
                    "desc": "3D modeling miễn phí",
                    "winget": "BlenderFoundation.Blender",
                    "choco": "blender",
                    "icon": "🎭",
                },
                {
                    "name": "Paint.NET",
                    "desc": "Chỉnh sửa ảnh đơn giản",
                    "winget": "dotPDN.PaintDotNet",
                    "choco": "paint.net",
                    "icon": "🖌️",
                },
            ],
            "🖼️ XEM ẢNH": [
                {
                    "name": "IrfanView",
                    "desc": "Xem ảnh nhanh và nhẹ",
                    "winget": "IrfanSkiljan.IrfanView",
                    "choco": "irfanview",
                    "icon": "🖼️",
                },
                {
                    "name": "XnView",
                    "desc": "Quản lý ảnh chuyên nghiệp",
                    "winget": "XnSoft.XnView",
                    "choco": "xnview",
                    "icon": "📷",
                },
                {
                    "name": "FastStone",
                    "desc": "Xem ảnh đầy đủ tính năng",
                    "winget": "FastStone.ImageViewer",
                    "choco": "fsviewer",
                    "icon": "🖼️",
                },
                {
                    "name": "ImageGlass",
                    "desc": "Xem ảnh hiện đại",
                    "winget": "DuongDieuPhap.ImageGlass",
                    "choco": "imageglass",
                    "icon": "🖼️",
                },
            ],
            "🎬 VIDEO": [
                {
                    "name": "OBS Studio",
                    "desc": "Quay màn hình và stream",
                    "winget": "OBSProject.OBSStudio",
                    "choco": "obs-studio",
                    "icon": "🎥",
                },
                {
                    "name": "ShareX",
                    "desc": "Screenshot đa năng",
                    "winget": "ShareX.ShareX",
                    "choco": "sharex",
                    "icon": "📸",
                },
                {
                    "name": "Shotcut",
                    "desc": "Chỉnh sửa video miễn phí",
                    "winget": "Meltytech.Shotcut",
                    "choco": "shotcut",
                    "icon": "🎞️",
                },
                {
                    "name": "HandBrake",
                    "desc": "Chuyển đổi định dạng video",
                    "winget": "HandBrake.HandBrake",
                    "choco": "handbrake",
                    "icon": "🔄",
                },
                {
                    "name": "Audacity",
                    "desc": "Chỉnh sửa audio miễn phí",
                    "winget": "Audacity.Audacity",
                    "choco": "audacity",
                    "icon": "🎵",
                },
            ],
            "📥 DOWNLOAD": [
                {
                    "name": "qBittorrent",
                    "desc": "Tải torrent tốt nhất",
                    "winget": "qBittorrent.qBittorrent",
                    "choco": "qbittorrent",
                    "icon": "🌐",
                },
                {
                    "name": "FDM",
                    "desc": "Free Download Manager mạnh mẽ",
                    "winget": "SoftDeluxe.FreeDownloadManager",
                    "choco": "free-download-manager",
                    "icon": "📥",
                },
                {
                    "name": "JDownloader",
                    "desc": "Tải từ nhiều host",
                    "winget": "AppWork.JDownloader",
                    "icon": "📦",
                },
            ],
            "💬 CHAT": [
                {
                    "name": "Telegram",
                    "desc": "Nhắn tin bảo mật tốt nhất",
                    "winget": "Telegram.TelegramDesktop",
                    "choco": "telegram",
                    "icon": "🔵",
                },
                {
                    "name": "Zoom",
                    "desc": "Họp online phổ biến nhất",
                    "winget": "Zoom.Zoom",
                    "choco": "zoom",
                    "icon": "🔵",
                },
                {
                    "name": "Zalo PC",
                    "desc": "Mạng xã hội Việt Nam",
                    "winget": "Zalo.Zalo",
                    "icon": "🔵",
                },
            ],
            "🔒 BẢO MẬT": [
                {
                    "name": "Bitwarden",
                    "desc": "Quản lý mật khẩu mã nguồn mở",
                    "winget": "Bitwarden.Bitwarden",
                    "choco": "bitwarden",
                    "icon": "🔵",
                },
                {
                    "name": "KeePassXC",
                    "desc": "Quản lý mật khẩu offline",
                    "winget": "KeePassXCTeam.KeePassXC",
                    "choco": "keepassxc",
                    "icon": "🟢",
                },
                {
                    "name": "ProtonVPN",
                    "desc": "VPN miễn phí bảo mật",
                    "winget": "ProtonTechnologies.ProtonVPN",
                    "icon": "🟣",
                },
            ],
            "🎮 GAME": [
                {
                    "name": "Steam",
                    "desc": "Nền tảng game PC lớn nhất",
                    "winget": "Valve.Steam",
                    "choco": "steam",
                    "icon": "⚫",
                },
                {
                    "name": "Epic Games",
                    "desc": "Game miễn phí mỗi tuần",
                    "winget": "EpicGames.EpicGamesLauncher",
                    "icon": "⚫",
                },
                {
                    "name": "GOG Galaxy",
                    "desc": "Game DRM-free",
                    "winget": "GOG.Galaxy",
                    "icon": "🟣",
                },
            ],
            "🔧 CÔNG CỤ": [
                {
                    "name": "Rufus",
                    "desc": "Tạo USB boot Windows",
                    "winget": "Rufus.Rufus",
                    "choco": "rufus",
                    "icon": "💿",
                },
                {
                    "name": "CPU-Z",
                    "desc": "Xem thông tin CPU chi tiết",
                    "winget": "CPUID.CPU-Z",
                    "choco": "cpu-z",
                    "icon": "🖥️",
                },
                {
                    "name": "GPU-Z",
                    "desc": "Xem thông tin GPU chi tiết",
                    "winget": "TechPowerUp.GPU-Z",
                    "choco": "gpu-z",
                    "icon": "🎮",
                },
                {
                    "name": "CrystalDiskInfo",
                    "desc": "Kiểm tra sức khỏe ổ cứng",
                    "winget": "CrystalDewWorld.CrystalDiskInfo",
                    "choco": "crystaldiskinfo",
                    "icon": "💾",
                },
            ],
            "☁️ CLOUD": [
                {
                    "name": "Google Drive",
                    "desc": "Google Drive Desktop",
                    "winget": "Google.GoogleDrive",
                    "icon": "☁️",
                },
                {
                    "name": "Dropbox",
                    "desc": "Cloud storage phổ biến",
                    "winget": "Dropbox.Dropbox",
                    "choco": "dropbox",
                    "icon": "📦",
                },
                {
                    "name": "Mega Sync",
                    "desc": "MEGA cloud 20GB miễn phí",
                    "winget": "Mega.MEGASync",
                    "icon": "☁️",
                },
            ],
        }

    # ---------- Resource & App Icon ----------
    def resource_path(self, rel_path: str) -> str:
        base = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
        return os.path.join(base, rel_path)

    def set_app_icon(self):
        """Set window/taskbar icon on Windows and keep references."""
        try:
            if sys.platform == "win32":
                # AppUserModelID helps Windows taskbar/Alt+Tab show the correct icon
                try:
                    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                        "MInstAllPro.App"
                    )
                except Exception:
                    pass

            ico = self.resource_path("app.ico")
            if os.path.exists(ico):
                try:
                    self.root.iconbitmap(ico)
                except Exception:
                    pass

            # iconphoto fallback (and helps some contexts)
            png = self.resource_path("app.png")
            if os.path.exists(png):
                try:
                    im = Image.open(png).convert("RGBA").resize((64, 64), Image.LANCZOS)
                    photo = ImageTk.PhotoImage(im)
                    self.root.iconphoto(True, photo)
                    self._img_cache["_app_icon"] = photo
                except Exception:
                    pass
        except Exception:
            pass

    # ---------- Software Icons ----------
    def _find_icon_file(self, sw_name: str) -> str:
        """Find an icon file in ./icons matching software name (any common ext)."""
        base_dir = self.resource_path("icons")
        candidates = [
            os.path.join(base_dir, f"{sw_name}.png"),
            os.path.join(base_dir, f"{sw_name}.jpg"),
            os.path.join(base_dir, f"{sw_name}.jpeg"),
            os.path.join(base_dir, f"{sw_name}.webp"),
            os.path.join(base_dir, f"{sw_name}.bmp"),
        ]
        for p in candidates:
            if os.path.exists(p):
                return p
        return os.path.join(base_dir, "default.png")

    def get_sw_icon(self, sw: dict, size=(24, 24)):
        path = self._find_icon_file(sw.get("name", ""))
        key = (path, size)
        if key in self._img_cache:
            return self._img_cache[key]
        try:
            im = Image.open(path).convert("RGBA")
            im = im.resize(size, Image.LANCZOS)
            photo = ImageTk.PhotoImage(im)
            self._img_cache[key] = photo
            return photo
        except Exception:
            # last resort: blank
            im = Image.new("RGBA", size, (0, 0, 0, 0))
            photo = ImageTk.PhotoImage(im)
            self._img_cache[key] = photo
            return photo

    # ---------- Rounded Buttons ----------
    def make_rounded_button(
        self,
        parent,
        text,
        command,
        bg,
        fg="white",
        width=130,
        height=36,
        radius=14,
        font=("Segoe UI", 9, "bold"),
    ):
        c = tk.Canvas(
            parent,
            width=width,
            height=height,
            bg=parent["bg"],
            highlightthickness=0,
            bd=0,
        )

        def round_rect(x1, y1, x2, y2, r, **kwargs):
            points = [
                x1 + r,
                y1,
                x2 - r,
                y1,
                x2,
                y1,
                x2,
                y1 + r,
                x2,
                y2 - r,
                x2,
                y2,
                x2 - r,
                y2,
                x1 + r,
                y2,
                x1,
                y2,
                x1,
                y2 - r,
                x1,
                y1 + r,
                x1,
                y1,
            ]
            return c.create_polygon(points, smooth=True, **kwargs)

        shape = round_rect(2, 2, width - 2, height - 2, radius, fill=bg, outline=bg)
        label = c.create_text(width // 2, height // 2, text=text, fill=fg, font=font)

        def on_click(_=None):
            command()

        def on_enter(_):
            c.itemconfig(shape, outline=bg)

        def on_leave(_):
            c.itemconfig(shape, outline=bg)

        c.bind("<Button-1>", on_click)
        c.bind("<Enter>", on_enter)
        c.bind("<Leave>", on_leave)
        c.configure(cursor="hand2")
        return c

    def create_ui(self):
        header = tk.Frame(self.root, bg="#2563eb", height=100)
        header.pack(fill=tk.X)
        header.pack_propagate(False)

        # App logo (left)
        try:
            logo_path = self.resource_path("app.png")
            if os.path.exists(logo_path):
                im = (
                    Image.open(logo_path)
                    .convert("RGBA")
                    .resize((42, 42), Image.LANCZOS)
                )
                logo = ImageTk.PhotoImage(im)
                self._img_cache["_header_logo"] = logo
                tk.Label(header, image=logo, bg="#2563eb").place(x=18, y=28)
        except Exception:
            pass

        tk.Label(
            header,
            text="MInstAll Pro",
            font=("Segoe UI", 24, "bold"),
            bg="#2563eb",
            fg="white",
        ).pack(pady=(15, 3))
        tk.Label(
            header,
            text="🚀 60+ Phần mềm • Tự động • Miễn phí",
            font=("Segoe UI", 10),
            bg="#2563eb",
            fg="#dbeafe",
        ).pack()

        status = tk.Frame(
            self.root,
            height=40,
            bg="#10b981" if (self.has_winget or self.has_choco) else "#f59e0b",
        )
        status.pack(fill=tk.X)
        status.pack_propagate(False)

        if self.has_winget or self.has_choco:
            txt = (
                "✅ Sẵn sàng | "
                + ("Winget ✓ " if self.has_winget else "")
                + ("Choco ✓" if self.has_choco else "")
            )
        else:
            txt = "⚠️ Cần cài Winget/Chocolatey"

        tk.Label(
            status, text=txt, font=("Segoe UI", 9, "bold"), bg=status["bg"], fg="white"
        ).pack(pady=8)

        self.progress_frame = tk.Frame(self.root, bg="#1e293b", height=50)
        progress_container = tk.Frame(self.progress_frame, bg="#1e293b")
        progress_container.pack(expand=True, fill=tk.BOTH, padx=20)

        self.progress_label = tk.Label(
            progress_container, text="", font=("Segoe UI", 9), bg="#1e293b", fg="white"
        )
        self.progress_label.pack(pady=(8, 4))

        self.progress_bar = ttk.Progressbar(
            progress_container, mode="determinate", length=600
        )
        self.progress_bar.pack(pady=(0, 8))

        content = tk.Frame(self.root, bg="#f1f5f9")
        content.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(content, bg="#f1f5f9", highlightthickness=0)
        scrollbar = ttk.Scrollbar(content, orient="vertical", command=canvas.yview)
        scrollable = tk.Frame(canvas, bg="#f1f5f9")

        scrollable.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas_frame = canvas.create_window((0, 0), window=scrollable, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind(
            "<Configure>", lambda e: canvas.itemconfig(canvas_frame, width=e.width)
        )

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        row, col = 0, 0
        for category, softwares in self.software_db.items():
            self.create_category(scrollable, category, softwares).grid(
                row=row, column=col, padx=8, pady=8, sticky="nsew"
            )
            col += 1
            if col >= 2:
                col = 0
                row += 1

        for i in range(2):
            scrollable.grid_columnconfigure(i, weight=1)

        control = tk.Frame(self.root, bg="white", height=70)
        control.pack(fill=tk.X, side=tk.BOTTOM)
        control.pack_propagate(False)

        btns = tk.Frame(control, bg="white")
        btns.pack(expand=True)

        # Rounded, compact buttons
        self.btn_select_all = self.make_rounded_button(
            btns, "Chọn tất cả", self.select_all, bg="#3b82f6", width=120, height=34
        )
        self.btn_select_all.pack(side=tk.LEFT, padx=6)

        self.btn_deselect = self.make_rounded_button(
            btns, "Bỏ chọn", self.deselect_all, bg="#64748b", width=110, height=34
        )
        self.btn_deselect.pack(side=tk.LEFT, padx=6)

        self.count_label = tk.Label(
            btns,
            text="0 phần mềm",
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg="#1e293b",
        )
        self.count_label.pack(side=tk.LEFT, padx=14)

        self.btn_install = self.make_rounded_button(
            btns,
            "Cài đặt",
            self.start_install,
            bg="#dc2626",
            width=110,
            height=38,
            font=("Segoe UI", 10, "bold"),
        )
        self.btn_install.pack(side=tk.LEFT, padx=6)

    def create_category(self, parent, category, softwares):
        card = tk.Frame(
            parent, bg="white", highlightbackground="#cbd5e1", highlightthickness=1
        )

        header = tk.Frame(card, bg="#3b82f6", height=42)
        header.pack(fill=tk.X)
        header.pack_propagate(False)

        tk.Label(
            header,
            text=category,
            font=("Segoe UI", 11, "bold"),
            bg="#3b82f6",
            fg="white",
            anchor="w",
        ).pack(side=tk.LEFT, padx=10, pady=8)
        tk.Label(
            header,
            text=f"{len(softwares)}",
            font=("Segoe UI", 8, "bold"),
            bg="white",
            fg="#3b82f6",
            padx=5,
            pady=1,
        ).pack(side=tk.RIGHT, padx=10)

        list_frame = tk.Frame(card, bg="white")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)

        for sw in softwares:
            self.create_item(list_frame, sw, category)

        return card

    def create_item(self, parent, sw, category):
        item = tk.Frame(
            parent,
            bg="#f8fafc",
            highlightbackground="#e2e8f0",
            highlightthickness=1,
            height=52,
        )
        item.pack(fill=tk.X, pady=1, padx=1)
        item.pack_propagate(False)

        var = tk.BooleanVar()
        tk.Checkbutton(
            item, variable=var, bg="#f8fafc", command=self.update_count
        ).pack(side=tk.LEFT, padx=5)

        self.checkbox_vars[f"{category}:{sw['name']}"] = (var, sw)

        icon_img = self.get_sw_icon(sw, size=(26, 26))
        tk.Label(item, image=icon_img, bg="#f8fafc").pack(side=tk.LEFT, padx=6)

        info = tk.Frame(item, bg="#f8fafc")
        info.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=6)

        tk.Label(
            info,
            text=sw["name"],
            font=("Segoe UI", 9, "bold"),
            bg="#f8fafc",
            fg="#1e293b",
            anchor="w",
        ).pack(fill=tk.X)
        tk.Label(
            info,
            text=sw["desc"],
            font=("Segoe UI", 8),
            bg="#f8fafc",
            fg="#64748b",
            anchor="w",
        ).pack(fill=tk.X)

        key = f"{category}:{sw['name']}"
        badge = tk.Label(
            item,
            text="CHƯA CHỌN",
            font=("Segoe UI", 8, "bold"),
            bg="#64748b",
            fg="white",
            padx=9,
            pady=3,
        )
        badge.pack(side=tk.RIGHT, padx=6)
        self.badge_labels[key] = badge

    def update_count(self):
        count = 0
        for key, (var, sw) in self.checkbox_vars.items():
            badge = self.badge_labels.get(key)
            if var.get():
                count += 1
                if badge:
                    badge.config(text="ĐÃ CHỌN", bg="#10b981")
            else:
                if badge:
                    badge.config(text="CHƯA CHỌN", bg="#64748b")
        self.count_label.config(text=f"{count} phần mềm")

    def select_all(self):
        for var, _ in self.checkbox_vars.values():
            var.set(True)
        self.update_count()

    def deselect_all(self):
        for var, _ in self.checkbox_vars.values():
            var.set(False)
        self.update_count()

    def start_install(self):
        selected = [(sw, var) for var, sw in self.checkbox_vars.values() if var.get()]

        if not selected:
            messagebox.showwarning("Cảnh báo", "Chọn ít nhất 1 phần mềm!")
            return

        if not self.has_winget and not self.has_choco:
            if messagebox.askyesno(
                "Cần Package Manager", "Chưa có Winget/Chocolatey!\n\nMở hướng dẫn?"
            ):
                webbrowser.open("https://chocolatey.org/install")
            return

        self.progress_frame.pack(after=self.root.winfo_children()[1], fill=tk.X)
        self.progress_bar["maximum"] = len(selected)
        self.progress_bar["value"] = 0

        threading.Thread(
            target=self.install_process, args=(selected,), daemon=True
        ).start()

    def install_process(self, selected):
        total = len(selected)
        success = 0

        for idx, (sw, var) in enumerate(selected, 1):
            self.progress_label.config(
                text=f"📦 Đang cài: {sw['name']} ({idx}/{total})"
            )
            self.progress_bar["value"] = idx
            self.root.update()

            if self.install_sw(sw):
                success += 1

        self.progress_label.config(text=f"✅ Hoàn tất! Thành công: {success}/{total}")
        self.root.after(3000, lambda: self.progress_frame.pack_forget())

        messagebox.showinfo("Hoàn tất!", f"✅ Đã cài: {success}/{total}")

    def install_sw(self, sw):
        try:
            flags = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0

            if self.has_winget and sw.get("winget"):
                result = subprocess.run(
                    [
                        "winget",
                        "install",
                        "--id",
                        sw["winget"],
                        "--silent",
                        "--accept-source-agreements",
                        "--accept-package-agreements",
                    ],
                    capture_output=True,
                    timeout=600,
                    creationflags=flags,
                )
                return result.returncode == 0

            elif self.has_choco and sw.get("choco"):
                result = subprocess.run(
                    ["choco", "install", sw["choco"], "-y"],
                    capture_output=True,
                    timeout=600,
                    creationflags=flags,
                )
                return result.returncode == 0

            return False
        except:
            return False


def main():
    root = tk.Tk()
    app = MInstAllPro(root)
    root.mainloop()


if __name__ == "__main__":
    main()
