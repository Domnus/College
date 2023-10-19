import asyncio
import websockets

async def connect_to_server():
    try:
        async with websockets.connect('ws://localhost:8000') as websocket:
            while True:
                # Obtenha a entrada do usuário
                message = input("Digite sua mensagem ('exit' para sair): ")

                if message.lower() == 'exit':
                    break

                # Envie a mensagem para o servidor
                await websocket.send(message)

                # Receba uma resposta do servidor
                response = await websocket.recv()

                # Exiba a mensagem recebida
                print("Recebido:", response)
    except KeyboardInterrupt:
        print("Cliente WebSocket encerrado.")

# Conecta o cliente WebSocket
asyncio.get_event_loop().run_until_complete(connect_to_server())
