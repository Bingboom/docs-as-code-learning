
AT+CMSS
=======

**Title**: 发送已保存的短消息
**Types**: 执行, 查询

Formats::
   AT+CMSS

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <index>
     - 存储器中短信序号
     - N/A
   * - <da>
     - 文本模式下短信发送目的号码
     - N/A
   * - <toda>
     - type of address
     - N/A
   * - <mr>
     - 存储位置
     - N/A
   * - <scts>
     - 服务中心时间戳
     - N/A
   * - <ackpdu>
     - 3GPP 23.040 RP-User-Data element of RP-ACK PDU
     - N/A

**Description**: 发送存储器中<index>指定位置的短消息（SMS-SUBMIT），短消息发送成功后网络返回参考值<mr>给终端。\n命令格式