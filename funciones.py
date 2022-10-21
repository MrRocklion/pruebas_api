from subprocess import run
import json
comandoBaseRead="./ejecutable_comandos_api/Windows_winsock.exe "

def leerControler() :
    """ Lee todos los datos del controlador en base a la ip  """
    try:
        output = run(comandoBaseRead+"--buscar_ip .", capture_output=True, timeout=20).stdout
        
        ips_disponibles = json.loads(output)
        ip = ips_disponibles['Ips_disponibles'][0]['ip']
        mac = ips_disponibles['Ips_disponibles'][0]['mac']
        output2 = run(comandoBaseRead+str(ip)+ " --leer_hora_controlador", capture_output=True, timeout=20).stdout
        print(ip)
        tiempo = json.loads(output2)
        return [ip,mac]
    except:
        raise Exception('Error ejecutando comando leer todo')
    
