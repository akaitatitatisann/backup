"""Generated client library for alpha_vision version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.alpha_vision.v1 import alpha_vision_v1_messages as messages


class AlphaVisionV1(base_api.BaseApiClient):
  """Generated client library for service alpha_vision version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://alpha-vision.googleapis.com/'

  _PACKAGE = u'alpha_vision'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloud-vision']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'AlphaVisionV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new alpha_vision handle."""
    url = url or self.BASE_URL
    super(AlphaVisionV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.files = self.FilesService(self)
    self.images = self.ImagesService(self)
    self.operations = self.OperationsService(self)

  class FilesService(base_api.BaseApiService):
    """Service class for the files resource."""

    _NAME = u'files'

    def __init__(self, client):
      super(AlphaVisionV1.FilesService, self).__init__(client)
      self._upload_configs = {
          }

    def AsyncBatchAnnotate(self, request, global_params=None):
      """Run async image detection and annotation for a list of generic files (e.g.
PDF) which may contain multiple pages and multiple images per page.
Progress and results can be retrieved through the
`google.longrunning.Operations` interface.
`Operation.metadata` contains `OperationMetadata` (metadata).
`Operation.response` contains `AsyncBatchAnnotateFilesResponse` (results).

      Args:
        request: (AsyncBatchAnnotateFilesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('AsyncBatchAnnotate')
      return self._RunMethod(
          config, request, global_params=global_params)

    AsyncBatchAnnotate.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'alpha_vision.files.asyncBatchAnnotate',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1/files:asyncBatchAnnotate',
        request_field='<request>',
        request_type_name=u'AsyncBatchAnnotateFilesRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class ImagesService(base_api.BaseApiService):
    """Service class for the images resource."""

    _NAME = u'images'

    def __init__(self, client):
      super(AlphaVisionV1.ImagesService, self).__init__(client)
      self._upload_configs = {
          }

    def Annotate(self, request, global_params=None):
      """Run image detection and annotation for a batch of images.

      Args:
        request: (BatchAnnotateImagesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BatchAnnotateImagesResponse) The response message.
      """
      config = self.GetMethodConfig('Annotate')
      return self._RunMethod(
          config, request, global_params=global_params)

    Annotate.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'alpha_vision.images.annotate',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1/images:annotate',
        request_field='<request>',
        request_type_name=u'BatchAnnotateImagesRequest',
        response_type_name=u'BatchAnnotateImagesResponse',
        supports_download=False,
    )

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = u'operations'

    def __init__(self, client):
      super(AlphaVisionV1.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      """Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

      Args:
        request: (AlphaVisionOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations/{operationsId}:cancel',
        http_method=u'POST',
        method_id=u'alpha_vision.operations.cancel',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:cancel',
        request_field=u'cancelOperationRequest',
        request_type_name=u'AlphaVisionOperationsCancelRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (AlphaVisionOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations/{operationsId}',
        http_method=u'DELETE',
        method_id=u'alpha_vision.operations.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AlphaVisionOperationsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (AlphaVisionOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'alpha_vision.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AlphaVisionOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`. To
override the binding, API services can add a binding such as
`"/v1/{name=users/*}/operations"` to their service configuration.
For backwards compatibility, the default name includes the operations
collection id, however overriding users must ensure the name binding
is the parent resource, without the operations collection id.

      Args:
        request: (AlphaVisionOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations',
        http_method=u'GET',
        method_id=u'alpha_vision.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AlphaVisionOperationsListRequest',
        response_type_name=u'ListOperationsResponse',
        supports_download=False,
    )