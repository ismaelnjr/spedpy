from sped.ecd.arquivos import ArquivoDigital 

f = ArquivoDigital()
f.readfile("etc\\ecd.txt")

print(f._registro_abertura.NOME)

