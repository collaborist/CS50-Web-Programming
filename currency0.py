import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=d9b2ab4bce9cfec7756e09961acf560f")    
    if res.status_code !=200:
        raise Exception("ERROR: API request unsuccessful.") 
    data = res.json()
    print(data)

if __name__ == "__main__":
    main()