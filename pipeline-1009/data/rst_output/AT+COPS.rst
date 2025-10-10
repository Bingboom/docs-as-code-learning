
AT+COPS
=======

**Title**: 网络选择
**Types**: 执行, 查询

Formats::
   AT+COPS

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <mode>
     - 用来设置自动选择网络还是手动选择网络。
0：自动选择网络（忽略参数<oper>）
1：手动选择网络
2：从网络侧撤销注册
3：只设置<format>
4：先手动选择网络后自动选择网络（若手动选择网络不成功，就进入自动选择网络）
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 0
            - 自动选择网络（忽略参数<oper>）
          * - 1
            - 手动选择网络
          * - 2
            - 从网络侧撤销注册
          * - 3
            - 只设置<format>
          * - 4
            - 先手动选择网络后自动选择网络（若手动选择网络不成功
   * - <format>
     - 0：长字母<oper>（默认设置）
1：短格式字母<oper>
2：数字<oper>
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 0
            - 长字母<oper>（默认设置）
          * - 1
            - 短格式字母<oper>
          * - 2
            - 数字<oper>
   * - <oper>
     - 在<format>中被赋值，可以是16个符的长字母格式、8个符的短字母格式及5个符的数字格式（MCC/MNC）
     - N/A
   * - <AcT>
     - 显示无线接入技术，取值如下：
0：GSM
1：GSM compact
3：GSM w/EGPRS
7：E-UTRAN
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 取值如下
            - 
          * - 0
            - GSM
          * - 1
            - GSM compact
          * - 3
            - GSM w/EGPRS
          * - 7
            - E-UTRAN

**Description**: 查询网络。
命令格式