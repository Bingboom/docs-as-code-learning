
.. _cmd-at+csms:

AT+CSMS：选择短信服务
=======

用于支持的短消息包括：发送（SMS-MO）、接收（SMS-MT）、小区广播（SMS-CB）。


测试命令
^^^^

**命令：**

::

    AT+CSMS=?<CR>

**响应：**

::


    <CR><LF>+CSMS: (list of supported <service>s)

    <CR><LF>OK<CR><LF>




参数
^^^^


- **<service>**：
  
    短信服务模式选择
  
  
    - 0：GSM03.40/GSM03.41 Phase 2
  
    - 1：GSM03.40/GSM03.41 Phase 2+
  

- **<mt>,<mo>,<bm>**：
  
    下行/上行/广播支持
  
  
    - 0：不支持
  
    - 1：支持
  



说明
^^^^
支持多种短消息服务类型

示例命令
^^^^^^^^

::



