
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://rms.geckoworksnepal.com.np/staff/login")

    table_input = page.get_by_placeholder("GECKO-01")
    table_input.fill("GC-01")

    expect(table_input).to_have_value("GC-01")

    page.get_by_role("button", name="Activate System").click()

    page.get_by_role("button").filter(has_text="Astha").click()

    for i in range(4):
        page.get_by_role("button", name="0").click()

    page.get_by_role("button", name="Start Shift").click()

    page.wait_for_timeout(2000)

    page.get_by_text("Reports").click()

    page.wait_for_timeout(2000)

    page.get_by_role("button", name="leave", exact=True).click()
    page.get_by_role("button", name="Apply Now", exact=True).click()
    page.get_by_role("button", name="Urgent", exact=True).click()

    page.wait_for_timeout(2000)

    date_inputs = page.locator('input[type="date"]')

    date_inputs.nth(0).fill("2026-09-20")  # FROM
    date_inputs.nth(1).fill("2026-09-22")  # TO
    page.wait_for_timeout(2000)

    page.get_by_placeholder("Why do you need leave?").fill("I need leave for personal reasons")
    page.wait_for_timeout(2000)

    page.get_by_role("button", name="Submit Request").click()
    
    page.wait_for_timeout(2000)
    
    expect(page.get_by_text("Request sent", exact=False)).to_be_visible()
    
    page.wait_for_timeout(7000)

    browser.close()
    