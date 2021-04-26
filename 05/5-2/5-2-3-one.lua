function main(splash)
    -- 指定访问的url
    splash:go('http://quotes.toscrape.com/')
    -- 等待0.5秒钟
    splash:wait(0.5)
    title = splash:select('h1 > a'):text()
    return {
        result = title
    }
end
