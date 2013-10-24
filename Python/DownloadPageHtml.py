import urllib
import time

# URL
#url = 'http://www.carlissongaldino.com.br/modules/pubdlcnt/pubdlcnt.php?file=http://www.carlissongaldino.com.br/sites/default/files/o-fantasma-da-opera.pdf&nid=1287'

url = 'http://pwi.com.br'
print "baixando . . . "

# Tempo antes do inicio do download
sec = time.time()

# Iniciando Download
urllib.urlretrieve(url, "teste.html")

# Tempo depois do download
sec2 = time.time()

# Subtraindo os mesmos, informa os valores em minutos/segundos
print "Tempo gasto para download: %f min \n" % round( ( sec2 - sec ) / 60, 2 )
print "Tempo gasto para download: %.2f min \n" % ( ( sec2 - sec ) / 60 )
print "Tempo gasto para download: inicial: ", sec
print " - final: \n", sec2