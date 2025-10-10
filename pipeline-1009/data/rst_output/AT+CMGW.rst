
AT+CMGW
=======

**Title**: 写短消息
**Types**: 执行, 查询

Formats::
   AT+CMGW

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <da>
     - 文本模式下短信发送目的号码
     - N/A
   * - <text>
     - 文本模式下短信内容
     - N/A
   * - <length>
     - PDU模式下短信内容的字节长度
     - N/A
   * - <index>
     - 位置信息
     - N/A
   * - <CR>
     - 结束符
     - N/A
   * - <Ctrl+Z>
     - 表示输入消息体的结束，即示例中的符号“”
     - N/A
   * - <ESC>
     - 表示放弃输入消息体
     - N/A

**Description**: 往存储器中写入短消息，正确存储后返回位置信息<index>。
命令格式