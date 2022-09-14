import logging
import os
import sys
import time
from asyncio.log import logger

import pytest
from Testcase.Email import EmailManage
logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    # pytest.main(["-vs", '-n=2'])
    # pytest.main(["-vs", '--reruns==2'])
    # pytest.main()
    # os.system("allure generate temp -o reports --clean")
    file = os.path.basename(sys.argv[0])
    # print(file)
    # print(sys.argv[0])
    try:
        print("开始执行脚本")
        logging.info("===============" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "================")
        # 每次生成数据前先清空数据
        pytest.main([r'D:\Users\FHJ\PycharmProjects\pythonProject\Testcase', "-m smoke or login", "--alluredir=./temp", "--clean-alluredir"])
        time.sleep(3)
        logging.info("脚本执行完成")
        # raise print("脚本批量执行失败")

    except Exception as e:
        logging.error("脚本批量执行失败！", e)
        print("脚本批量执行失败！", e)
    try:
        print("开始执行报告生成")
        os.system("allure generate temp -o reports --clean")
        logging.info("开始发送测试报告")
        # print("开始发送测试报告")
        # print("报告生成完毕")
        time.sleep(3)
        EmailManage().send_mail(r'D:\\Users\\FHJ\\PycharmProjects\\pythonProject\\reports\\index.html')

    except Exception as e:
        print("报告生成失败，请重新执行", e)
        # logger.error("报告生成失败，请重新执行", e)
        # log.error('执行用例失败，请检查环境配置')
        raise
    time.sleep(5)
