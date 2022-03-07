from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from consultaCompleta import *
w, h = A4
w = 740
h = 500


class Reporte:

    def __init__(self,a):
        self.hostname = a[0]
        self.version = a[1]
        self.comunidad = a[2]
        self.puerto = a[3]


    def CrearReporte(self):
        t = str(Consulta(self.hostname,self.version,self.comunidad,self.puerto,'1.3.6.1.2.1.1.1.0'))
        c = canvas.Canvas(f'{self.hostname}/{self.hostname}-Reporte.pdf')
        
        text = c.beginText(10,830)
        sistema = t[t.find('=')+1:]
        sistema = sistema.split(' ')
        imagen = 'Windows' if 'Windows' in sistema else 'Linux'
        t = t[t.find('=')+1:]
        c.drawImage(f'img/{imagen}.png', 500, 740, width = 100, height = 100)
        text.setFont("Times-Roman", 12)
        text.textLine(f"Descripcion:{t}")
        c.drawText(text)
        text = c.beginText(10,785)
        localizacion = str(Consulta(self.hostname,self.version,self.comunidad,self.puerto,'1.3.6.1.2.1.1.6.0'))
        localizacion = localizacion[localizacion.find('=')+1:]
        text.textLine(f'Localizacion:{localizacion}')
        c.drawText(text)
        text = c.beginText(10,770)
        n_int = str(Consulta(self.hostname,self.version,self.comunidad,self.puerto,'1.3.6.1.2.1.2.1.0'))
        n_int = n_int[n_int.find('=')+1:]
        text.textLine(f'Numero de Interfaces:{n_int}')
        c.drawText(text)
        text = c.beginText(10,755)
        tiempo = str(Consulta(self.hostname,self.version,self.comunidad,self.puerto,'1.3.6.1.2.1.1.3.0'))
        tiempo = tiempo[tiempo.find('=')+1:]
        tiempo = int(tiempo)/360000
        text.textLine(f'Tiempo de actividad desde el último reinicio: {tiempo}')
        c.drawText(text)
        text = c.beginText(10,743)
        text.textLine(f'Comunidad: {self.comunidad}')
        c.drawText(text)
        text = c.beginText(10,730)
        text.textLine(f'Direcccion IP: {self.hostname}')
        c.drawText(text)
        text = c.beginText(10,710)
        text.textLine(f'Paquetes multicast que ha recibido una interfaz ')
        c.drawText(text)
        text = c.beginText(280,710)
        text.textLine(f'Paquetes multicast que ha recibido una interfaz ')
        c.drawText(text)
        c.drawImage(f'{self.hostname}/{self.hostname} inmulticast.png', 10, 500, width = 250, height = 200)
        c.drawImage(f'{self.hostname}/{self.hostname} inip.png', 280, 500, width = 250, height = 200)
        text = c.beginText(10,470)
        text.textLine(f'Mensajes de respuesta ICMP que ha enviado el agente ')
        c.drawText(text)
        text = c.beginText(275,485)
        text.textLine(f'Segmentos enviados, incluyendo los de las conexiones actuales ')
        c.drawText(text)
        text = c.beginText(275,475)
        text.textLine(f'pero excluyendo los que contienen solamente octetos retransmitidos')
        c.drawText(text)
        c.drawImage(f'{self.hostname}/{self.hostname} icmpecho.png', 10, 260, width = 250, height = 200)
        c.drawImage(f'{self.hostname}/{self.hostname} tcpsegsent.png', 280, 260, width = 250, height = 200)
        text = c.beginText(10,240)
        text.textLine(f'Datagramas recibidos que no pudieron ser entregados por cuestiones distintas a la falta de aplicación en el puerto destino')
        c.drawText(text)
        c.drawImage(f'{self.hostname}/{self.hostname} udpin.png', 10, 25, width = 250, height = 200)
        c.save()



if(__name__=='__main__'):
    r = Reporte('localhost')
    r.CrearReporte()