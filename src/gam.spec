# -*- mode: python -*-

import sys

from PyInstaller.utils.hooks import copy_metadata

sys.modules['FixTk'] = None

extra_files = [
    ('cacerts.pem', '.'),
    ('cbcm-v1.1beta1.json', '.'),
    ('contacts-v3.json', '.'),
    ('contactdelegation-v1.json', '.'),
    ('sites-v1.json', '.')
    ]
extra_files += copy_metadata('gam/googleapiclient')

a = Analysis(['gam/__main__.py'],
             pathex=['./gam'],
             hiddenimports=['pkg_resources.py2_warn'],
             hookspath=None,
             excludes=['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter'],
             datas=extra_files,
             runtime_hooks=None)

for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break


pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='gam',
          debug=False,
          strip=None,
          upx=False,
          console=True )
