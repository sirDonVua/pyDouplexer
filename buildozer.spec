[app]

title = pyDoublexer
package.name = pydoublexer
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,json
source.exclude_dirs = __pycache__,bin,.github,.git

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk_api = 21

android.archs = arm64-v8a
