# gRPC Demo

- [gRPC Demo](#grpc-demo)
  - [Requirements](#requirements)
  - [gRPC Service](#grpc-service)
  - [Testing the application](#testing-the-application)
    - [Start the Server](#start-the-server)
    - [Start the client](#start-the-client)
    - [Analyzing gRPC messages in Wireshark](#analyzing-grpc-messages-in-wireshark)

In this demo, we will take a look at a very basic example of `gRPC`

## Requirements

Confirm the following packages are installed, else install them using `pip`

```shell
python3 -m pip freeze | egrep "grpcio|grpcio-tools"
```

## gRPC Service

The gRPC service is defined in the `calculator.proto` file, with the RPC method parameters and return types.

<details>
<summary>Reveal Output</summary>
<p>

```proto
syntax = "proto3";
package calculator;

// Math service definition
service MathService {
  rpc Add (AddRequest) returns (AddResponse) {}
  rpc Subtract (SubtractRequest) returns (SubtractResponse) {}
}

// The request message containing two numbers.
message AddRequest {
  int32 num1 = 1;
  int32 num2 = 2;
}

// The response message containing the result.
message AddResponse {
  int32 result = 1;
}

// The request message containing two numbers.
message SubtractRequest {
  int32 num1 = 1;
  int32 num2 = 2;
}

// The response message containing the result.
message SubtractResponse {
  int32 result = 1;
}
```

</p>
</details>

gRPC uses `protoc` with a special gRPC plugin to generate code from your proto file: you get generated gRPC client and server code, as well as the regular protocol buffer code for populating, serializing, and retrieving your message types

Run the following command to generate the request/response and client/server classes.

```shell
python3 -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. calculator.proto
```

Post running above command following files will be generated:

- `calculator_pb2.py`: Contains the generated request and response classes
- `calculator_pb2_grpc.py`: Contains the generated client and server classes

## Testing the application

### Start the Server

```shell
$ python3 calc_server.py 
Server started, listening on port: 50051
```

### Start the client

```shell
$ python3 calc_client.py 
Asking server to add [ 71539 ] and [ 17593 ]
Asking server to subtract [ 71539 ] and [ 17593 ]
Addition Result: 89132
Subtraction Result: 53946
```

### Analyzing gRPC messages in Wireshark

With the `.proto` files available, Wireshark can be used to analyze plain text gRPC messages that are transferred over the network. More details can be found [here](https://grpc.io/blog/wireshark/).
