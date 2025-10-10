
AT+IPR
======

**Title**: 设置模组波特率
**Types**: 执行, 查询

Formats::
   AT+IPR

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <baud rate>
     - 波特率
(0,1200,2400,4800,9600,14400,19200,28800,38400,57600,115200,256000,512000,921600)
     - N/A

**Description**: 设置模组波特率，默认掉电保存。
若波特率查询返回为0，表示模组波特率自适应。默认为波特率自适应（备注：自适应波特率不超过115200）。
命令格式