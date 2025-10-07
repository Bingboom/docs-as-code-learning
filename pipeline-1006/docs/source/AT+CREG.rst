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
   :widths: 15 30 45

   * - 参数名
     - 描述
     - 取值范围
   * - <n>
     - 控制结果代码输出方式
     - 0: 禁用上报
1: 启用上报
2: 上报并包含LAC/CI信息
   * - <stat>
     - 网络注册状态
     - 0: 未注册
1: 已注册本地网络
2: 正在搜索

示例
----
.. code-block:: none

   命令: AT+CREG=1
   响应: OK

.. code-block:: none

   命令: AT+CREG?
   响应: +CREG: 0,1 OK

.. code-block:: none

   命令: AT+CREG=?
   响应: +CREG: (0-2) OK

**功能描述**：查询或控制模块的网络注册状态

**注意事项**：AT+CREG=5 返回 ERROR（参数超出范围）
