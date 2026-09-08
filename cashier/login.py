# import re

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://rms.geckoworksnepal.com.np/staff/login")

    table_input = page.get_by_placeholder("GECKO-01")
    table_input.fill("GC-01")

    expect(table_input).to_have_value("GC-01")

    page.get_by_role("button", name="Activate System").click()
    page.get_by_role("button", name="Ramala").click()
    page.wait_for_timeout(1000)  

    for i in range(4):
        page.get_by_role("button", name="0").click()
    page.wait_for_timeout(1000)  

    page.get_by_role("button", name="Start Shift").click()
    page.wait_for_timeout(1000)  
    page.get_by_role("button", name="New Order").click()

    # page.get_by_role("button", name="Open POS").click()
    page.get_by_role("button", name="Open POS").click()
    page.wait_for_timeout(2000)
    # item = page.get_by_text("Iced Blended Oreo Frappe", exact=True)
    # card = item.locator("xpath=ancestor::button")

    # box = card.bounding_box()

    # print("Card box:", box)

    # page.mouse.click(
    #     box["x"] + box["width"] / 2,
    #     box["y"] + box["height"] / 2
    # )

    # print("Mouse clicked")

    # input("Check the RMS, then press Enter...")
    # item = page.get_by_text("Iced Blended Oreo Frappe", exact=True)
    # page.wait_for_timeout(2000)

    # card = item.locator("xpath=ancestor::button")

    # add_item = card.get_by_text("Add Item", exact=True)

    # print("Add Item count:", add_item.count())

    # add_item.click()

    # page.wait_for_timeout(2000)

    # print("Add Item clicked")

    # item = page.get_by_text("Iced Blended Oreo Frappe", exact=True)
    # card = item.locator("xpath=ancestor::button")

    # print("Card count:", card.count())

    # card.click()

    # page.wait_for_timeout(2000)

    # print("Clicked item")

    # item = page.get_by_text("Iced Blended Oreo Frappe", exact=True)

    # card = item.locator("xpath=ancestor::button")

    # add_item = card.get_by_text("Add Item", exact=True)

    # add_item.click()
    # item = page.get_by_text("Iced Blended Oreo Frappe", exact=True)

    # card = item.locator("xpath=ancestor::button")

    # print("Card count:", card.count())
    # print("Add Item count:", card.get_by_text("Add Item", exact=True).count())


    

    # item = page.get_by_text("Iced Blended Oreo Frappe", exact=True)

    # card = item.locator("xpath=ancestor::button")

    # card.get_by_text("Add Item", exact=True).click()

    # # page.get_by_text("Iced Blended Oreo Frappe", exact=True).click()
    # item = page.get_by_text("Iced Blended Oreo Frappe", exact=True)

    # print("Count:", item.count())
    # print(item.first.evaluate("el => el.parentElement.outerHTML"))
    # page.get_by_text("Iced Blended Oreo Frappe", exact=True).click()
    # page.get_by_text("Apple Iced Tea").click()
    # # page.get_by_text("Chinese Chop Suey (Indo-Chinese style) (Veg)").first.click()


    # buttons = page.get_by_role("button", name="Add Item", exact=False)

    # print("Count:", buttons.count())

    # for i in range(min(buttons.count(), 10)):
    #     print("-----", i, "-----")
    # print(buttons.nth(i).get_attribute("class"))
    # print(buttons.nth(i).inner_text())

    # page.get_by_role(
    # "button",
    # name=re.compile("Send .* to kitchen", re.IGNORECASE)
    # ).click()
    # page.get_by_role("button", name="Send to Kitchen").click()


    # page.wait_for_timeout(7000) 

    # expect(page).to_have_url("https://rms.geckoworksnepal.com.np/staff/cashier")


    browser.close()
