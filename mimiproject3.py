import urllib.request
import json

print("project AI AGENTIC TOOL CREATION")
print("stock market,nifty,sensux,goldrate,rupee value,... prediction ai")
print("BULLIONIQ")
print("groceries price detection ai")
print("BAZARSCAN")

# This will be your entry point
def main():
    print("Welcome to your EA agentic tool!")

if __name__ == "__main__":
    main()
def fetch_trending_topics():
    # Fetch trending topics from a real public API
    url = "https://api.coingecko.com/api/v3/search/trending"
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                coins = data.get("coins", [])
                return [coin["item"]["name"] for coin in coins if coin.get("item")]
            print(f"Unexpected response status: {response.status}")
    except Exception as error:
        print(f"Error fetching trending topics: {error}")

    return ["Unable to fetch trending topics at this time."]

# Example usage
trending_data = fetch_trending_topics()
print(trending_data)
print('function executed successfully')



