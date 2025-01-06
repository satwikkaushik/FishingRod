import joblib, requests, pandas
from bs4 import BeautifulSoup
from sklearn.preprocessing import StandardScaler

def extract_HTML(url):
    response = requests.get(url)

    if response.text == "":
        print("Error fetching HTML contents")
    
    return response.text

# Function to extract features
# AI generated
def extract_features(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    features = {
        # Presence checks
        "has_title": bool(soup.title),
        "has_input": bool(soup.find('input')),
        "has_button": bool(soup.find('button')),
        "has_image": bool(soup.find('img')),
        "has_submit": bool(soup.find('input', {'type': 'submit'})),
        "has_link": bool(soup.find('a')),
        "has_password": bool(soup.find('input', {'type': 'password'})),
        "has_email_input": bool(soup.find('input', {'type': 'email'})),
        "has_hidden_element": bool(soup.find(attrs={"type": "hidden"})),
        "has_audio": bool(soup.find('audio')),
        "has_video": bool(soup.find('video')),
        "has_h1": bool(soup.find('h1')),
        "has_h2": bool(soup.find('h2')),
        "has_h3": bool(soup.find('h3')),
        "has_footer": bool(soup.find('footer')),
        "has_form": bool(soup.find('form')),
        "has_text_area": bool(soup.find('textarea')),
        "has_iframe": bool(soup.find('iframe')),
        "has_text_input": bool(soup.find('input', {'type': 'text'})),
        "has_nav": bool(soup.find('nav')),
        "has_object": bool(soup.find('object')),
        "has_picture": bool(soup.find('picture')),

        # Count features
        "number_of_inputs": len(soup.find_all('input')),
        "number_of_buttons": len(soup.find_all('button')),
        "number_of_images": len(soup.find_all('img')),
        "number_of_option": len(soup.find_all('option')),
        "number_of_list": len(soup.find_all(['ul', 'ol'])),
        "number_of_th": len(soup.find_all('th')),
        "number_of_tr": len(soup.find_all('tr')),
        "number_of_href": len([tag for tag in soup.find_all('a') if tag.get('href')]),
        "number_of_paragraph": len(soup.find_all('p')),
        "number_of_script": len(soup.find_all('script')),
        "length_of_title": len(soup.title.string.strip()) if soup.title and soup.title.string else 0,
        "length_of_text": len(soup.get_text(strip=True)),
        "number_of_clickable_button": len(soup.find_all('button', {'type': 'button'})),
        "number_of_a": len(soup.find_all('a')),
        "number_of_img": len(soup.find_all('img')),
        "number_of_div": len(soup.find_all('div')),
        "number_of_figure": len(soup.find_all('figure')),
        "number_of_meta": len(soup.find_all('meta')),
        "number_of_sources": len(soup.find_all('source')),
        "number_of_span": len(soup.find_all('span')),
        "number_of_table": len(soup.find_all('table'))
    }

    return features

def preprocessing(features):
    df = pandas.DataFrame([features])
    scaler = StandardScaler()

    df_scaled = scaler.fit_transform(df)
    return df_scaled

def predict_result(df):
    model = joblib.load("./ml_model/LR_model.pkl")
    prediction = model.predict(df)
    return prediction

def format_URL(url):
    if("https://" not in url):
        url = "https://" + url

    return url

def check(url):
    url = format_URL(url)
    html = extract_HTML(url)
    features = extract_features(html)
    df = preprocessing(features)
    result = predict_result(df)

    return result