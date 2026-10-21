facebook = {"Ana", "Luis", "Sol"}
instagram = {"Luis", "Sol", "Eva"}
x = {"Sol", "Bruno"}
todos = facebook.intersection(instagram, x)
solo_facebook = facebook.difference(instagram.union(x))
solo_instagram = instagram.difference(facebook.union(x))
solo_x = x.difference(facebook.union(instagram))
solo_una = solo_facebook.union(solo_instagram, solo_x)  # Reúno a quienes usan una sola plataforma.
facebook_instagram = facebook.intersection(instagram)
facebook_x = facebook.intersection(x)
instagram_x = instagram.intersection(x)
al_menos_dos = facebook_instagram.union(facebook_x, instagram_x)  # Uno las coincidencias de cada pareja de plataformas.
print("Las tres:", todos)
print("Solo una:", solo_una)
print("Al menos dos:", al_menos_dos)
