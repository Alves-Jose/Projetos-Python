m=float(input('Digite uma metragem:'))
cm=m*100
mm=m*1000
km=m/1000
dc=m/10
hc=m/100
dec=m*10
print('Sua medida em metros é:{:.0f} \n Sua medida em centímetros é:{:.0f} \n Sua medida em milímetros é:{:.0f} \n Sua medida em decímetros é:{:.0f} \n Sua medida em decâmetro é:{:.0f} \n Sua medida em hectômetro é:{:.0f} \n Sua medida em quilômetros é:{:.1f}'.format(m, cm, mm, dec, dc, hc, km))