def beautify(arr):
    result = ""
    for i in range(len(arr)):
        result = result+"{}\n".format(arr[i])
    return result

def arreglo_binario(numero):
    x = '00000000'
    # 8 bits
    bits = 8
    binarios = []
    binarios.append(list(x))
    for i in xrange(numero):
        x = incrementar_binario_string(x)
        if len(x) < bits:
            aux = ''
            for j in xrange(bits - len(x)):
                aux = aux + '0'
            x = aux + x
        binarios.append(list(x))
    aux = []
    for i in range(len(binarios)):
        aux.append(map(int, binarios[i]))
    binarios = aux
    return binarios

def incrementar_binario_string(s):
    return '{:04b}'.format(1 + int(s, 2))
