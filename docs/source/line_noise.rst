.. _示波器的使用:

示波器的使用
================
示波器预习：

示波器的原理（八股文）：详细见 https://zhuanlan.zhihu.com/p/87293941 开头

波形特征：

- 幅度：一般是峰值/均方根（RMS），后者指波形值平方求出平均电压，例如高中学过的对于周期交流电 :math:`V=f( t)`，那么我们会计算一个有效值

  .. math::
     V_{RMS}^{2} =\frac{1}{T}\int _{0}^{T}[ f( t)]^{2} \ \mathrm{d} t

  例如对于正弦交流电来说，我们高中就知道 :math:`V_{RMS} =V_{\max} /\sqrt{2}`。

- 相位差，即不同波形之间的水平偏移量。
- 周期和频率

不同信号的种类：

正弦波（阻尼正弦波、如果峰值会随着时间变化不断下降）、方波、矩形波、三角波锯齿波以及脉冲（可以用来做 trigger）

触发方式：https://core-electronics.com.au/guides/oscilloscope-triggers-what-how/

示波器的 trigger（触发） 和某些测量中会用到的多通道 trigger（标记触发） 有所不同，高精度测量用的 trigger 是利用在不同信号通道上输出一个脉冲信号（上升时间比较短）用于同步记录事件的发生。而示波器的trigger做的事情可能正好相反。在一个固定的时间轴（示波器屏幕上），如果波形一直在运动，那么我们就没法用肉眼去观测波形的形态是什么了，所以对于示波器而言，trigger检测的是“我是否需要更新上一幕出现的波形”，所以对于周期信号而言，我们可以在示波器屏幕上看到一个静态的正弦波。触发的方式有以下几种（一般的是前三种）：

- auto：自动处理，但是比较容易出现屏幕信号一直发生变化的情况。
- normal：设置一个阈值，如果信号的变化超过了阈值，则更新显示，否则要么显示空屏要么显示上一幕的静态波形，在有的示波器上会出现 WAIT 状态，也即示波器在等待 trigger 是否达到。
- 边缘触发（edge trigger）：设置了电压阈值和斜率变化的阈值，如果同时满足，则刷新屏幕显示波形。根据梯度的正负可以分为上升沿触发（rising edge）和下降沿触发（falling edge），一个示意图如下：

  .. image:: data-resources/b4d97fc8-477c-409e-ab6b-443211d3dc87

信号发生器和可编程电源：

预习不完了，看这段 https://www.elektroautomatik.cn/bidirectional/13042/

平稳信号和非平稳信号（非数学部分可以看https://blog.csdn.net/weixin_44939026/article/details/103210984）

数学一些的定义来自随机过程，我们考虑一个随机过程满足在时间或者空间尺度上的联合概率分布在任意平移后保持原有的联合概率分布，也即使得期望和方差不含时。

如果人话一点就是，平稳信号包含的信息量比较小，统计特征不随着时间改变而改变（你只需要测量一段时间，剩下的观测时不需要的），例如直流信号叠加白噪声（但是这不是周期信号，所以平稳信号并不一定都是周期信号）。所以我们可以直接考虑频域信息，因为无论怎样，时域上的信息总是一样的。

非平稳信号无法保证期望和方差不含时，一个最简单的例子就是人的心电信号与肌电信号，因为心电信号取决于每次心跳带来的震荡（刚跑完步和休息状态肯定是不一样的）在进行时频分析的非平稳信号是需要同时进行时域和频域信息提取的确定性信号，通过利用时频联合分析方法进行处理，获取信号的时频信息。

区分平稳信号和非平稳信号的标准是看信号特征统计量是否随着时间改变，不能单纯把周期性当成是判断标准。

