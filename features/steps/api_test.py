from behave import *
from requests_egg import *
import os


u = UploadRequest()
m = GetFileMetadataRequest()
d = DeleteRequest()


@given(u'file name is "text.txt"')
def step_impl(context):
    assert os.path.isfile('./files/text.txt')==True


@when(u'uploading "text.txt" file to Dropbox')
def step_impl(context):
    u.get_response()


@then(u'file "text.txt" is uploaded')
def step_impl(context):
    assert u.response.status_code == 200



@given(u'file named "text.txt" is uploaded')
def step_impl(context):
    assert u.response.status_code == 200


@when(u'requesting metadata of "text.txt" by its id')
def step_impl(context):
    m.get_response(u.id)


@then(u'we receive metadata for "text.txt"')
def step_impl(context):
    assert m.response.status_code == 200


@given(u'we have file path of "text.txt"')
def step_impl(context):
    assert m.file_path!=None


@when(u'we request to delete "text.txt"')
def step_impl(context):
    d.get_response(m.file_path)


@then(u'file "text.txt" deleted')
def step_impl(context):
    assert d.response.status_code==200