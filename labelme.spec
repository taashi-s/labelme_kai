# -*- mode: python -*-
# vim: ft=python


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=['labelme_kai'],
    binaries=[],
    datas=[
        ('labelme_kai/config/default_config.yaml', 'labelme_kai/config'),
        ('labelme_kai/icons/*', 'labelme_kai/icons'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=['matplotlib'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='labelme_kai',
    debug=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=False,
    icon='labelme_kai/icons/icon.ico',
)
app = BUNDLE(
    exe,
    name='labelme_kai.app',
    icon='labelme_kai/icons/icon.icns',
    bundle_identifier=None,
    info_plist={'NSHighResolutionCapable': 'True'},
)
