from playwright.sync_api import sync_playwright

def scrape_linkedin_jobs(query: str, num_pages: int = 5):
    jobs = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for i in range(num_pages):
            url = f"https://www.linkedin.com/jobs/search/?keywords={query}&start={i*25}"
            page.goto(url)
            page.wait_for_selector(".jobs-search__results-list")
            
            job_cards = page.query_selector_all(".jobs-search__results-list > li")
            for card in job_cards:
                title = card.query_selector(".base-search-card__title").inner_text()
                company = card.query_selector(".base-search-card__subtitle").inner_text()
                location = card.query_selector(".job-search-card__location").inner_text()
                link = card.query_selector("a.base-card__full-link").get_attribute("href")
                
                jobs.append({
                    "title": title,
                    "company": company,
                    "location": location,
                    "link": link
                })
        
        browser.close()
    return jobs