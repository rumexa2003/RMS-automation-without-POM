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
    authenticate.click()

    page.wait_for_timeout(7000) 
    staff=page.get_by_text("Staff",exact=True)
    # print("Count=",staff.count())
    staff.click()
    page.wait_for_timeout(10000) 

    page.get_by_role("button", name="New Staff", exact =True).click()
    page.wait_for_timeout(1000)  

    category_input = page.get_by_placeholder("e.g. Nischal Shrestha")
    category_input.fill("Staff 1")

    role = page.locator('select[name="role"]')

    expect(role).to_be_visible()
    role.select_option("cashier")
    expect(role).to_have_value("cashier")

    pin= page.get_by_placeholder("0000")
    pin.fill("0000")
   
    button = page.get_by_role("button", name="Create ", exact=True)
    button.scroll_into_view_if_needed()
    button.click()

    browser.close()