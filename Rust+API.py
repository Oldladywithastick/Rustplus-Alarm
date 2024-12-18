import asyncio
from rustplus import RustSocket, ServerDetails

async def main():
    server_details = ServerDetails("154.6.138.32", "28082", 76561199084429057, -1928286762)
    socket = RustSocket(server_details)
    await socket.connect()

    try:
        entity_info = await socket.get_entity_info(371824932)  # Assuming 2 is the ID
        server_details = await socket.get_info()
        print(f"Entity Info for ID 2: {entity_info}")
        print(f"Server Details: {server_details}")
    except Exception as e:
        print(f"Error fetching entity info: {e}")

    await socket.disconnect()

asyncio.run(main())
