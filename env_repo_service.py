# coding=utf-8
import grpc
from proto import env_repo_service_pb2
from proto import env_repo_service_pb2_grpc


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

def RegisterGrpcServer(grpc_server):
    env_repo_service_pb2_grpc.add_EnvRepoServiceServicer_to_server(EnvRepoService(), server=grpc_server)
    return