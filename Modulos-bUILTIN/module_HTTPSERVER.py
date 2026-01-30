# O módulo http.server (atenção: HTTP, não hhtp) é um módulo padrão do Python para criar servidores HTTP simples, muito usado em testes, labs e pentest.


from http.server import HTTPServer, SimpleHTTPRequestHandler

server = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)

print("SERVIDOR RODANDO NA PORTA 8000")
server.serve_forever()
