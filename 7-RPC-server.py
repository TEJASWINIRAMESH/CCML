import socket
import json

# Define the functions for each operation
def add(args):
    return sum(args)

def subtract(args):
    return args[0] - sum(args[1:])

def multiply(args):
    result = 1
    for arg in args:
        result *= arg
    return result

def divide(args):
    try:
        result = args[0]
        for arg in args[1:]:
            result /= arg
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"

# Function to process the request
def process_request(request):
    function_name = request.get("function")
    args = request.get("args")
    
    if function_name == "add":
        result = add(args)
    elif function_name == "subtract":
        result = subtract(args)
    elif function_name == "multiply":
        result = multiply(args)
    elif function_name == "divide":
        result = divide(args)
    else:
        result = "Error: Unsupported function"

    return {"result": result}

# Server setup
def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server started, listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive the request data
        request_data = client_socket.recv(1024).decode()
        request = json.loads(request_data)

        # Process the request
        response = process_request(request)

        # Send the response back to the client
        client_socket.sendall(json.dumps(response).encode())

        client_socket.close()

if __name__ == "__main__":
    start_server()
