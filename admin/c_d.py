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

    page.wait_for_timeout(5000)  

    menu = page.get_by_text("Menu Engine", exact=True)
    # print("menu count:", menu.count())
    menu.click()
  
    page.wait_for_timeout(2000)

    page.get_by_role("button", name="New Category").click()
    page.wait_for_timeout(2000)
    
    category_input = page.get_by_placeholder("e.g. Starters")
    category_input.fill("Automation Category")
    page.wait_for_timeout(2000)

    page.get_by_role("button", name="Create").click()
    page.wait_for_timeout(10000)

    Auto= page.get_by_text("Automation Category", exact=True)
    Auto.click()
    page.wait_for_timeout(5000)


    page.get_by_role("button", name=" Dish").click()
    page.wait_for_timeout(2000)
    
    
    dish_name_input = page.get_by_placeholder("Item Name")
    dish_name_input.fill("Signature Burger")
    page.wait_for_timeout(2000)
    

    price_input = page.locator("input[type='number'][placeholder='0']")
    price_input.fill("350")

    
    page.evaluate("window.scrollBy(0, 500)")  
    
    page.get_by_role("button", name="Save Dish").click() 

    page.wait_for_timeout(7000)  
    browser.close()
