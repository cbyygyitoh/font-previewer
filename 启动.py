import os
import webbrowser
import http.server
import socketserver
import threading
import time

PORT = 8888

# 获取当前目录
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# 启动服务器
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), handler)

print(f"""
╔══════════════════════════════════════════════════════════════╗
║  🚀 字体工坊服务器已启动                                    ║
║                                                             ║
║  📁 工作目录: {script_dir}                                  ║
║  🌐 访问地址: http://localhost:{PORT}                       ║
║                                                             ║
║  📌 按 Ctrl+C 停止服务器                                   ║
╚══════════════════════════════════════════════════════════════╝
""")

# 自动打开浏览器
webbrowser.open(f"http://localhost:{PORT}")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\n👋 服务器已关闭")
    httpd.shutdown()