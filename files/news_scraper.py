import requests
from bs4 import BeautifulSoup


def fetch_headlines(url):
    try:
        # Send a GET request to the website
        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        # Check if request was successful
        if response.status_code == 200:

            # Parse the HTML
            soup = BeautifulSoup(response.text, "html.parser")

            # Find all h3 headings
            headlines = soup.find_all("h3")

            print("\nLatest Sky Sports Headlines\n")
            print("-" * 40)

            count = 0

            for headline in headlines:

                text = headline.get_text(strip=True)

                # Ignore empty headings
                if text:

                    print(f"{count + 1}. {text}")
                    count += 1

                    # Show only first 20 headlines
                    if count == 20:
                        break

            if count == 0:
                print("No headlines found.")

        else:
            print(f"Failed to fetch webpage. Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)


news_url = "https://www.skysports.com"

fetch_headlines(news_url)