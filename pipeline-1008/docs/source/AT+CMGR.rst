
AT+CMGR
=======

**Title**: 读短消息
**Types**: 执行, 查询

Formats::
   AT+CMGR

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <index>
     - 短信在<mem1>的索引号，CMGR读取的是<mem1>的短信
     - N/A
   * - <stat>
     - TEXT mode
“REC UNREAD”已接收未读取的消息
“REC READ”已接收已读取的消息
“STO UNSENT”已存储未发送的消息
“STO SENT”已存储已发送的消息
PDU mode
0 已接收未读取的消息
1 已接收已读取的消息
2 已存储未发送的消息
3 已存储已发送的消息
     - N/A
   * - <alpha>
     - 以字符型的数字来表示。
     - N/A
   * - <length>
     - 给定的TP层数据单元的八位位组代码数目（不包含服务中心地址的八位位组）。
     - N/A
   * - <pdu>
     - PDU数据。
     - N/A

**Description**: 读取当前存储器中的短消息（需预先通过AT+CPMS指令设定当前存储器）。\n如果接收到的短信状态是未读的，执行该指令后，短信存储状态就变成已读。\n命令格式