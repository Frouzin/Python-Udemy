velocidadeCarro = 61
local_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1
vel_carro_passar_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidadeCarro > RADAR_1:
    print('Velocidade carro passou do radar 1')
if vel_carro_passar_radar and velocidadeCarro > RADAR_1:
    print('Carro multado')
