import requests
from bs4 import BeautifulSoup
import random
import string


url = input("Url'yi girin: ")


def generate_random_number():
    return random.randint(1, 1000)

def generate_random_text(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Kullanıcıdan kaç kez form göndereceğini al
def get_number_of_requests():
    while True:
        try:
            num_requests = int(input("Kaç kez form göndermek istiyorsunuz? "))
            return num_requests
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser') #beautifulsoup nesnesine çevirip daha kolay kullanıyoruz
form_fields = soup.find_all("input", class_="form-control") #burayı sizin input değerlerinize göre değiştirin

#burada verileri hazırlıyoruz
def prepare_form_data():
    data = {}
    for field in form_fields:
        field_name = field.get("name")  
        field_type = field.get("type")  
        
        
        if field_name:
            if field_type == "number":
                data[field_name] = generate_random_number()
            elif field_type == "text":
                data[field_name] = generate_random_text()
            else:
                data[field_name] = generate_random_text()
    return data


submit_button = soup.find("button", class_="btn btn-default") #butonun class değerini veriyoruz
if submit_button and submit_button.get("name"):
    
    data[submit_button.get("name")] = submit_button.get("value", "")


num_requests = get_number_of_requests()


for i in range(num_requests):
    data = prepare_form_data()
    try:
        post_response = requests.post(url, data=data)
        print(f"{i+1}. Form gönderildi! Durum kodu: {post_response.status_code}") #burada i+1 yapmamızın sebebi, for döngüsünde belirttiğimiz i değerini her istekte 1 arttırmamızdır
        print(f"Gönderilen veriler: {data}")
    except Exception as e:
        print(f"Hata varr!: {e}")
