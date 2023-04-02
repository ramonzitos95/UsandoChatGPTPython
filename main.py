from senha import API_KEY
import requests
import json

print(API_KEY)

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
#https://api.openai.com/v1/models
id_modelo = "gpt-3.5-turbo"

body_mensagem = {
    "model": id_modelo,
    "messages": [{"role": "user", "content": "escreva uma apresentação para uma reunião sobre as demandas da semana"}]
}

body_mensagem = json.dumps(body_mensagem)
print(body_mensagem)

requisicao = requests.post(link, headers=headers, data=body_mensagem)
print(requisicao)
resposta = requisicao.json()

if(resposta["error"]["type"] == "insufficient_quota"):
    print("A quantidade de requisições para a api foi excedida")
else:
    mensagem = resposta["choices"][0]["message"]["content"]
    print(mensagem)