.. tip::

    为什么不能用 auto

    下面这段回答了为什么不能使用示波器上的 auto 按钮。首先我们要知道 auto 干了啥，根据说明书：

    示波器将根据输入信号自动调整垂直档位、水平时基以及触发方式，使波形显示达到最佳状态。应用波形自动设置功能时要求正弦波的频率不小于 25 Hz。如果不满足此参数条件，则波形自动设置功能可能无效。以及 auto 按钮能够实现：

    .. image:: data-resources/375bad18-bb82-434f-a9c8-585cbbf787eb

    一个猜测是 auto 只能处理正弦波...跟周不周期、平稳不平稳没啥关系...（往届有人说能处理正弦波以外的东西，例如方波啊什么的。）

时域-频域表征（Time Frequency Representation，TFR）

之前我们了解了什么是平稳信号和非平稳信号，我们知道平稳信号在频域上的成分在任何时间窗口都成立，这也是为什么我们不需要对其做持续测量的原因。但是对于非平稳信号而言，我们在不同时间窗口上得到的频域信息都不一样，那么我们应该怎么表征时间/频率信息呢？

先从比较简单的入手，也就是 Fourier 变换用于将时域信号分解为不同频率的正弦和余弦分量。对于一个可积函数 :math:`f(t)`，其连续 Fourier 变换定义为：

.. math::
   \mathcal{F} \{f(t)\}=F(\omega )=\int _{-\infty }^{\infty } f(t)e^{-i\omega t} \ dt

但是 Fourier 变换只能得到频域上的信息，对于非平稳信号，在经过 Fourier 变换后会在频谱上出现小的 抖动（Jitter），一种解决方法是使用 Multitaper，也即使用滑动时间窗口来计算给定频率的功率。这种方法之所以叫multitaper，是因为在使用离散傅里叶变换计算功率之前信号都被加窗（taped）过了。

而小波分析通过缩放和平移一个称为母小波的函数来分析信号的局部特征，从而得到整体的时频信息。连续小波变换（Continuous Wavelet Transform, CWT）的定义为：

.. math::
   \mathcal{W}_{\psi } \{f(t)\}(a,b)=\frac{1}{\sqrt{|a|}}\int _{-\infty }^{\infty } f(t)\psi ^{*}\left(\frac{t-b}{a}\right) \ dt

其中：:math:`\psi (t)` 是母小波函数，满足有限能量和零平均值、:math:`a` 是尺度参数，控制小波的宽度、:math:`b` 是平移参数，控制小波的位置以及 :math:`\psi ^{*}` 表示 :math:`\psi ` 的复共轭。常用的小波变换方法有 Morlet 变换，只需要知道如何使用 Python 包即可（例如 scipy 或 neurodsp）。在后续的实验里，我们应该大概率碰到的都是非平稳信号，因此早日学会怎么使用 TFR 可以得到更好的时频分析结果。

.. tip::

    好消息，示波器支持 FFT。只需要按 MATH 操作，选择“FFT”后，可以设置 FFT 运算的参数。（可惜的是看了示波器没有即时的 notch 滤波，不知道使用 band-stop filter 能否实现这么小范围的滤波）

波形文件存储的规则

编辑波形文件用的是 .raf 文件，是一种私有格式，无论是做科研还是看盗版这并不是好的。大家常用的 .mp3 和 .mp4 格式也是私有的，因此在一些开源软件和系统中需要使用第三方工具才能打开，或者根本无法支持。

从示波器中导出的波形文件一般是 .csv 文件，一般来说在表头部分会有采样率（sample rate），这样可以根据不同时间节点的幅值还原在真实时间上的信息。

如果你的记录时间很长，且信号的变化并不明显，可以考虑使用降采样（downsampling）方法降低数据量（后续分析中越大的数据需要的资源越多），但是并不是无脑降采样，我们有 Nyquist-Shannon 采样定理：

如果一个函数 :math:`x( t)` 的不含有高于 :math:`B\ \operatorname{Hz}` 的频率成分，那么我们可以使用一条等距距离小于 :math:`1/( 2B) \ \operatorname{s}` 的序列完全确定信号的形态。

简单来说就是我们要从抽样信号中无失真的还原原有信号，那么采样频率必须大于两倍的最高频率，因此降采样应当根据 Nyquist 定理选择目标频率。