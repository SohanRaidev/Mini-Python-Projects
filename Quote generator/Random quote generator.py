import requests
import os

api_key = os.getenv("API_KEY")

def get_random_quote(category):
    api_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    
    if response.status_code == requests.codes.ok:
        quote_data = response.json()
        if quote_data: 
            quote = quote_data[0]['quote']
            author = quote_data[0]['author']
            print(f'"{quote}" - {author}')
        else:
            print("No quotes found for this category.")
    else:
        print("Error:", response.status_code, response.text)

# Main program
if __name__ == "__main__":
    print("Welcome to the Random Quote Generator!")
    category = input("Enter a category (e.g., happiness, love, inspiration): ").strip().lower()
    
    
    get_random_quote(category)
