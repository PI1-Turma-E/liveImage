#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <unistd.h>

#define PORT 8080
#define DATA_QUANTITY 1

/*
* Brief: Sends data through a pre configured socket
*
* Parameters:
* int socket - A pre configured socket
* int* content - pointer to the content vector that keeps the 3 integers
*/
void send_data(int socket, int* content) {
  send(socket, content, 3*sizeof(int), 0);
}

int main() {
    // Socket configuration
    int server_file_descriptor;
    server_file_descriptor = socket(AF_INET, SOCK_STREAM, 0);

    int opt = 1;
    setsockopt(server_file_descriptor, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt));

    struct sockaddr_in address;
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    bind(server_file_descriptor, (struct sockaddr *)&address, sizeof(address));

    listen(server_file_descriptor, 3);

    int addrlen = sizeof(address);
    int new_socket;
    new_socket = accept(server_file_descriptor, (struct sockaddr*) &address, (socklen_t*) &addrlen);

    // Data sending
    int content[3] = {0};

    int x = 0;

    for(x = 0; x < DATA_QUANTITY; x++){

      int y;

      for(y=0; y<3; y++){
        scanf("%d", &content[y]);
      }

      send_data(new_socket, content);

    }

    return 0;
}
