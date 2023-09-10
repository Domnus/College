import grpc
from concurrent import futures

class GreeterServicer(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message="Hello, " + request.name)

    def Soma(self, request, context):
        result = request.num1 + request.num2
        return helloworld_pb2.HelloReply(message=str(result))

    def Divisao(self, request, context):
        if request.num2 == 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Division by zero!')
            return helloworld_pb2.HelloReply(message="Division by zero is not allowed")

        result = request.num1 / request.num2
        return helloworld_pb2.HelloReply(message=str(result))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
