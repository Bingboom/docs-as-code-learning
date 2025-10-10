
AT+CGDCONT
==========

**Title**: 设置PDP格式
**Types**: 执行, 查询

Formats::
   AT+CGDCONT

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <cid>
     - (PDP Context Identifier)一个数字参数，指定一个PDP上下文定义，这个参数是当地的TE-MT接口并且被应用到其他PDP上下文相关的命令当中，使用查询命令可以查询到允许的值(最小值为1)。
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - (PDP
            - Context Identifier)一个数字参数
          * - 这个参数是当地的TE
            - MT接口并且被应用到其他PDP上下文相关的命令当中
   * - <PDP_type>
     - (Packet Data Protocol type)字符串参数，用于指定分组数据协议的类型
“IP”网络协议（Internet Protocol）（IETFSTD 5）
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - (Packet
            - Data Protocol type)字符串参数
          * - “IP”网络协议（Internet
            - Protocol）（IETFSTD 5）
   * - <APN>
     - (Access Point Name)字符串形式，是一个逻辑名称，用来选择GGSN或者外部分组数据网。
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - (Access
            - Point Name)字符串形式
   * - <PDP_address>
     - 字符串形式，用来在地址空间中区分MT。
如果不写这个参数，则在PDP的启动过程当中由TE提供这个值。
如果TE提供失败，就请求动态地址，即使在PDP的启动过程当中分配了地址，在使用这条指令查询的时候仍然会返回空。
     - N/A
   * - <d_comp>
     - 数字参数用来控制PDP数据压缩（仅适用于SNDCP）
0 - off (缺省情况下默认值)
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 0
            - off (缺省情况下默认值)
   * - <h_comp>
     - 数字参数用来控制PDP头部压缩0 - off (缺省情况下默认值)
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 数字参数用来控制PDP头部压缩0
            - off (缺省情况下默认值)
   * - <pd1>, … <pdN>
     - 0到N，字符串类型，意义与<PDP_type>有关
     - N/A

**Description**: 设置GPRS的PDP（Packet Data Protocol，分组数据协议）格式。APN允许设置的长度最长是50。
命令格式