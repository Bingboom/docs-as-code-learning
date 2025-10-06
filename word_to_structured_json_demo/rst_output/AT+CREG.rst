AT+CREG
=======

**命令标题**：查询网络注册状态

**命令类型**：执行, 查询, 测试


命令格式::

   AT+CREG=[<n>]
   AT+CREG?
   AT+CREG=?

参数说明
--------

.. list-table::
   :header-rows: 1
   :widths: 15 30 40

   * - 参数名
     - 描述
     - 取值

   * - <n>
     - 控制结果代码输出方式
     - 0: 禁用上报\n1: 启用上报\n2: 上报并包含LAC/CI信息
   * - <stat>
     - 网络注册状态
     - 0: 未注册\n1: 已注册本地网络\n2: 正在搜索\n3: 注册被拒绝\n4: 未知\n5: 已注册漫游
   * - <Act>
     - 接入技术
     - 0: GSM\n2: UTRAN\n7: E-UTRAN

示例
----

.. code-block:: none

   AT+CREG=1
   OK

.. code-block:: none

   AT+CREG?
   +CREG: 0,1 OK

.. code-block:: none

   AT+CREG=?
   +CREG: (0-2) OK


**功能描述**：查询或控制模块的网络注册状态


**注意**：AT+CREG=5 返回 ERROR（参数超出范围）
