from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://rms.geckoworksnepal.com.np/login")

    table_input = page.get_by_placeholder("e.g. KTM-01")
    table_input.fill("GC-01")

    expect(table_input).to_have_value("GC-01")
    page.wait_for_timeout(5000)  


    table_input = page.get_by_placeholder("admin@gecko.works")
    table_input.fill("nabinbamthakuri2055@gmail.com")
    page.wait_for_timeout(5000)  

    table_input = page.get_by_placeholder("••••••••")
    table_input.fill("gecko01#")
    page.wait_for_timeout(5000)  

        
    authenticate = page.get_by_text("AUTHENTICATE", exact=True)

    # print("Authenticate count:", authenticate.count())

    authenticate.click()

    # page.get_by_role("button", name="Start Shift").click()
    page.wait_for_timeout(7000)  
    browser.close()
