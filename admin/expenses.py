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


    inventory=page.get_by_text("Inventory",exact=True)
    inventory.click()
    page.wait_for_timeout(2000)


    add=page.get_by_role("button",name="Log Cashflow")
    add.click()
    page.wait_for_timeout(2000)

   
    # e.g. Plumber Fixing Sink

    t=page.get_by_placeholder("e.g. Plumber Fixing Sink")
    t.fill("Electricity")
     # Click chevron-down dropdown
    page.locator("svg.lucide-chevron-down").click()
    page.wait_for_timeout(1000)
    
    page.wait_for_timeout(5000)

    amount = page.locator('input[name="amount"]')
    amount.fill("5000")
    page.wait_for_timeout(5000)

    date_input = page.locator('input[name="date"]')
    # date_input.fill()
    page.wait_for_timeout(5000)

    date_input.fill("2026-09-09") 
    page.get_by_role("button", name="Save Expense",exact=True).click()
    page.wait_for_timeout(5000)

    page.wait_for_timeout(7000)  
    browser.close()
