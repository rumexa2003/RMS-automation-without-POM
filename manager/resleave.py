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
    review_request = page.get_by_text("Review Request", exact=True)

    print("Review Request:", review_request.count())

    staff_card = review_request.locator("xpath=..")

    # print("Card:", staff_card.count())

    staff_card.click()

    page.get_by_role("button", name="Approve").click()


    page.wait_for_timeout(1000)  
    browser.close()

    # # handling multiple rewiew requests
    # review_requests = page.get_by_text("Review Request", exact=True)

    # print("Review Requests:", review_requests.count())



    # review_requests = page.get_by_text("Review Request", exact=True)

    # for i in range(review_requests.count()):
    #     card = review_requests.nth(i).locator("xpath=..")

    #     print("-----")
    #     print(card.inner_text())


    # staff_name = page.get_by_role("heading", name="Astha", exact=True)

    # staff_card = staff_name.locator("xpath=../..")

    # staff_card.click()


    

