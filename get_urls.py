import requests
requests.packages.urllib3.disable_warnings()
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
}

home_page = 'https://about.muse.jhu.edu/resources/freeresourcescovid19/'

def req_get(this_url):
    page = requests.get(url=this_url, headers=headers, verify=False)
    page_thing = etree.HTML(page.text)
    return page_thing


def get_urls():
    home_page_req = requests.get(url=home_page, headers=headers, verify=False)
    tree = etree.HTML(home_page_req.text)
    publishers = tree.xpath('//div[@class="box_shadow"]/ul/li/a/@href')


    # publishers = etree.HTML(home_page_req).xpaht('//div[@class="box_shadow"]/ul/li/a/@href')

    for index, url in enumerate(publishers):
        print(url)
        each_pub = req_get(url)







        if index == 1:
            break


if __name__ == '__main__':
    pass
    get_urls()
