def comprobarArroba(mail):
    '''
    La funcion comprueba si el mail esta correctamente ingresado
        Tenga 1 @ correcto

    >>> comprobarArroba('mail@dominio.com')
    True
    >>> comprobarArroba('maildominio.com@')
    False
    >>> comprobarArroba('mail@@dominio.com')
    False
    >>> comprobarArroba('maildominio.com')
    False
    '''

    arroba = mail.count('@')

    if arroba!=1 or mail.rfind('@')==(len(mail)-1):
        return False
    else:
        return True
import doctest

doctest.testmod()