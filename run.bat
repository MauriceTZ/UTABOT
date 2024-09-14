:: PARA OBTENER LA IP DE LA RASPBERRY, PONER "hostname -I"
:: EN LA CONSOLA DE LA RASPBERRY, RECORDAR PONER LA RASPBERRY EN EL MISMO WIFI DE LA PC,
:: LUEGO PARA EJECUTAR ESTE SCRIPT PONER "./run.bat"
SCP test.py utabot@192.168.72.177:/home/utabot
@REM SSH utabot@192.168.72.179 -t "sudo killall python3; python3 test.py"
SSH utabot@192.168.72.177 -t "python3 test.py"