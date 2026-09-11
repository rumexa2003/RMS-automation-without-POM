from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://rms.geckoworksnepal.com.np/staff/login")

    table_input = page.get_by_placeholder("GECKO-01")
    table_input.fill("GC-01")

    expect(table_input).to_have_value("GC-01")

    page.get_by_role("button", name="Activate System").click()
    page.get_by_role("button", name="Nabin").click()
    page.wait_for_timeout(1000)  

    for i in range(4):
        page.get_by_role("button", name="0").click()
    page.wait_for_timeout(1000)  

    page.get_by_role("button", name="Start Shift").click()
    link = page.get_by_role("link", name="Specials", exact=True)
    link.click()
    page.wait_for_timeout(1000)  

    dish = page.locator("div.grid.grid-cols-12").filter(
    has_text="American Chopsey"
    )

    print("Dish count:", dish.count())

    toggle = dish.locator("button")

    print("Toggle count:", toggle.count())

    toggle.click()

    page.wait_for_timeout(7000)  
    browser.close()
