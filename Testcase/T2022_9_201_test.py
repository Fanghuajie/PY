# NOTE: Generated By HttpRunner v3.1.6
# FROM: 2022-9-201.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseT20229201(HttpRunner):

    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/vcms/app/info")
            .get("http://58.49.165.22:8062/vcms/app/info")
            .with_params(
                **{"attClient": "1", "current": "1", "infoType": "2", "size": "5"}
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Authorization": "Bearer pig::91341600MA2MXAHD26::40b1774c-1aaf-4ce3-8c85-3ba00f8220bb",
                    "Connection": "keep-alive",
                    "Host": "58.49.165.22:8062",
                    "Referer": "http://58.49.165.22:8062/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
        ),
    ]


if __name__ == "__main__":
    TestCaseT20229201().test_start()