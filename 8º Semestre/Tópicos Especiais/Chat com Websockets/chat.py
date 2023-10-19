# Servidor
import asyncio
import websockets

connected_clients = set()

async def handle_connection(websocket, path):
    # Adiciona o websocket à lista de clientes conectados
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Transmite a mensagem para todos os clientes conectados
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosedError:
        pass
    finally:
        # Remove o websocket da lista de clientes conectados
        connected_clients.remove(websocket)

# Inicia o servidor WebSocket
start_server = websockets.serve(handle_connection, 'localhost', 8000)

# Executa o servidor indefinidamente
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# Cliente
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
