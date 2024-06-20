import socket
import sys
import os

def parse_request(request_data):
    lines = request_data.split('\r\n')
    print(lines)
    start_line = lines[0]
    headers = {}
    
    index = 1
    while lines[index] != '':  
        
        header_key, header_value = lines[index].split(': ', 1)
        headers[header_key] = header_value
        index += 1

    body_index = index + 1
    body = '\r\n'.join(lines[body_index:])

    parts = start_line.split(' ')
    if len(parts) != 3:
        raise ValueError(f"Invalid request line: {start_line}")

    method, path, version = parts
    
    user_agent = ""
    for line in lines:
        if line.startswith("User-Agent:"):
            user_agent = line.split("User-Agent: ")[1]
            break
            
    return path, user_agent, method, headers, body

def get_response(path, user_agent, method, headers, body):
    
    default_response = "HTTP/1.1 404 Not Found\r\n\r\nPage not found."

    if path == "/":
        return "HTTP/1.1 200 OK\r\n\r\nHello, World!"

    if path.startswith("/echo/"):
        echo_string = path[len("/echo/"):]
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(echo_string)}\r\n\r\n{echo_string}"
        return response

    if path == "/user-agent":
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_agent)}\r\n\r\n{user_agent}"
        return response
    
    if path.startswith("/files"):
        directory = sys.argv[2]
        filename = os.path.basename(path)  
        file_path = os.path.join(directory, filename)

        if method == "GET":
            try:
                with open(file_path, "r") as f:
                    file_content = f.read()
                return f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: {len(file_content)}\r\n\r\n{file_content}"
            except FileNotFoundError:
                return "HTTP/1.1 404 Not Found\r\n\r\nFile not found"
            except Exception as e:
                return f"HTTP/1.1 500 Internal Server Error\r\n\r\n{str(e)}"

        elif method == "POST":
            try:
                with open(file_path, "w") as f:
                    f.write(body)
                return "HTTP/1.1 201 Created\r\n\r\nFile created"
            except Exception as e:
                return f"HTTP/1.1 500 Internal Server Error\r\n\r\n{str(e)}"
    
    return default_response

def handle_request(client_socket):
    request_data = client_socket.recv(1024).decode("UTF-8")
    print("Request data:")
    print(request_data)  

    try:
        path, user_agent, method, headers, body = parse_request(request_data)
        response = get_response(path, user_agent, method, headers, body)
    except ValueError as e:
        print(f"Error parsing request: {e}")
        response = "HTTP/1.1 400 Bad Request\r\n\r\nBad Request"

    print("Response data:")
    print(response)  

    client_socket.sendall(response.encode())

def main():
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221))

    try:
        while True:
            print("Waiting for a connection...")
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr} has been established")
            handle_request(client_socket)
            client_socket.close()
    except KeyboardInterrupt:
        print("\nServer is shutting down")
    finally:
        server_socket.close()
        print("Server has been shut down")

if __name__ == "__main__":
    main()
