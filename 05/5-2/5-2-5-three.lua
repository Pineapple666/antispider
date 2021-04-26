function main(splash)
    splash:go('https://www.ituring.com.cn/')
    splash:wait(0.2)
    -- 聚焦搜索框
    splash:select('input[name=q]'):focus()
    -- 在搜索框中输入Python
    splash:send_text('Python')
    splash:wait(0.2)
    print(splash:png())
--    return {
--        png = splash:png()
--    }
end