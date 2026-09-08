from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://rms.geckoworksnepal.com.np/staff/login")

    table_input = page.get_by_placeholder("GECKO-01")
    table_input.fill("GC-01")

    expect(table_input).to_have_value("GC-01")

    page.get_by_role("button", name="Activate System").click()
    page.get_by_role("button", name="Bar").click()
    page.wait_for_timeout(1000)  # Add between critical actions

    for i in range(4):
        page.get_by_role("button", name="0").click()
    page.wait_for_timeout(1000)  # Add between critical actions

    page.get_by_role("button", name="Start Shift").click()
    page.wait_for_timeout(1000)  # Add between critical actions

    page.get_by_text("START SHIFT").click()

    page.wait_for_timeout(7000)  # Add between critical actions

    expect(page).to_have_url("https://rms.geckoworksnepal.com.np/staff/bartender")
    page.wait_for_timeout(1000)  # Add between critical actions
    
    menu_icon = page.locator("svg.lucide-layout-grid")
    

    menu_icon.click()

    page.get_by_role("button", name="Category").click()
    page.wait_for_timeout(2000)
        
        # Locate and fill the category name input
    category_input = page.get_by_placeholder("e.g. Cocktails, Hookah")
    category_input.fill("Automation Category")
    page.wait_for_timeout(2000)
    
    page.get_by_role("button", name="Create").click()
    page.wait_for_timeout(2000)
    
    page.get_by_text("New Drink").click()
    page.wait_for_timeout(2000)
        
        # Locate and fill the drink name input
    drink_name_input = page.get_by_placeholder("e.g. Classic Mojito")
    drink_name_input.fill("test drink")
    page.wait_for_timeout(2000)
        
        # Locate and fill the price input
    price_input = page.locator("input[type='number'][placeholder='0']")
    price_input.fill("350")
    page.wait_for_timeout(2000)
        
        # Scroll down to see the "Save Drink" button
    page.evaluate("window.scrollBy(0, 500)")  # Scroll down 500px
    page.wait_for_timeout(2000)
        
        # Click on "Save Drink" button
    page.get_by_role("button", name="Save Drink").click()
    page.wait_for_timeout(3000)
    page.wait_for_timeout(7000)

    browser.close()
