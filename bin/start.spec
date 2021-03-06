# -*- mode: python -*-

block_cipher = None

OCTOBOT_PACKAGES_FILES = REQUIRED = [s.strip() for s in open('bin/octobot_packages_files.txt').readlines()]
# hiddenimports=['numpy.core._dtype_ctypes'] from https://github.com/pyinstaller/pyinstaller/issues/3982
a = Analysis(['../start.py'],
             pathex=['../'],
             datas=[
                ('../octobot/config', 'octobot/config'),
                ('../octobot/strategy_optimizer/optimizer_data_files', 'octobot/strategy_optimizer/optimizer_data_files')
             ],
             hiddenimports=[
             "colorlog", "numpy.core._dtype_ctypes",
             "aiosqlite", "aiohttp",
             "telegram", "telegram.ext", "jsonschema",
             "tulipy",
             "praw", "twitter", "simplifiedpytrends", "simplifiedpytrends.exceptions", "simplifiedpytrends.request",
             "pyngrok", "pyngrok.ngrok", "flask", "flask_login", "wtforms", "wtforms.fields.html5", "flask_wtf",
             "gevent", "geventwebsocket", "flask_socketio", "newspaper", "vaderSentiment",
             "vaderSentiment.vaderSentiment",
             "aiofiles",
             "ccxt", "ccxt.async_support", "cryptography", "websockets", "yarl", "idna", "sortedcontainers"
             ] + OCTOBOT_PACKAGES_FILES,
             excludes=["tentacles", "logs", "user"],
             hookspath=[],
             runtime_hooks=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='OctoBot',
          debug=False,
          strip=False,
          icon="favicon.ico",
          upx=True,
          runtime_tmpdir=None,
          console=True )
