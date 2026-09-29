[app]
title = pyDoublexer
package.name = pydoublexer
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,json
source.exclude_dirs = __pycache__, bin, .github

version = 0.1

requirements = python3,kivy,pymupdf

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk_api = 21
android.build_tools_version = 33.0.1

android.architectures = arm64-v8a
