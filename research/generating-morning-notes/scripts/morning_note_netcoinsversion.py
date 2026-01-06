import requests
import pandas as pd
import logging
from datetime import datetime

# Configure logging to be extremely clear
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'morning_note_netcoins_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)

# Space for you to input assets to be excluded from the FRNT Crypto Index
EXCLUDED_ASSETS = ["usds", 
                   "pi-network", 
                   "tether", 
                   "usd-coin", 
                   "staked-ether", 
                   "dai", 
                   "ton", 
                   "internet-computer", 
                   "wrapped-steth", 
                   "weth", 
                   "ethena",
                   "wrapped-bitcoin",
                   "wrapped-beacon-eth",
                   "wrapped-eeth",
                   "ethena-usde",
                   "weeth",
                   "binance-bridged-usdt-bnb-smart-chain",
                   ]

# HARDCODED NETCOINS ASSETS WITH COINGECKO IDs
# This list can be manually updated when assets are added/removed from Netcoins
NETCOINS_ASSETS = [
    {"name": "1inch Network", "symbol": "1INCH", "coingecko_id": "1inch"},
    {"name": "Aave", "symbol": "AAVE", "coingecko_id": "aave"},
    {"name": "Algorand", "symbol": "ALGO", "coingecko_id": "algorand"},
    {"name": "Apecoin", "symbol": "APE", "coingecko_id": "apecoin"},
    {"name": "Arbitrum", "symbol": "ARB", "coingecko_id": "arbitrum"},
    {"name": "Avalanche", "symbol": "AVAX", "coingecko_id": "avalanche-2"},
    {"name": "Axie Infinity", "symbol": "AXS", "coingecko_id": "axie-infinity"},
    {"name": "BONK", "symbol": "BONK", "coingecko_id": "bonk"},
    {"name": "Basic Attention Token", "symbol": "BAT", "coingecko_id": "basic-attention-token"},
    {"name": "Bitcoin", "symbol": "BTC", "coingecko_id": "bitcoin"},
    {"name": "Bitcoin Cash", "symbol": "BCH", "coingecko_id": "bitcoin-cash"},
    {"name": "Bittensor", "symbol": "TAO", "coingecko_id": "bittensor"},
    {"name": "Cardano", "symbol": "ADA", "coingecko_id": "cardano"},
    {"name": "Celestia", "symbol": "TIA", "coingecko_id": "celestia"},
    {"name": "Chainlink", "symbol": "LINK", "coingecko_id": "chainlink"},
    {"name": "Chiliz", "symbol": "CHZ", "coingecko_id": "chiliz"},
    {"name": "Cosmos", "symbol": "ATOM", "coingecko_id": "cosmos"},
    {"name": "Curve DAO", "symbol": "CRV", "coingecko_id": "curve-dao-token"},
    {"name": "DYDX", "symbol": "DYDX", "coingecko_id": "dydx"},
    {"name": "Decentraland", "symbol": "MANA", "coingecko_id": "decentraland"},
    {"name": "Dogecoin", "symbol": "DOGE", "coingecko_id": "dogecoin"},
    {"name": "Dogwifhat", "symbol": "WIF", "coingecko_id": "dogwifhat"},
    {"name": "Ethena", "symbol": "ENA", "coingecko_id": "ethena"},
    {"name": "Ethereum", "symbol": "ETH", "coingecko_id": "ethereum"},
    {"name": "Fartcoin", "symbol": "FARTCOIN", "coingecko_id": "fartcoin"},
    {"name": "Fetch.AI", "symbol": "FET", "coingecko_id": "fetch-ai"},
    {"name": "Floki", "symbol": "FLOKI", "coingecko_id": "floki"},
    {"name": "GOAT", "symbol": "GOAT", "coingecko_id": "goat"},
    {"name": "Gala Games", "symbol": "GALA", "coingecko_id": "gala"},
    {"name": "Hedera", "symbol": "HBAR", "coingecko_id": "hedera-hashgraph"},
    {"name": "Hyperliquid", "symbol": "HYPE", "coingecko_id": "hyperliquid"},
    {"name": "Injective", "symbol": "INJ", "coingecko_id": "injective"},
    {"name": "Jupiter", "symbol": "JUP", "coingecko_id": "jupiter"},
    {"name": "Litecoin", "symbol": "LTC", "coingecko_id": "litecoin"},
    {"name": "Loopring", "symbol": "LRC", "coingecko_id": "loopring"},
    {"name": "Maker", "symbol": "MKR", "coingecko_id": "maker"},
    {"name": "Mog Coin", "symbol": "MOG", "coingecko_id": "mog-coin"},
    {"name": "Near", "symbol": "NEAR", "coingecko_id": "near"},
    {"name": "Ondo", "symbol": "ONDO", "coingecko_id": "ondo"},
    {"name": "Pepe", "symbol": "PEPE", "coingecko_id": "pepe"},
    {"name": "Polkadot", "symbol": "DOT", "coingecko_id": "polkadot"},
    {"name": "Polygon", "symbol": "POL", "coingecko_id": "matic-network"},
    {"name": "Popcat", "symbol": "POPCAT", "coingecko_id": "popcat"},
    {"name": "Pudgy Penguins", "symbol": "PENGU", "coingecko_id": "penguins"},
    {"name": "Pump.fun", "symbol": "PUMP", "coingecko_id": "pump"},
    {"name": "Quant", "symbol": "QNT", "coingecko_id": "quant-network"},
    {"name": "Render", "symbol": "RENDER", "coingecko_id": "render-token"},
    {"name": "Shiba Inu", "symbol": "SHIB", "coingecko_id": "shiba-inu"},
    {"name": "Solana", "symbol": "SOL", "coingecko_id": "solana"},
    {"name": "Sonic", "symbol": "S", "coingecko_id": "sonic"},
    {"name": "Stellar", "symbol": "XLM", "coingecko_id": "stellar"},
    {"name": "Sui", "symbol": "SUI", "coingecko_id": "sui"},
    {"name": "SushiSwap", "symbol": "SUSHI", "coingecko_id": "sushi"},
    {"name": "Tezos", "symbol": "XTZ", "coingecko_id": "tezos"},
    {"name": "The Graph", "symbol": "GRT", "coingecko_id": "the-graph"},
    {"name": "The Sandbox", "symbol": "SAND", "coingecko_id": "the-sandbox"},
    {"name": "Trump", "symbol": "TRUMP", "coingecko_id": "trump"},
    {"name": "USDC", "symbol": "USDC", "coingecko_id": "usd-coin"},
    {"name": "Uniswap", "symbol": "UNI", "coingecko_id": "uniswap"},
    {"name": "Virtuals Protocol", "symbol": "VIRTUAL", "coingecko_id": "virtuals"},
    {"name": "Worldcoin", "symbol": "WLD", "coingecko_id": "worldcoin"},
    {"name": "XRP", "symbol": "XRP", "coingecko_id": "ripple"},
    {"name": "Yearn Finance", "symbol": "YFI", "coingecko_id": "yearn-finance"}
]

