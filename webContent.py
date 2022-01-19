def get_html_lines(input_file):
    f = open(input_file, 'r', encoding='utf-8')  # 获取HTML内容，并将结果转为一个分行的列表
    s = f.readlines()
    f.close()
    # print(s)
    return s


def extract_image_urls(html_lines):  # 程序核心，解析文件并提取图像的url
    urls = []
    for line in html_lines:
        if "img" in line:
            url = line.split('src=')[-1].split('"')[1]  # 以src=为分割符保留最后一段，以"分隔
            # print(url)
            if "http" in url or "https" in url:
                urls.append(url)

    # print(urls)
    return urls


def show_results(urls):
    count = 0
    for url in urls:
        print("第{:2}个URL：{}".format(count, url))
        count += 1


def save_results(file_path, urls):
    f = open(file_path, 'w')
    for url in urls:
        f.write(url + "\n")
    f.close()


def main():
    input_file = "nation.html"
    output_file = 'nation_urls.txt'
    html_lines = get_html_lines(input_file)  # 获取HTML内容，并将结果转为一个分行的列表
    image_urls = extract_image_urls(html_lines)  # 程序核心，解析文件并提取图像的url
    show_results(image_urls)  # 将获取的链接输出到屏幕上面了
    save_results(output_file, image_urls)  # 保持结果到文件


main()
