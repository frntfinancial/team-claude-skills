import requests

# Space for you to input assets to be excluded from the FRNT Crypto Index
EXCLUDED_ASSETS = ["usds", "pi-network", "tether", "usd-coin", "staked-ether", "wrapped-bitcoin", "dai", "ton", "internet-computer", "wrapped-steth", "weth", "ethena", "wrapped-beacon-eth", "wrapped-eeth", "ethena-usde", "weeth", "binance-bridged-usdt-bnb-smart-chain","figure-heloc","mantle","usdt0","ethena-usde","whitebit"]

def fetch_crypto_data():
    """
    Fetch cryptocurrency data from CoinGecko API using API key for higher limits.
    """
    api_key = "CG-AoXY9Ky5oZ2rLDPWRWGgPJQc"
    url = "https://pro-api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 100,  # Higher limit with API key
        'page': 1,
        'sparkline': 'false',
        'locale': 'en'
    }
    
    headers = {'x-cg-pro-api-key': api_key}
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        crypto_data = response.json()
        print(f"Successfully fetched {len(crypto_data)} cryptocurrencies from CoinGecko API")
        return crypto_data
    except requests.RequestException as e:
        print(f"Error fetching data from CoinGecko API: {e}")
        return []

def calculate_frnt_index(crypto_data):
    market_caps = []
    price_changes = []
    top_performer = None
    top_performer_change = float('-inf')
    top_underperformer = None
    top_underperformer_change = float('inf')

    # Filter the top 20, excluding the assets you specified
    top_20 = [asset for asset in crypto_data if asset['id'] not in EXCLUDED_ASSETS][:20]
    
    print(f"FRNT Index calculation: Using top 20 assets by market cap")
    print("Assets used in FRNT Index calculation:")
    for i, asset in enumerate(top_20, 1):
        print(f"  • {asset['name']} ({asset['symbol'].upper()}) - Market Cap: ${asset['market_cap']:,.0f}")

    for asset in top_20:
        # Handle None values by treating them as 0% change
        price_change = asset['price_change_percentage_24h'] or 0.0

        # Calculate the weighted price change
        market_caps.append(asset['market_cap'])
        price_changes.append(price_change * asset['market_cap'])

        # Determine top performer and underperformer
        if price_change > top_performer_change:
            top_performer = asset
            top_performer_change = price_change

        if price_change < top_underperformer_change:
            top_underperformer = asset
            top_underperformer_change = price_change

    total_market_cap = sum(market_caps)
    weighted_price_change = sum(price_changes) / total_market_cap if total_market_cap else 0

    return weighted_price_change, top_performer, top_underperformer, top_performer_change, top_underperformer_change

def main():
    crypto_data = fetch_crypto_data()
    frnt_index, top_performer, top_underperformer, top_performer_change, top_underperformer_change = calculate_frnt_index(crypto_data)

    print(f"FRNT Crypto Index value: {frnt_index:.2f}%")

    if top_performer:
        print(f"Top performer: {top_performer['name']} ({top_performer_change:.2f}%)")

    if top_underperformer:
        print(f"Top underperformer: {top_underperformer['name']} ({top_underperformer_change:.2f}%)")

if __name__ == "__main__":
    main()