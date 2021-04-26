import asyncio

from pyppeteer import launch


async def main():
    # 初始化浏览器对象
    browser = await launch()
    # 在浏览器上下文中创建新页面
    page = await browser.newPage()
    # 打开目标网址
    await page.goto('http://localhost:8207/verify/cookie/index.html')
    # 点击指定按钮
    await page.click('.btn.btn-warning')
    # 读取页面指定位置的文本
    resp_list = await page.xpath('//div[@class="left col-md-10"]/p')
    for resp in resp_list:
        text = await(await resp.getProperty('textContent')).jsonValue()
        print(text)
    # text = await(await resp[0].getProperty('textContent')).jsonValue()
    # print(text)
    print(resp, type(resp))
    # 关闭浏览器对象
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
