import grpc
import calculator_pb2
import calculator_pb2_grpc
from concurrent import futures

class MathService(calculator_pb2_grpc.MathServiceServicer):
    def Add(self, request, context):
        print("Received request to add [ {} ] and [ {} ]".format(request.num1, request.num2))
        result = request.num1 + request.num2
        return calculator_pb2.AddResponse(result=result)

    def Subtract(self, request, context):
        print("Received request to subtract [ {} ] and [ {} ]".format(request.num1, request.num2))
        result = request.num1 - request.num2
        return calculator_pb2.SubtractResponse(result=result)
    
def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_MathServiceServicer_to_server(MathService(), server=server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on port: {}".format(port))
    server.wait_for_termination()

if __name__ == "__main__":
    serve()