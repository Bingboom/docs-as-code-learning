.. _cmd-at+csms:

AT+CSMS — 选择短信服务
================

用于支持的短消息包括：发送（SMS-MO）、接收（SMS-MT）、小区广播（SMS-CB）。
命令

执行命令
^^^^^^^^

**命令：**

::

    AT+CSMS

**响应：**

::

    <CR><LF>OK<CR><LF>


参数
^^^^

-  **<service>**：

    - 0: GSM03.40 and GSM03.41；SMS相关AT指令支持 GSM07.05 Phase 2
    - 1: GSM03.40 and GSM03.41；SMS相关AT指令支持 GSM07.05 Phase 2+

-  **<mt>,<mo>,<bm>**：

    - 0: 不支持
    - 1: 支持




说明
^^^^
说明示例2

示例命令
^^^^^^^^

::

    AT+CSMS
    
    OK