def load_netcoins_cryptocurrencies():
    """
    Load hardcoded Netcoins assets instead of reading from CSV.
    This makes it easy to manually add/remove assets when needed.
    """
    logging.info(f"Loaded {len(NETCOINS_ASSETS)} hardcoded Netcoins assets")
    return NETCOINS_ASSETS

def fetch_crypto_data():
    """
    Fetch cryptocurrency data from CoinGecko API using API key for higher limits.
    Returns data for all cryptocurrencies that can be matched with Netcoins list.
    """
    api_key = "CG-AoXY9Ky5oZ2rLDPWRWGgPJQc"
    url = "https://pro-api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 1000,  # Much higher limit with API key
        'page': 1,
        'sparkline': 'false',
        'locale': 'en'
    }
    
    headers = {'x-cg-pro-api-key': api_key}
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        crypto_data = response.json()
        logging.info(f"Successfully fetched {len(crypto_data)} cryptocurrencies from CoinGecko API (with API key)")
        
        # If we still don't have enough, try to get more pages
        if len(crypto_data) < 1000:
            logging.info("Fetching additional pages to get more cryptocurrencies...")
            page = 2
            while len(crypto_data) < 3000 and page <= 15:  # Increased to 15 pages to get more coins including Maker
                params['page'] = page
                response = requests.get(url, params=params, headers=headers)
                if response.status_code == 200:
                    page_data = response.json()
                    if page_data:
                        crypto_data.extend(page_data)
                        logging.info(f"Added page {page}: {len(page_data)} more cryptocurrencies")
                        page += 1
                    else:
                        break
                else:
                    break
        
        logging.info(f"Final total: {len(crypto_data)} cryptocurrencies fetched")
        return crypto_data
    except requests.RequestException as e:
        logging.error(f"Error fetching data from CoinGecko API: {e}")
        return []

