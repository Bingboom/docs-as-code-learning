
AT+XGAUTH
=========

**Title**: 用户认证
**Types**: 执行, 查询

Formats::
   AT+XGAUTH

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <cid>
     - (PDP Context Identifier)一个数字参数，指定一个PDP上下文定义
<cid>对应+CGDCONT中的<cid>。
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - (PDP
            - Context Identifier)一个数字参数
   * - <auth>
     - 鉴权类型，默认为1
0：NONE
1：PAP
2：CHAP
鉴权类型为非NONE时，需带<name>和<pwd>参数
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 0
            - NONE
          * - 1
            - PAP
          * - 2
            - CHAP
   * - <name>
     - 用户名
     - N/A
   * - <pwd>
     - 密码
     - N/A

**Description**: PDP认证。
该指令要放在AT+CGDCONT这条指令后面。目前在专网中各个地方逐渐增加了用户身份认证需求，使用内部协议栈，需要使用到这条指令，因此，请在代码流程上加上这条指令。
联通卡默认用户名和密码是“card”和“card”。
<cid>对应+CGDCONT中的<cid>。
<name>和<pwd>允许设置的最大字符串长度都是50
命令格式