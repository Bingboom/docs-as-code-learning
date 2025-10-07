AT+CWJAP
========

**命令标题**：连接WiFi网络

**命令类型**：设置, 查询

命令格式::
  AT+CWJAP=<ssid>,<pwd>[,<bssid>][,<prio>]
  AT+CWJAP?

参数说明
--------
.. list-table::
   :header-rows: 1
   :widths: 15 30 45

   * - 参数名
     - 描述
     - 取值范围
   * - <ssid>
     - WiFi名称
     - 格式: 字符串
长度: 1-32字节
   * - <pwd>
     - WiFi密码
     - 格式: ASCII字符
长度: 8-64字节

示例
----
.. code-block:: none

   命令: AT+CWJAP="MyWiFi","123456"
   响应: OK

.. code-block:: none

   命令: AT+CWJAP?
   响应: +CWJAP:"MyWiFi","aa:bb:cc:dd:ee:ff",-50,1 OK

**功能描述**：连接到指定WiFi网络

**注意事项**：密码需为8-64字节ASCII字符
