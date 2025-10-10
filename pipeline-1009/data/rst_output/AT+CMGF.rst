
AT+CMGF
=======

**Title**: 设置短消息模式
**Types**: 执行, 查询

Formats::
   AT+CMGF

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <mode>
     - 0：PDU模式(默认)
1：文本模式
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 0
            - PDU模式(默认)
          * - 1
            - 文本模式

**Description**: 设置短信的输入模式。
命令格式