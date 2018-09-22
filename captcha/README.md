[//]: # (Image References)

[image1]: ./images/preview.png "Sample Output"

# 爱科研人工智能科研实训毕业项目

## 项目概述

欢迎来到卷积神经网络（CNN）项目！本项目会通过 Keras 搭建一个深度卷积神经网络来识别 captcha 验证码，建议使用显卡来运行该项目，Keras 版本：2.1.0。

captcha 是用 python 写的生成验证码的库，它支持图片验证码和语音验证码，我们使用的是它生成图片验证码的功能。

## 项目预览

![Sample Output][image1]

## 项目指南

### 步骤

1. 进入文件夹，激活环境并安装captcha。

 ```bash
cd iResearch/captcha
source activate iResearch
pip install captcha
```

2. 打开 notebook

 ```
jupyter notebook captcha.ipynb
```

__注意：__ 我们虽然已经实现了一些代码，让你更快地开始工作，你仍需要实现额外的功能，以回答 notebook 中所有的问题。
__除非有要求，否则不要修改任何已经包含的代码。__

## 项目提交

当你准备好提交你的项目时，将下列文件整理并压缩成一个文件，以便上传。

- 代码完整可运行的文件 `captcha.ipynb`，所有的代码块都要执行并展示结果，并要求回答所有问题
- 将你的 notebook 导出为 HTML 或 PDF 格式，并以 `report.html` 或是 `report.pdf` 命名
- 任何用于项目中，并且并非由我们为这一项目提供的额外数据图片。
