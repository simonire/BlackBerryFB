# BlackBerryFB

> ## 这是一个计算反馈电阻的程序。
>
> 选取`RES_0402_E96 电阻元件盒`中的电阻进行计算
>
> 省去在嘉立创扩展库选择巨贵电阻从而+20换料费的时间*（





用法：运行python



```python
##  +---- Vout   
##  |
##  | R1
##  |
##  +----FB      
##  |
##  | R2
##  +---- GND    
fb res:
```

会提示输入`Vfb`和`Vout`

```python
?Vfb=
?Vout=
```

一般可以有0.8v，1.0v，1.2v

vout看心情（



运行会选取`RES_0402_E96 电阻元件盒`中电阻进行计算，省去在嘉立创扩展库选择巨贵电阻从而+20换料费的时间*（



后面可能会做上位机/在线网页运行版（？）



# 举例：

`?Vfb= 0.8`，`?Vout=3.3`输出：

```python
min_v=3.381V    R1=2000K        R2=620K
min_v=3.224V    R1=1000K        R2=330K
min_v=3.227V    R1=910K R2=300K
min_v=3.23V     R1=820K R2=270K
min_v=3.21V     R1=750K R2=249K
min_v=3.273V    R1=680K R2=220K
min_v=3.28V     R1=620K R2=200K
min_v=3.289V    R1=560K R2=180K
min_v=3.35V     R1=510K R2=160K
min_v=3.295V    R1=499K R2=160K
min_v=3.307V    R1=470K R2=150K
min_v=3.446V    R1=430K R2=130K
min_v=3.4V      R1=390K R2=120K
min_v=3.2V      R1=360K R2=120K
min_v=3.2V      R1=330K R2=110K
min_v=3.2V      R1=300K R2=100K
min_v=3.434V    R1=270K R2=82K
min_v=3.229V    R1=249K R2=82K
min_v=3.388V    R1=220K R2=68K
min_v=3.381V    R1=200K R2=62K
min_v=3.371V    R1=180K R2=56K
min_v=3.31V     R1=160K R2=51K
min_v=3.353V    R1=150K R2=47K
min_v=3.219V    R1=130K R2=43K
min_v=3.262V    R1=120K R2=39K
min_v=3.244V    R1=110K R2=36K
min_v=3.224V    R1=100K R2=33K
min_v=3.227V    R1=91K  R2=30K
min_v=3.23V     R1=82K  R2=27K
min_v=3.21V     R1=75K  R2=24.9K
min_v=3.273V    R1=68K  R2=22K
min_v=3.28V     R1=62K  R2=20K
min_v=3.289V    R1=56K  R2=18K
min_v=3.35V     R1=51K  R2=16K
min_v=3.295V    R1=49.9K        R2=16K
min_v=3.307V    R1=47K  R2=15K
min_v=3.446V    R1=43K  R2=13K
min_v=3.4V      R1=39K  R2=12K
min_v=3.2V      R1=36K  R2=12K
min_v=3.2V      R1=33K  R2=11K
```

