
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
    page.wait_for_timeout(1000)  
    page.get_by_text("Staff Hub").click()

    page.wait_for_timeout(1000)  

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

    page.wait_for_timeout(1000)  
    browser.close()
