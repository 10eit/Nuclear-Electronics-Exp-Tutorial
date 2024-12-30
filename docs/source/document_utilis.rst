=====
一些流水线工具
=====

如果你使用 `Python` 进行实验分析，在 GitHub 上可以使用以下代码方便处理，如果你不清楚函数使用的参数是什么，可以考虑利用 `help()` 函数或者查找本文档。

`wav_utils` 模块
=======================

1. `find_waves`

**描述：**

该函数用于从指定路径中查找所有 `.csv` 格式的波形文件。

**参数：**

:param path: 文件路径。
:type path: str
:return: 返回 `.csv` 文件的完整路径列表。
:rtype: list

**示例：**

.. code-block:: python

    files = find_waves("./data")
    print(files)

2. `filter_waveform`

**描述：**

根据实验步骤和类型字符串筛选波形文件。

**参数：**

:param path: 文件路径。
:type path: str
:param step: 实验步骤。
:type step: int
:param type_string: 波形类型（如 'landscape'）。
:type type_string: str
:return: 如果 `type_string` 为 `None`，返回第一个波形文件，否则返回符合条件的文件列表。
:rtype: list/str

**示例：**

.. code-block:: python

    wave_files = filter_waveform("./data", 1, "landscape")
    print(wave_files)

    # 当 type_string 为 None 时
    first_wave_file = filter_waveform("./data", 1, None)
    print(first_wave_file)

3. `read_wave`

**描述：**

读取 `.csv` 文件中的波形数据，返回时间、幅度、采样率和通道名。

**参数：**

:param path: 文件路径。
:type path: str
:param ch_name: 指定通道名，默认为 'auto'。
:type ch_name: str
:return: 返回时间数组、幅度数组、采样率和通道名。
:rtype: tuple

**示例：**

.. code-block:: python

    times, amplitude, fs, ch_name = read_wave("./data/step1_wave.csv")

4. `convert_time_units`

**描述：**

将时间点转换为合适的时间单位（ns、us、ms）。

**参数：**

:param fs: 采样率。
:type fs: int
:param time_points: 未缩放的时间点列表。
:type time_points: list
:return: 转换后的时间点和时间单位。
:rtype: tuple

**示例：**

.. code-block:: python

    scaled_time, unit = convert_time_units(1000, [0.1, 0.2, 0.3])

5. `wave2plot`

**描述：**

初步可视化示波器波形数据。

**参数：**

:param path: 文件路径。
:type path: str
:param step: 实验步骤。
:type step: int
:param type_string: 波形类型。
:type type_string: str
:param caption: 图表标题。
:type caption: str
:param yunit: Y轴单位。
:type yunit: str
:param multiple: 需要绘制的多个通道名。
:type multiple: list, 可选
:param alternative: 若有多个文件，指定索引选择文件。
:type alternative: int, 可选
:return: 返回绘图对象。
:rtype: matplotlib.figure.Figure

**示例：**

.. code-block:: python

    fig = wave2plot("./data", 1, "landscape", "示波器波形图", "V")
    fig.show()
