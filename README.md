# T_pai

Project for Tencent Machine Learning Contest


## 环境要求
*python2.7  
*scipy  
*numpy  
*matplotlib  
*pandas  
*sklearn  

## lib版本
安装后，运行versioncheck.py  
  
*scipy: 0.19.0  
*numpy: 1.12.1  
*matplotlib: 2.0.0  
*pandas: 0.19.2  
*sklearn: 0.18.1  
  
## 安装教程  

### 0.为什么不用用ubuntu呢?
推荐使用oracle的[virtualbox](https://www.virtualbox.org/wiki/Downloads)安装虚拟系统[ubuntu-kylin](https://www.ubuntu.com/download/ubuntu-kylin)/[ubuntu](https://www.ubuntu.com/download/desktop)

### 1.安装python2.7
百度一下呗

### 2.安装各式lib
[官网](https://www.scipy.org/install.html)  
在linux环境下，安装/更新pip：  
'''
python -m pip install --upgrade pip
'''
之后:  
'''
pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
'''
pip在某种情况下会使用非常小的cache进行连续安装;如果安装中报错出现MemoryError,用这个:  
'''
pip install --no-cache-dir --user numpy scipy matplotlib ipython jupyter pandas sympy nose
'''

### 3.运行versioncheck.py,检查版本统一

## 题目
[腾讯官网](http://algo.tpai.qq.com/home/information/index.html)  
每组数据有以下6维度：clickTime，creativeID，userID，positionID，connectionType，telecomsOperator  
其中 用户,素材,广告位 分别有自己的特征  
总之超麻烦，大家加油吧
