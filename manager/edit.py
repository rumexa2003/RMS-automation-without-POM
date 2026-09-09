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


    # staff_card = page.locator("div").filter(
    # has=page.get_by_role("heading", name="Staff 1", exact=True)
    # )

    # print("Staff cards found:", staff_card.count())

    # staff_card.click()

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
    page.get_by_text("Staff Hub", exact=True).click()


    page.wait_for_timeout(7000)
    browser.close()
