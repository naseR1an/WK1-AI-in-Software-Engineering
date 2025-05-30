
# Dataset of cryptocurrencies 
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}  

print("👋Hey there! I'm CryptocashGuide- your friendly and eco-conscious cypto buddy! 🚀🤑")
print("Ask me things like:\n- Which crypto is trending up?\n- Which crypto is sustainable?\n- Which crypto has long-term growth potential📈?\n-(Type 'exit' to quit)\n")


# Decision Logic for crypto advice
# Rule based Response Function
def get_response(user_input):
    user_input = user_input.lower()

    if "trending" in user_input or "rising" in user_input:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        return f" These cryptos are trending up: {', '.join(trending)} 🚀"
    elif "sustainable" in user_input or "eco" in user_input:
        best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        score = crypto_db[best]["sustainability_score"] * 10
        return f"Invest in {best}! 🌱 It’s eco-friendly with a sustainability score of {score}/10 and has long-term potential!"
    elif "long-term" in user_input or "profit" in user_input or "growth" in user_input:
        best = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["market_cap"] == "high"]
        if best:
            return f" 💰For long-term gains, go with {best[0]} - it has a higher market cap and rising trend: {', '.join(best)} 📈"
        else:
            return "No long-term growth options found😔.Nothing looks promising for long-term gains right now. Try asking about other trends! 📊"
    elif "help" in user_input or "advice" in user_input:
        return "I'm here to help! Ask me about crypto trends, sustainability, or long-term growth potential! 💬"
    else:
        return "🤔 I'm not sure about that. Can you ask about trends, sustainability, or long-term growth? Or type 'help' for more options!"

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("CryptoCashGuide: Always ready to help😇. Trade responsibly!")
        break
    response = get_response(user_input)
    print(f"CryptoCashGuide: {response}")
print("\n⚠️ Disclaimer: Cryptocurrency is risky. This bot is for educational use only. Always do your own research before investing! ⚠️")