
AT+CSMS
=======

**Title**: 选择短信服务
**Types**: 执行, 查询

Formats::
   AT+CSMS

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <service>
     - 0：GSM03.40 and GSM03.41；SMS相关AT指令支持 GSM07.05 Phase 2
1：GSM03.40 and GSM03.41；SMS相关AT指令支持 GSM07.05 Phase 2+
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 0
            - GSM03.40 and GSM03.41
          * - SMS相关AT指令支持
            - GSM07.05 Phase 2+
          * - 1
            - GSM03.40 and GSM03.41
   * - <mt>,<mo>,<bm>
     - 0：不支持
1：支持
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 0
            - 不支持
          * - 1
            - 支持

**Description**: 用于支持的短消息包括：发送（SMS-MO）、接收（SMS-MT）、小区广播（SMS-CB）。
命令格式