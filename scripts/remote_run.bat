:: PARA OBTENER LA IP DE LA RASPBERRY, PONER "hostname -I"
:: EN LA CONSOLA DE LA RASPBERRY, RECORDAR PONER LA RASPBERRY EN EL MISMO WIFI DE LA PC,
:: LUEGO PARA EJECUTAR ESTE SCRIPT PONER "./run.bat"

set "RPI_ADDRESS=192.168.1.177"

SCP test.py utabot@%RPI_ADDRESS%:/home/utabot
:: REM SSH utabot@%RPI_ADDRESS% -t "sudo killall python3; python3 test.py"
SSH utabot@%RPI_ADDRESS% -t "sudo python3 test.py"