def fetch_maker_data():
    """
    Fetch Maker (MKR) data specifically from CoinGecko coin ID endpoint.
    Returns Maker asset data if available, None otherwise.
    """
    api_key = "CG-AoXY9Ky5oZ2rLDPWRWGgPJQc"
    url = "https://pro-api.coingecko.com/api/v3/coins/maker"
    headers = {'x-cg-pro-api-key': api_key}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            
            # Check if we have the necessary data
            if 'market_data' in data and data['market_data'].get('price_change_percentage_24h') is not None:
                # Create a compatible asset structure
                maker_asset = {
                    'id': 'maker',
                    'name': 'Maker',
                    'symbol': 'mkr',
                    'price_change_percentage_24h': data['market_data']['price_change_percentage_24h'],
                    'current_price': data['market_data'].get('current_price', {}).get('usd', 0),
                    'market_cap': data['market_data'].get('market_cap', {}).get('usd', 0),
                    'market_cap_rank': data['market_data'].get('market_cap_rank'),
                    'source': 'direct_api_call'
                }
                logging.info(f"Successfully fetched Maker (MKR) data: {maker_asset['price_change_percentage_24h']:.2f}% 24h change")
                return maker_asset
            else:
                logging.warning("Maker data available but missing 24h change percentage")
                return None
        else:
            logging.warning(f"Failed to fetch Maker data: HTTP {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Error fetching Maker data: {e}")
        return None

def match_netcoins_with_coingecko(netcoins_assets, crypto_data):
    """
    Match hardcoded Netcoins assets with CoinGecko data using their CoinGecko IDs.
    Returns a list of matched assets with their data.
    """
    matched_assets = []
    matched_details = []
    unmatched_netcoins = []
    
    # Create a lookup dictionary for CoinGecko data by ID
    coingecko_lookup = {asset['id']: asset for asset in crypto_data}
    
    # Match each Netcoins asset by its CoinGecko ID
    for netcoins_asset in netcoins_assets:
        coingecko_id = netcoins_asset['coingecko_id']
        if coingecko_id in coingecko_lookup:
            # Merge Netcoins asset info with CoinGecko data
            matched_asset = coingecko_lookup[coingecko_id].copy()
            matched_asset['netcoins_name'] = netcoins_asset['name']
            matched_asset['netcoins_symbol'] = netcoins_asset['symbol']
            matched_assets.append(matched_asset)
            matched_details.append(f"{netcoins_asset['name']} ({netcoins_asset['symbol']})")
            logging.info(f"Matched {netcoins_asset['name']} ({netcoins_asset['symbol']}) by CoinGecko ID: {coingecko_id}")
        else:
            unmatched_netcoins.append(netcoins_asset)
            logging.warning(f"Could not find {netcoins_asset['name']} ({netcoins_asset['symbol']}) with CoinGecko ID: {coingecko_id}")
    
    # Special handling for Maker (MKR) - fetch directly if not matched
    maker_asset = next((asset for asset in netcoins_assets if asset['symbol'] == 'MKR'), None)
    if maker_asset and maker_asset not in [a.get('netcoins_symbol') for a in matched_assets]:
        logging.info("Attempting to fetch Maker (MKR) data directly...")
        maker_data = fetch_maker_data()
        if maker_data:
            maker_data['netcoins_name'] = maker_asset['name']
            maker_data['netcoins_symbol'] = maker_asset['symbol']
            matched_assets.append(maker_data)
            matched_details.append(f"{maker_asset['name']} ({maker_asset['symbol']})")
            logging.info("Maker (MKR) successfully added using direct API call")
        else:
            logging.warning("Maker (MKR) could not be fetched directly")
    
    logging.info(f"Successfully matched {len(matched_assets)} out of {len(netcoins_assets)} Netcoins assets")
    logging.info(f"Matched assets: {', '.join(matched_details)}")
    
    if unmatched_netcoins:
        unmatched_list = [f"{a['name']} ({a['symbol']})" for a in unmatched_netcoins]
        logging.warning(f"Unmatched Netcoins assets: {', '.join(unmatched_list)}")
    
    return matched_assets

