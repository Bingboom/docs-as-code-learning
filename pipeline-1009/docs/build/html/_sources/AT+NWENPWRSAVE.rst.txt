
AT+NWENPWRSAVE
==============

**Title**: 休眠（Sleep）设置
**Types**: 执行, 查询

Formats::
   AT+NWENPWRSAVE

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <n>
     - 0：不允许进入休眠模式（默认）
1：允许进入休眠模式（DTR信号低电平进入休眠，高电平退出休眠）
2：允许进入休眠模式（DTR信号高电平进入休眠，低电平退出休眠）
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 0
            - 不允许进入休眠模式（默认）
          * - 1
            - 允许进入休眠模式（DTR信号低电平进入休眠
          * - 2
            - 允许进入休眠模式（DTR信号高电平进入休眠
   * - <usb>
     - 0：不允许USB远程休眠唤醒（缺省）
1：使能USB远程休眠唤醒（USB主机挂起USB总线模组才能进入休眠，USB主机恢复USB总线会唤醒模组，有网络下行事件（数据、短信、电话）时模组会通过USB总线唤醒USB主机）
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 0
            - 不允许USB远程休眠唤醒（缺省）
          * - 1
            - 使能USB远程休眠唤醒（USB主机挂起USB总线模组才能进入休眠

**Description**: 设置是否允许模组进入休眠（Sleep）模式。该命令设置掉电不保存。
模组DTR信号默认为低电平：
发送允许进入休眠模式指令之后，且模组DTR信号为低（或高）电平，模组内部各个部分的电路都允许进入休眠状态模组才能进入休眠。
命令格式