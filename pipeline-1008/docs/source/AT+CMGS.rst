
AT+CMGS
=======

**Title**: 发送短消息
**Types**: 执行, 查询

Formats::
   AT+CMGS

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
   * - <mr>
     - 存储位置
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
   * - <scts>
     - 服务中心时间戳
     - N/A
   * - <ackpdu>
     - GPP 23.040 RP-User-Data element of RP-ACK PDU
     - N/A

**Description**: 将短消息从模组发送到网络，短消息发送成功后网络返回参考值<mr>给模组。\n命令格式