def calculate_frnt_index(crypto_data, netcoins_assets):
    """
    Calculate FRNT index (same as original morning note.py) and find top performer/underperformer from Netcoins assets.
    """
    market_caps = []
    price_changes = []
    top_performer = None
    top_underperformer = None
    
    # FRNT INDEX CALCULATION - EXACTLY AS IN ORIGINAL morning note.py
    # Filter the top 20, excluding the assets you specified
    logging.info(f"Total assets fetched: {len(crypto_data)}")
    logging.info(f"Assets to exclude: {EXCLUDED_ASSETS}")
    
    # Check which assets are being excluded
    excluded_found = [asset for asset in crypto_data if asset['id'] in EXCLUDED_ASSETS]
    if excluded_found:
        logging.info(f"Found {len(excluded_found)} assets that should be excluded:")
        for asset in excluded_found:
            logging.info(f"  • {asset['name']} ({asset['id']}) - Market Cap: ${asset['market_cap']:,.0f}")
    
    top_20 = [asset for asset in crypto_data if asset['id'] not in EXCLUDED_ASSETS][:20]
    
    logging.info(f"FRNT Index calculation: Using top 20 assets by market cap (same as original morning note.py)")
    logging.info("Assets used in FRNT Index calculation:")
    for i, asset in enumerate(top_20, 1):
        logging.info(f"  • {asset['name']} ({asset['symbol'].upper()}) - Market Cap: ${asset['market_cap']:,.0f}")
    
    for asset in top_20:
        # Skip assets with missing price change data
        if asset['price_change_percentage_24h'] is None:
            logging.warning(f"Skipping {asset['name']} in FRNT calculation - no 24h price change data")
            continue
        # Calculate the weighted price change
        market_caps.append(asset['market_cap'])
        price_changes.append(asset['price_change_percentage_24h'] * asset['market_cap'])
    
    total_market_cap = sum(market_caps)
    weighted_price_change = sum(price_changes) / total_market_cap if total_market_cap else 0
    
    # TOP PERFORMER AND UNDERPERFORMER - FROM NETCOINS ASSETS ONLY
    logging.info(f"Top performer/underperformer calculation: Using {len(netcoins_assets)} Netcoins assets")
    
    # Filter Netcoins assets to exclude the same assets and those with missing price data
    filtered_netcoins = [
        asset for asset in netcoins_assets 
        if asset['id'] not in EXCLUDED_ASSETS and asset.get('price_change_percentage_24h') is not None
    ]
    
    if filtered_netcoins:
        logging.info("Netcoins assets considered for top performer/underperformer:")
        for asset in filtered_netcoins:
            # Use Netcoins name if available, otherwise fall back to CoinGecko name
            display_name = asset.get('netcoins_name', asset['name'])
            display_symbol = asset.get('netcoins_symbol', asset['symbol']).upper()
            logging.info(f"  • {display_name} ({display_symbol}) - {asset['price_change_percentage_24h']:+.2f}%")
        
        # Find top performer and underperformer from Netcoins assets only
        for asset in filtered_netcoins:
            # Determine top performer and underperformer
            if top_performer is None or asset['price_change_percentage_24h'] > top_performer['price_change_percentage_24h']:
                top_performer = asset
            
            if top_underperformer is None or asset['price_change_percentage_24h'] < top_underperformer['price_change_percentage_24h']:
                top_underperformer = asset
        
        # Use Netcoins names for display
        top_performer_name = top_performer.get('netcoins_name', top_performer['name'])
        top_performer_symbol = top_performer.get('netcoins_symbol', top_performer['symbol']).upper()
        top_underperformer_name = top_underperformer.get('netcoins_name', top_underperformer['name'])
        top_underperformer_symbol = top_underperformer.get('netcoins_symbol', top_underperformer['symbol']).upper()
        
        logging.info(f"Top performer from Netcoins: {top_performer_name} ({top_performer_symbol}) - {top_performer['price_change_percentage_24h']:.2f}%")
        logging.info(f"Top underperformer from Netcoins: {top_underperformer_name} ({top_underperformer_symbol}) - {top_underperformer['price_change_percentage_24h']:.2f}%")
    
    return weighted_price_change, top_performer, top_underperformer

