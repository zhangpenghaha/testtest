import csv
import time
from lxml import etree
import requests

def main(job,pages):

    dicts ={}
    for page in range(1,pages+1):
        # 51job软件测试职位搜索网址
        url = "https://search.51job.com/list/180200,000000,0000,00,9,99,{},2,{}.html".format(job, page)
        response = requests.get(url)
        response.encoding = "gbk"
        result= response.text
        # 将页面源代码转化为能为Xpath匹配的格式
        html = etree.HTML(result)
        page_data_list = html.xpath("//div[@class='dw_table']")
        for page_dara in page_data_list:
            # 职位
            position = page_dara.xpath("//div/p/span/a/@title")
            # print(position)
            # 公司名称
            company = page_dara.xpath("//div/span[@class='t2']/a/@title")
            # print(company)
            # 地址
            address = page_dara.xpath("//div[@class='el']/span[@class='t3']")
            # print(address)
            #薪资
            salary = page_dara.xpath("//div[@class='el']/span[@class='t4']")
            # 发布日期
            data = page_dara.xpath("//div[@class='el']/span[@class='t5']")

            for i in range(len(position)):
                dicts[position[i]] = [company[i],address[i].text,salary[i].text,data[i].text]
        time.sleep(2)
        print(dicts)

        # 保存数据
        with open("软件测试职位{}.csv".format(time.strftime("%Y%m%d%H%M%S")), "w", newline='') as f:
            csvwrite = csv.writer(f,dialect=('excel'))
            csvwrite.writerow(['公司名称','职位','工作地点','薪资','发布时间'])
            for name in dicts:
                csvwrite.writerow([name,dicts[name][0],dicts[name][1],dicts[name][2],dicts[name][3]])


if __name__ == "__main__":

    main(19)