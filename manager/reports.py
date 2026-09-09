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
    page.wait_for_timeout(7000)  

    reports_link = page.get_by_role("link", name="Reports", exact=True)

    # print(reports_link.count())
    reports_link.click()
    
 
    page.get_by_role("button", name="Credit Ledger").click()
    page.wait_for_timeout(5000)  

    close_button = page.get_by_role("button").filter(
    has=page.locator("svg.lucide-x")
    )
    # print("Close buttons:", close_button.count())
    close_button.click()
    page.wait_for_timeout(10000)  

    date_dropdown = page.locator("button").filter(
    has=page.locator("svg.lucide-calendar")
    )

    # print("Date dropdown:", date_dropdown.count())
    date_dropdown.click()
    page.wait_for_timeout(5000) 
    page.wait_for_timeout(1000)

    days_30 = page.get_by_role(
        "button",
        name="30 Days",
        exact=True
    )
    days_30.click()
    page.wait_for_timeout(5000)
    browser.close()
