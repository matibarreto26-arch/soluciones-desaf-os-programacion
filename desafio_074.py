a = [1, 2, 3, 4]
b = [10, 20]
resultado = []
for i in range(max(len(a), len(b))):  # Recorro hasta el largo de la lista mayor.
    valor_a = a[i] if i < len(a) else 0  # Si falta un elemento, uso 0.
    valor_b = b[i] if i < len(b) else 0  # Hago lo mismo con la otra lista.
    resultado.append(valor_a + valor_b)
print(resultado)
