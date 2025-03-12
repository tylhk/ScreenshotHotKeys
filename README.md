# ScreenshotHotKeys

**基于AutoHotkey的自定义windows自带截屏快捷键**<br>
个人博客指路：[satone1008.cn](satone1008.cn)<br>
博客文章指路：[自定义windows自带截屏快捷键](https://satone1008.cn/?p=306)
## 使用前须知

- 本程序基于AutoHotkey开发，使用前需先进行AutoHotkey的安装。文件夹内已包含对应版本的安装包，您亦可通过[软件官网](https://www.autohotkey.com/)进行下载（请选择1.1版本）。
- 您可直接运行`ScreenshotHotKeys.py`文件或是运行`./dist`目录下的`ScreenshotHotkey.exe`文件。
- AutoHotkey安装后会自动开机自启并后台静默运行，无需再进行其余操作。

## 使用说明

1. 使用`win+R`打开运行栏并在输入`shell:startup`后回车，弹出文件夹窗口后复制地址栏的地址。示例：`C:\Users\hp\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`，将复制的地址粘贴入程序的输入框中。
2. 点击检测组合键，再点击弹出的新窗口，在键盘上按住想要设置的截图快捷键（单键亦可）的同时关闭窗口。*注意：如果与电脑自带的热键冲突会导致设置失败，我自己常用的截图快捷键有F1，F2，win+c，可供参考。还有一些不常用的按键我并没有写入程序内，如有需要，可通过博客联系我添加或是自行修改py文件。*
3. 点击生成AHK文件。若生成成功即可双击对应地址生成的.ahk文件运行脚本并尝试快捷键是否生效，之后脚本会随电脑开机自动启动。如果想更改快捷键设置可直接在程序内修改，会自动进行覆盖。
