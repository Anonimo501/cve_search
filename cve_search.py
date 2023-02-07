import requests
import re
from termcolor import colored
import sys

def get_cve_info(name):
    print("\n💻 CVE SEARCH v.1\n")  # Agregamos el banner
    nvd_url = f"https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&query={name}&search_type=all"
    response = requests.get(nvd_url)
    
    if response.status_code == 200:
        html_content = response.text
        cve_ids = re.findall(r'href="/vuln/detail/CVE-(.*?)"', html_content)
        if cve_ids:
            cve_ids.sort()  # Ordenamos los IDs de CVE encontrados
            print("\n🔍 IDs de CVE encontrados para", name, ":")
            for cve_id in cve_ids:
                cve_url = f"https://www.cvedetails.com/cve/CVE-{cve_id}"
                cve_response = requests.get(cve_url)
                if cve_response.status_code == 200:
                    cve_html_content = cve_response.text
                    cve_summary = re.search(r'<div class="cvedetailssummary">(.*?)</div>', cve_html_content, re.DOTALL).group(1)
                    print("\n💻 -", cve_id, ":", colored(cve_summary, "yellow"))
                    print(colored("=====================", "blue"))
                else:
                    print("\n💣 Error al hacer la solicitud GET para", cve_id, colored("[ERROR]", "red"))
        else:
            print("\n💣 No se encontraron resultados para", name, colored("[ERROR]", "red"))
    else:
        print("\n💣 Error al hacer la solicitud GET", colored("[ERROR]", "red"))

    print("\n💻 Hasta la próxima")  # Agregamos el mensaje al final de la ejecución del script

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        print("\n" 'Modo de uso: python cve_search.py <nombre del sistema operativo>')
        print('Ejemplo: python3 cve_search.py "vsFTPd 2.3.4"\n')
        sys.exit()
    elif len(sys.argv) != 2:
        print("\n" 'Modo de uso: python3 cve_search.py -h para obtener ayuda\n')
        sys.exit()

    print("Bienvenido al CVE Search v.1")
    name = sys.argv[1]
    get_cve_info(name)
