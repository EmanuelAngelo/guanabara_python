larg = float(input('largura da parede: '))
alt = float(input('Altura da parede: '))
area =  larg * alt
print('Sua parede tem dimensao de {}x{}M e sua area é de {}m² '.format(larg, alt, area))
tinta = area / 2
print('Para pintar sua parede, voce precisa de {}L de tintas.'.format(tinta))