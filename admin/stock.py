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

    inventory=page.get_by_text("Inventory",exact=True)
    inventory.click()
    page.wait_for_timeout(2000)

    add=page.get_by_role("button",name="Add Stock")
    add.click()
    page.wait_for_timeout(2000)

   
    name = page.get_by_placeholder("e.g. Jack Daniels")
    name.fill("Coke")

    
    selected_category = page.get_by_text(
        "packaged",
        exact=True
    ).locator("xpath=..")

    selected_category.click()

    #form
    category_dropdown_text = page.locator("form").get_by_text(
        "drinks",
        exact=True
    )

    print("Category count:", category_dropdown_text.count())
    print("Category visible:", category_dropdown_text.is_visible())

    
    category_dropdown_text.click()

    
    drink_option = page.locator("span.capitalize").filter(
        has_text="drinks"
    )

    # print("Drink option count:", drink_option.count())
    # print("Drink option visible:", drink_option.is_visible())

    
    # print("Drink option HTML:")
    # print(drink_option.evaluate("(el) => el.outerHTML"))

    
    drink_option.click()

    
    page.get_by_text("Manual (Not Linked)", exact=True).click()

    
    page.get_by_text("Coke", exact=True).click()

    
    stock = page.locator('input[name="stock"]')
    stock.fill("10")
    page.wait_for_timeout(2000)

    
    cost_price = page.locator('input[name="cost_price"]')
    cost_price.fill("90")
    page.wait_for_timeout(2000)

    price = page.locator('input[name="price"]')
    price.fill("100")
    page.wait_for_timeout(2000)


    page.get_by_role("button", name="Save to Vault").click()

    page.wait_for_timeout(7000)

    browser.close()