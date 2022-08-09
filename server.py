#coding at utf-8
from concurrent import futures

import grpc
from proto import service_pb2
from proto import service_pb2_grpc

class ServiceBody(service_pb2_grpc.SampleServiceServicer):
    def SayHello(self, request, context):
        print("RECV : %s" % request.name)
        message = "Hello, %s !" % request.name
        print("SEND : %s" % message)
        return service_pb2.HelloReply(message=message)

def serve():
    # Create grpc server.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Add handler.
    service_pb2_grpc.add_SampleServiceServicer_to_server(ServiceBody(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()