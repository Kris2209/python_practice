import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmxlSEFpT2pFMk16QXlNalEyTnpFc0lrMXZaR1ZzSWpwN0lrTm9ZWEpoWTNSbGNuTlFaWEpFWVhraU9qVXdNREF3TENKVmMyVnlTV1FpT2pVME16a3NJbFZ1YVhGMVpVbGtJam9pTldObVpqTXhNRGN0WWpJM1l5MDBORGxqTFdJeU1qRXRaRFptTWpsalkyVmhOMlJoSW4xOS5rSFlLTE9CaWVvdjhUWnVCVHJBMEp4cm11bVZxLWpWemM5R3pkM3pWTktB'
# ключ действителен сутки

headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)
print(auth)

if auth.status_code == 200:
    token = auth.text

    while True:
        word = input('Введите слово для первода: ')
        if word:
            headers_translate = {
                'Authorization': 'Bearer ' + token
            }
            params = {'text': word,
                      'srcLang': 1033,
                      'dstLang': 1049
            }
            r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
            res = r.json()
            try:
                print(res['Translation']['Translation'])
            except:
                print('Не найдено варианта для перевода.')
else:
    print('Error!')
