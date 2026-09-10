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

    page.wait_for_timeout(2000) 
    staff=page.get_by_text("Staff",exact=True)
    # print("Count=",staff.count())
    staff.click()
    page.wait_for_timeout(7000) 
    staff_card = page.locator("div").filter(
        has=page.get_by_role("heading", name="Staff 1")
    ).last

    staff_card.click()

    page.get_by_role("button", name="Edit").click()

    page.wait_for_timeout(5000)
    # page.get_by_placeholder("Phone").fill("9876543210")
    page.get_by_placeholder("Phone", exact=True).fill("9876543210")

    button = page.get_by_role("button", name="Update", exact=True)
    button.scroll_into_view_if_needed()
    button.click()
    
    page.wait_for_timeout(7000)
    browser.close()