整个接口测试流程：从用例Excel文件中读取case，然后依次对接口进行调用测试，然后生成接口测试结果文件。期间对测试不通过的case在禅道zt_bug表做记录。

所需工具或文件：
1、接口用例文件interfaceTestExcel.xlsx
2、部署禅道环境（mysql环境、php环境、apche环境）
3、接口测试文件interface.py

注意：Mac上部署禅道环境时session.save_path的配置文件名必须时php.ini文件（没有时可以复制一份），同时配置好之后还需要重启apche以便其生效。
