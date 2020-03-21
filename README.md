# Wox.Plugin.PasswordGenerator
Wox插件，密码生成器

需要手动按装clipboard组件

    pip install clipboard

Python需要3.6以上版本

使用方式：

    passwd

生成20长度的字符大小写+数字密码 (默认)

    passwd 20s

生成20长度高强度(strong)密码，字符大小写+数字+特殊字符

    passwd uuid

生成UUID

打包方式：

压缩为zip格式文件，改名如下：
Wox.Plugin.Passwd-88430272-FEF8-4390-90F8-A7D3F88D27C9.wox