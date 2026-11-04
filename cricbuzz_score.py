
from playwright.sync_api import sync_playwright, TimeoutError

SCORE_SELECTOR = "span.font-medium.text-cbTxtPrim"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    try:
        print("Opening Cricbuzz...")

        page.goto(
            "https://www.cricbuzz.com/",
            wait_until="domcontentloaded"
        )

        print("Waiting for cricket scores...")

        page.wait_for_selector(
            SCORE_SELECTOR,
            state="visible",
            timeout=20000
        )

        scores = page.locator(SCORE_SELECTOR).all_inner_texts()

        scores = [score.strip() for score in scores if score.strip()]

        if scores:
            print("\nLatest cricket score:")
            print(scores[0])

            page.screenshot(path="score.png")
            print("\nScreenshot saved as score.png")

        else:
            print("No live cricket score available.")

    except TimeoutError:
        print("No cricket score found. Please try again.")

    finally:
        browser.close()
