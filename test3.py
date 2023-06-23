import wget
def hi():
    # 从文件中读取下载链接并存储在列表中
    with open('download.txt') as f:
        links = f.read().splitlines()

    versions = [link.split('/n')[0] for link in links]

    print("可用版本号：")
    for i, version in enumerate(versions):
        print(f"{i}: {version}")


    selected_index = input("请输入要下载的链接的索引：")
    try:
        selected_index = int(selected_index)
        selected_link = links[selected_index]
        selected_link_parts = selected_link.split()
        selected_link = ' '.join(selected_link_parts[1:])
    except (ValueError, IndexError):
        print("无效的索引！")
        selected_link = None


    if selected_link is None:
        error="没有找到所选链接！"
        return error
    else:
        wget.download(selected_link)


hi()