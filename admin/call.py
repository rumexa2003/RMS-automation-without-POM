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
    page.wait_for_timeout(5000)  


    page.get_by_text("Settings", exact=True) .click()

    page.wait_for_timeout(5000)  

    external_link = page.get_by_role("link").filter(
    has=page.locator("svg.lucide-external-link")
    )

    with page.expect_popup() as popup_info:
     external_link.click()
     page.wait_for_timeout(5000)

    new_page = popup_info.value

    new_page.wait_for_load_state()

    new_page.wait_for_timeout(5000)

    call_waiter = new_page.get_by_text("Call Waiter", exact=True)

    call_waiter.click()

    table_input = new_page.get_by_placeholder("e.g. 5, A2, Outside-1")
    table_input.fill("Cafe-1")
    new_page.get_by_role("button", name="Call now").click()
    
    page.wait_for_timeout(7000)  
    browser.close()
