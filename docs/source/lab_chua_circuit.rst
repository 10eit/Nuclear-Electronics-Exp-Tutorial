.. _非线性物理一混沌:

近代物理实验：非线性物理一混沌
================

引言
----

非线性是在自然界广泛存在的自然规律，相对于我们熟悉的线性要复杂得多。随着物理学研究的不断深入，非线性问题逐渐被重视起来，现已出现了多个分支，混沌便是其中之一。混沌现象在生活中广泛存在，如著名的蝴蝶效应、湍流、昆虫繁衍等。

要直观地演示混沌现象，采用非线性电路是一个非常好的选择。
能产生混沌现象的自治电路至少满足以下三个条件 
1. 有一个非线性元件，非线性元件是一种电气元件，它在电流和电压之间不存在任何线性关系。一个典型的例子就是二极管。
2. 有一个用于耗散能量的电阻
3. 有三个存储能量的元件。

.. note::
    在谈论自治电路之前，我们需要讨论一下自治系统的概念。考虑 :math:`\mathbb{T} \subset \mathbb{R}` 是一个区间，考虑 :math:`\mathbb{R}^{n}` 上区域 :math:`D`，设在时间 :math:`t \in \mathbb{T}` 有一个质点的坐标为

    .. math::
        \mathbf{x} = (x_{1}, x_{2}, \dotsc, x_{n})^{\top} \in D

    定义速度向量：

    .. math::
        \mathbf{f}(t, \mathbf{x}) = (f_{1}(t, \mathbf{x}), \dotsc, f_{n}(t, \mathbf{x}))^{\top} \in C(\mathbb{T} \times D, \mathbb{R}^{n})

    这样在 :math:`D` 中定义了一个向量场，则 :math:`Q` 点的运动可以使用：

    .. math::
        \frac{\mathrm{d}\mathbf{x}}{\mathrm{d}t} = \mathbf{f}(t, \mathbf{x})

    来表述，我们称 :math:`Q` 运动的空间 :math:`\mathbb{R}^{n}` 为相空间（phase space），方程的积分曲线 :math:`(t, \mathbf{x}(t))` 在相空间的图形称作是相轨线（phase trajectory）。

    如果 :math:`\mathbf{f}(t, \mathbf{x})` 不显含时，也即：

    .. math::
        \frac{\partial \mathbf{f}}{\partial t}(t, \mathbf{x}) = 0

    那么我们称这是一个自治系统或者说是定常系统。而自治电路是一种在没有时变输入（即只有直流电源作为输入）的情况下产生时变输出的电路
