from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://rms.geckoworksnepal.com.np/staff/login")

    table_input = page.get_by_placeholder("GECKO-01")
    table_input.fill("GC-01")

    expect(table_input).to_have_value("GC-01")

    page.get_by_role("button", name="Activate System").click()
    page.get_by_role("button", name="Anish").click()
    page.wait_for_timeout(1000)  # Add between critical actions

    for i in range(4):
        page.get_by_role("button", name="0").click()
    page.wait_for_timeout(1000)  # Add between critical actions

    page.get_by_role("button", name="Start Shift").click()
    page.wait_for_timeout(1000)  # Add between critical actions

    page.get_by_text("START SHIFT").click()

    page.wait_for_timeout(1000)  # Add between critical actions

    expect(page).to_have_url("https://rms.geckoworksnepal.com.np/staff/kitchen")
    
    page.get_by_role("button", name="Acknowledge").click()
    page.wait_for_timeout(1000)  # Add between critical actions

    page.get_by_text("START SHIFT").click()
    
    page.get_by_text("C-4").click()
    # Click any order card that has the food item name
    # page.get_by_text("Chinese Chop Suey (Indo-Chinese style) (Veg)").click()

    # Or find by order number dynamically
    # order_number = "C-4"
    # page.get_by_text(order_number).click()
    page.wait_for_timeout(1000)  # Add between critical actions

    page.get_by_role("button", name="Start Preparing").click()
    page.get_by_role("button", name="All Ready").click()

    


    browser.close()
