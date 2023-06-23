import wget

# 从文件中读取下载链接并存储在列表中
with open('download.txt') as f:
    links = f.read().splitlines()

# 获取所有可用版本号
versions = set(link.split('/')[0] for link in links)

# 显示所有可用版本号供用户选择
print("可用版本号：")
for i, version in enumerate(sorted(versions)):
    print(f"{i}: {version}")

# 获取用户选择的版本号
selected_index = input("请输入要下载的版本号的索引：")
try:
    selected_index = int(selected_index)
    selected_version = sorted(versions)[selected_index]
except (ValueError, IndexError):
    print("无效的索引！")
    selected_version = None

# 检查是否找到所选版本的链接
if selected_version is None:
    print("没有找到所选版本的链接！")
else:
    # 获取所选版本的链接
    selected_links = [link for link in links if link.startswith(selected_version)]
    if not selected_links:
        print(f"没有找到版本号为{selected_version}的链接！")
    else:
        # 显示所选版本的链接供用户选择
        print("可用链接：")
        for i, link in enumerate(selected_links):
            print(f"{i}: {link}")

        # 获取用户选择的链接
        selected_index = input("请输入要下载的链接的索引：")
        try:
            selected_index = int(selected_index)
            selected_link = selected_links[selected_index]
        except (ValueError, IndexError):
            print("无效的索引！")
            selected_link = None

        # 检查是否找到所选链接
        if selected_link is None:
            print("没有找到所选链接！")
        else:
            # 使用wget下载所选链接
            wget.download(selected_link)