# -*- mode: python -*-

block_cipher = None


a = Analysis(['untitled.py'],
             pathex=['F:\\CodeWork\\PycharmProjects\\untitled1\\一键重启'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='非标服务管理器',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
