import requests
from bs4 import BeautifulSoup
def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def scrape_data(url):
    html = get_html(url)
    if not html:
        return None
    soup = BeautifulSoup(html, 'html.parser')
    parent = soup.find('meta', attrs={'name': 'description'})
    name_container = soup.find('meta', attrs={'property': 'og:url'})
    if name_container and "content" in name_container.attrs:
        content = name_container["content"]
        name = ""
        name = content.split("posts/")[1].split("_")[0]
    # print(parent)
    if parent:
        return [name, parent.get('content', '').strip()]
    else:
        return None
if __name__ == "__main__":
    x = "https://www.linkedin.com/posts/acraider_az-azpremium-activity-7390787350559318016-vXCv"
    result = scrape_data(x)
    # print(get_html(x))
    if result:
        print(result)
    else:
        print("No data found.")
