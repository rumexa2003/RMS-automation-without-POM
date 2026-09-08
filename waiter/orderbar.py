# this code executes the login process for the waiter and places a new order in the system.

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://rms.geckoworksnepal.com.np/staff/login")

    table_input = page.get_by_placeholder("GECKO-01")
    table_input.fill("GC-01")

    expect(table_input).to_have_value("GC-01")

    page.get_by_role("button", name="Activate System").click()
    page.wait_for_timeout(2000)


    page.get_by_role("button").filter(has_text="Astha").click()

    for i in range(4):
        page.get_by_role("button", name="0").click()

    page.get_by_role("button", name="Start Shift").click()

    page.wait_for_timeout(5000)

    page.get_by_role("button", name="New Order").click()


    page.wait_for_timeout(2000)

    page.get_by_role("button", name="Open POS").click()
    
    page.wait_for_timeout(2000)

    page.get_by_text("Apple Iced Tea").click()
    page.wait_for_timeout(2000)

    page.get_by_role("button", name="Add to Order").click()
    page.wait_for_timeout(2000)

    # page.get_by_role("button", name="Send to Kitchen").click()
    # page.wait_for_timeout(2000)
    # # page.get_by_role("button", name="Cancel").click()
    # cancel_button = page.get_by_role("button", name="Cancel")

    # print(cancel_button.count())

    # close_icon = page.locator("svg.lucide-circle-x")
    # print(page.locator(".lucide-circle-x").count())
    # print("URL:", page.url)
    # print("X count:", page.locator(".lucide-circle-x").count())
    # print("HTML contains circle-x:",
    #   "lucide-circle-x" in page.content())

    # print(close_icon.count())

    page.wait_for_timeout(7000)

    browser.close()