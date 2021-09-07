import network,time,machine,sys

print('toimii8')

try:
  import usocket as socket
except:
  import socket

Ledi = machine.Pin(1, machine.Pin.OUT)
Ledi.value(0)

adc = machine.ADC(0)

def kor(x):
    return round(23.*(x-608)/(788-608),2)

def web_page():
  menu="""
    <h1>TEMPERATURE</h1>
    <p><h1>"""+str(kor(adc.read()))+"""</h1> <p>
    <p><h1>"""+str(adc.read())+"""</h1> <p>
<p>  
<p>  
    <p> LED <a href="/led/on"> <button class="button">ON</button></a>
     <a href="/led/off"> <button class="button button2">OFF</button></a> </p>
    """
  html = """
     <html><head>
     <meta http-equiv="refresh" content="3"> 
     <title>LAMPOTILA</title>
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <link rel="icon" href="data:,">
     <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style>
     </head>
      <body>
     """ + menu + """
     </body>
   </html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    try:
        conn, addr = s.accept()
        request = conn.recv(1024)
        request = str(request)
        if request.find('/led/on') == 6:
            Ledi.value(0)
        if request.find('/led/off') == 6:
            Ledi.value(1)
        if request.find('/exit') == 6:
            machine.reset()
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError:
        pass
