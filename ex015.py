km = float(input('Quanto Km você rodou com o carro: '))
dias = int(input('Quantos dias você está com o carro: '))
pagar_km = km*0.15
pagar_dias = dias*60
total_pago = pagar_km + pagar_dias
print(f'Voce rodou {km}km você deve pagar R${pagar_km} \nEstando com o carro por {dias} você deve pagar R${pagar_dias} \nContudo no geral você deve R${total_pago}')