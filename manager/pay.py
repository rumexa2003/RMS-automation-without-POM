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

    staff_card = page.locator("div.cursor-pointer").filter(
    has=page.get_by_role("heading", name="Astha", exact=True)
    )

    print("Astha card count:", staff_card.count())

    if staff_card.count() == 1:
        print(staff_card.inner_text())
    staff_card.click()

    page.get_by_role("button", name="payroll").click()

  


    page.wait_for_timeout(2000)  


    page.get_by_placeholder("Year").fill("2083")
    
    page.get_by_placeholder("Rs Amount").fill("2083")
    page.wait_for_timeout(2000)  
    

    page.wait_for_timeout(7000)  
    month = page.locator("select").filter(
    has=page.locator('option[value="Baisakh"]')
    )

    payment_type = page.locator("select").filter(
        has=page.locator('option[value="salary"]')
    )

    print("Month:", month.count())
    print("Payment:", payment_type.count())

    month.select_option("Bhadra")
    payment_type.select_option("Bonus")
    page.wait_for_timeout(2000)  


    page.get_by_role("button", name="Confirm Payment").click()


    browser.close()



    