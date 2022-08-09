#coding at utf-8
from concurrent import futures

import grpc
from proto import service_pb2
from proto import service_pb2_grpc
from proto import env_repo_service_pb2
from proto import env_repo_service_pb2_grpc

class ServiceBody(service_pb2_grpc.SampleServiceServicer):
    def SayHello(self, request, context):
        print("RECV : %s" % request.name)
        message = "Hello, %s !" % request.name
        print("SEND : %s" % message)
        dstIds = {1,2,3}
        return service_pb2.HelloReply(message=message, ids=dstIds)

class EnvRepoService(env_repo_service_pb2_grpc.EnvRepoServiceServicer):
    def GetEnvInfo(self, request, context):
        return env_repo_service_pb2.GetEnvInfoReply(repository_path='', latest_released_tag='V6.15.0')
    def GetTargetableTags(self, request, context):
        dst_list = []
        dst_list.append(env_repo_service_pb2.GetTargetableTagsReply.Tag(tag_name='x86'))
        return env_repo_service_pb2.GetTargetableTagsReply(tags=dst_list)
    def GetDiffFiles(self, request, context):
        print(request.target_tag)
        dst_list = []
        dst_list.append(env_repo_service_pb2.GetDiffFilesReply.DiffFile(file_full_path="hoge.json"))
        dst_list.append(env_repo_service_pb2.GetDiffFilesReply.DiffFile(file_full_path="systemvariable.dll"))
        return env_repo_service_pb2.GetDiffFilesReply(diff_files=dst_list)


def serve():
    # Create grpc server.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Add handler.
    service_pb2_grpc.add_SampleServiceServicer_to_server(ServiceBody(), server)
    env_repo_service_pb2_grpc.add_EnvRepoServiceServicer_to_server(EnvRepoService(), server=server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()