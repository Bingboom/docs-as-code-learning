DEBUG: cmd['parameters'] valmap types and contents:
p['name']=<signal>, type(p.get('valmap'))=<class 'dict'>, p['valmap']={'0': '<4或99', '1': '<10', '2': '<16', '3': '<22', '4': '<28', '5': '>=28'}
p['name']=<ber>, type(p.get('valmap'))=<class 'dict'>, p['valmap']={'0...7': '参考GSM 05.08 8.2.4 章节表格中RXQUAL 的取值', '99': '误码率无法测量'}
TEMPLATE CONTENTS:
 
{{ cmd.command }}
{{ '=' * cmd.command|length }}

**Title**: {{ cmd.title }}
**Types**: {{ cmd.type|join(', ') }}

Formats::
{%- for f in cmd.formats %}
   {{ f }}
{%- endfor %}

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
{%- for p in cmd.parameters %}
   * - {{ p.name }}
     - {{ p.desc or '—' }}
     - {%- if p.valmap %}
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
{%- for k, v in p.valmap.items() %}
          * - {{ k }}
            - {{ v }}
{%- endfor %}
       {%- else %} N/A {%- endif %}
{%- endfor %}

Examples
--------
{%- for ex in cmd.examples %}
.. code-block:: none

   {{ ex.cmd }}
   {{ ex.resp }}
{%- endfor %}

**Description**: {{ cmd.description or '' }}

{%- if cmd.notes %}
**Notes**: {{ cmd.notes }}
{%- endif %}


AT+CSQ
======

**Title**: 获取信号强度
**Types**: 执行, 查询

Formats::
   AT+CSQ

Parameters
----------
.. list-table::
   :header-rows: 1
   :widths: 18 34 48

   * - Name
     - Description
     - Values
   * - <signal>
     - 信号强度CSQ
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 0
            - <4或99
          * - 1
            - <10
          * - 2
            - <16
          * - 3
            - <22
          * - 4
            - <28
          * - 5
            - >=28
   * - <ber>
     - Xx
     -
       .. list-table::
          :header-rows: 1
          :widths: 20 40

          * - Key
            - Value
          * - 0...7
            - 参考GSM 05.08 8.2.4 章节表格中RXQUAL 的取值
          * - 99
            - 误码率无法测量

Examples
--------
.. code-block:: none

   AT+CSQ
   

**Description**: 获取信号强度
