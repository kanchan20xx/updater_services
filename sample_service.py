# coding=utf-8
import grpc

from proto import service_pb2
from proto import service_pb2_grpc

class ServiceBody(service_pb2_grpc.SampleServiceServicer):
    def SayHello(self, request, context):
        print("RECV : %s" % request.name)
        message = "Hello, %s !" % request.name
        print("SEND : %s" % message)
        dstIds = {1,2,3}
        return service_pb2.HelloReply(message=message, ids=dstIds)

def RegisterGrpcServer(grpc_server):
    service_pb2_grpc.add_SampleServiceServicer_to_server(ServiceBody(), server=grpc_server)
    return