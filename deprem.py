from flask import Flask
from requests import get, exceptions
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    try:
        response = get("http://www.koeri.boun.edu.tr/scripts/lst7.asp")
        response_text = response.text
        response.raise_for_status()
        soup = BeautifulSoup(response_text, "html.parser")
        preler = soup.find_all("pre")
        result = """<meta http-equiv="refresh" content="60; URL=#" />Depremler \n"""
        if response.status_code == 200:
            print("web sitesi erişime açık")
        else:
            print("web sitesine ulaşılamıyor")
    
        for i in preler:
            result += str(i) + '\n'
        return result

    except exceptions.RequestException as e:
        return "web sitesine ulaşılamıyor"

if __name__ == '__main__':
    app.run()
