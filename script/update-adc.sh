#!/usr/bin/env bash

# 获取最新发布版本的URL
latest_release_url=$(curl -s -L -o /dev/null -w %{url_effective} https://github.com/TC999/AppDataCleaner/releases/latest)

# 提取最后一个"/"后面的内容
version=$(echo $latest_release_url | awk -F'/' '{print $NF}')

# 输出版本号
echo $version

# 进入WCMain
cd WCMain

# 删除
rm -f AppDataCleaner.exe
# 下载
wget "https://github.com/TC999/AppDataCleaner/releases/download/$version/AppDataCleaner.exe"
