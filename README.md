# cve_search

CVE search es un script desarrollado con chatGPT que nos ayudara a la hora de querer buscar un CVE ya sea de un sistema operativo o una version de algun servicio que hayamos escaneado con nmap u otra herramienta previamente, esta herramienta la he desarrollado debido a que a veces queremos encontrar el CVE de alguna version de algun servicio y se nos complica un poco, con este script solo ingresamos la version y nos mostrara los CVE relacionados con nuestra busqueda.

## Ejemplo de uso

![image](https://user-images.githubusercontent.com/67207446/217365351-2796c8fe-3c7c-497e-be37-83533843b0e9.png)

## Instalacion

git clone https://github.com/Anonimo501/cve_search.git

cd cve_search

python3 cve_search.py -h

python3 cve_search.py httpd

python3 cve_search.py "vsFTPd 2.3.4"