def main():
    """
    Main function to run the Netcoins version of the morning note analysis.
    """
    logging.info("=" * 80)
    logging.info("STARTING MORNING NOTE NETCOINS VERSION ANALYSIS")
    logging.info("=" * 80)
    
    # Load hardcoded Netcoins assets
    netcoins_assets = load_netcoins_cryptocurrencies()
    if not netcoins_assets:
        logging.error("Failed to load Netcoins assets. Exiting.")
        return
    
    # Fetch CoinGecko data
    crypto_data = fetch_crypto_data()
    if not crypto_data:
        logging.error("Failed to fetch CoinGecko data. Exiting.")
        return
    
    # Match Netcoins with CoinGecko data
    matched_netcoins_assets = match_netcoins_with_coingecko(netcoins_assets, crypto_data)
    if not matched_netcoins_assets:
        logging.error("No matching assets found between Netcoins and CoinGecko. Exiting.")
        return
    
    # Calculate FRNT index and find top performers
    frnt_index, top_performer, top_underperformer = calculate_frnt_index(crypto_data, matched_netcoins_assets)
    
    # Log results
    logging.info("=" * 80)
    logging.info("ANALYSIS RESULTS")
    logging.info("=" * 80)
    logging.info(f"FRNT Crypto Index value: {frnt_index:.2f}%")
    
    if top_performer:
        top_performer_name = top_performer.get('netcoins_name', top_performer['name'])
        top_performer_symbol = top_performer.get('netcoins_symbol', top_performer['symbol']).upper()
        logging.info(f"TOP PERFORMER: {top_performer_name} ({top_performer_symbol}) - {top_performer['price_change_percentage_24h']:.2f}%")
        logging.info(f"  Market Cap: ${top_performer['market_cap']:,.0f}")
        logging.info(f"  Current Price: ${top_performer['current_price']:.4f}")
    
    if top_underperformer:
        top_underperformer_name = top_underperformer.get('netcoins_name', top_underperformer['name'])
        top_underperformer_symbol = top_underperformer.get('netcoins_symbol', top_underperformer['symbol']).upper()
        logging.info(f"TOP UNDERPERFORMER: {top_underperformer_name} ({top_underperformer_symbol}) - {top_underperformer['price_change_percentage_24h']:.2f}%")
        logging.info(f"  Market Cap: ${top_underperformer['market_cap']:,.0f}")
        logging.info(f"  Current Price: ${top_underperformer['current_price']:.4f}")
    
    logging.info("=" * 80)
    logging.info("ANALYSIS COMPLETE")
    logging.info("=" * 80)
    
    # Also print to console for immediate viewing
    print("\n" + "=" * 60)
    print("MORNING NOTE NETCOINS VERSION - RESULTS")
    print("=" * 60)
    print(f"FRNT Crypto Index value: {frnt_index:.2f}%")
    print()
    
    if top_performer:
        print("TOP PERFORMER:")
        top_performer_name = top_performer.get('netcoins_name', top_performer['name'])
        top_performer_symbol = top_performer.get('netcoins_symbol', top_performer['symbol']).upper()
        print(f"  • {top_performer_name} ({top_performer_symbol}) - {top_performer['price_change_percentage_24h']:+.2f}%")
        print(f"    Market Cap: ${top_performer['market_cap']:,.0f}")
        print(f"    Current Price: ${top_performer['current_price']:.4f}")
        print()
    
    if top_underperformer:
        print("TOP UNDERPERFORMER:")
        top_underperformer_name = top_underperformer.get('netcoins_name', top_underperformer['name'])
        top_underperformer_symbol = top_underperformer.get('netcoins_symbol', top_underperformer['symbol']).upper()
        print(f"  • {top_underperformer_name} ({top_underperformer_symbol}) - {top_underperformer['price_change_percentage_24h']:+.2f}%")
        print(f"    Market Cap: ${top_underperformer['market_cap']:,.0f}")
        print(f"    Current Price: ${top_underperformer['current_price']:.4f}")
        print()
    
    print("=" * 60)
    print("Check the log file for detailed asset breakdowns")
    print("=" * 60)

if __name__ == "__main__":
    main() 