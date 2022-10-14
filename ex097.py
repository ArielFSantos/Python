def escreva(texto):
    print("="*(len(texto)+4))
    print(f"  {texto}")
    print("="*(len(texto)+4))


escreva(texto=str(input('Digite um Texto: ')))