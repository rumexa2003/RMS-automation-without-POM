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
    
    reports_icon = page.locator("svg.lucide-file-chart-column-increasing")

    # print(reports_icon.count())

    reports_icon.click()
    page.get_by_role("button", name="Leave Status").click()
    # expect(page).to_have_url("https://rms.geckoworksnepal.com.np/staff/bartender/reports")
    page.get_by_role("button", name="Apply Now", exact=True).click()
    page.get_by_role("button", name="Urgent", exact=True).click()
        
    page.wait_for_timeout(2000)
        
    date_inputs = page.locator('input[type="date"]')
        
    date_inputs.nth(0).fill("2026-09-21")  # FROM
    date_inputs.nth(1).fill("2026-09-29")  # TO
    page.wait_for_timeout(2000)
        
    page.get_by_placeholder("Why do you need leave?").fill("I need leave for personal reasons")
    page.wait_for_timeout(2000)
        
    page.get_by_role("button", name="Submit Request").click()
    page.wait_for_timeout(2000)
        
        # Check if "Request sent" notification appears
    try:
        success_notification = page.get_by_text("Request sent")
        success_notification.wait_for(timeout=5000)
        print(" Success! 'Request sent' notification appeared - Form submitted successfully")
    except:
        print(" Form NOT submitted - 'Request sent' notification not found")
    
    page.wait_for_timeout(3000)
    page.wait_for_timeout(7000)

    browser.close()
