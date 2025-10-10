
AT+CLCK
=======

**Title**: PIN使能与查询功能指令
**Types**: 执行, 查询

Formats::
   AT+CLCK

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <fac>
     - 需带双引号""
"OI"：呼出国际电话
"SC"：SIM卡
"AO"：呼出电话
"OX"：除了归属地外所有呼出国际电话
"FD"：SIM卡固定拨号空间
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 需带双引号""
"OI"
            - 呼出国际电话
"S
          * - "
            - SIM卡
"AO"：呼出电话
"OX"：除了归属地外所有呼出国际电话
"
          * - D"
            - SIM卡固定拨号空间
   * - <mode>
     - 0：解锁
1：锁定
2：查询状态
     - N/A
   * - <status>
     - 0：not active
1：active
     - N/A
   * - <passwd>
     - 密码或操作码，字符串类型，需带双引号""
     - N/A
   * - <classx>
     - 1：语音服务类型
2：数据服务类型
4：fax服务类型
8：短消息
16：同步数据业务
32：异步数据业务
64：专用包接入
128：专用数据包装拆器接入
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 6
            - 同步数据业务
32：异步数据业务
64：专用包接入
          * - 28
            - 专用数据包装拆器接入

**Description**: 锁、解锁以及查询MT和网络设备。设置该参数，重启模组后生效。\n命令格式