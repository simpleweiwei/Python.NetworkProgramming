import ntplib
from time import ctime


# 获取网络时间
def get_net_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request("ch.pool.ntp.org")  # 记着用中国的时间
    print(ctime(response.tx_time))


if __name__ == '__main__':
    get_net_time()
