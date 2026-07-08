from ctypes import *

libft = CDLL("./libs/libft.so")

libft.ft_strlen.argtypes = [c_char_p]
libft.ft_strlen.restype = c_int

resultado = libft.ft_strlen(b"Hello World")

print(resultado)

libft.ft_isalpha.argtypes = [c_int]
libft.ft_isalpha.restype = c_int

print(libft.ft_isalnum(ord("A")))
print(libft.ft_isalnum(ord("1")))
print(libft.ft_isalnum(ord(str(1))))
print(libft.ft_isalnum(ord(ascii(1))))

libft.ft_strdup.argtypes = [c_char_p]
libft.ft_strdup.restype = c_char_p

resultado = libft.ft_strdup(b"42 Sao Paulo")

print(resultado)
print(resultado.decode())

libft.ft_vector_create.argtypes = [c_size_t]
libft.ft_vector_create.restype = c_void_p

libft.ft_vector_push.argtypes = [
    c_void_p,
    c_void_p,
]
libft.ft_vector_push.restype = c_int

libft.ft_vector_get.argtypes = [
    c_void_p,
    c_size_t,
]
libft.ft_vector_get.restype = POINTER(c_int)

libft.ft_vector_size.argtypes = [c_void_p]
libft.ft_vector_size.restype = c_size_t

vec = libft.ft_vector_create(sizeof(c_int))

a = c_int(10)
b = c_int(20)

libft.ft_vector_push(
    vec,
    cast(pointer(a), c_void_p)
)

libft.ft_vector_push(
    vec,
    cast(pointer(b), c_void_p)
)

size = libft.ft_vector_size(vec)

for i in range(size):
    ptr = libft.ft_vector_get(vec, i)
    print(hex(ptr.contents.value))

print(hex(vec))



libformas = CDLL("./libs/libformas.so")
