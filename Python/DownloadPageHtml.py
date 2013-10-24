import urllib
import time

# URL
url = 'http://pwi.com.br'
print "Baixando . . . "

# Tempo antes do inicio do download
sec = time.time()

# Iniciando Download
urllib.urlretrieve(url, "Pagina.html")

# Tempo depois do download
sec2 = time.time()

# Subtraindo os mesmos, informa os valores em minutos/segundos
print "Tempo gasto para download: %f min \n" % round( ( sec2 - sec ) / 60, 2 )
print "Tempo gasto para download: %.2f min \n" % ( ( sec2 - sec ) / 60 )
print "Tempo gasto para download: inicial: ", sec
print " - final: \n", sec2