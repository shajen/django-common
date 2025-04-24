from django.http import HttpResponse, HttpResponseServerError
import io
import os
import tarfile


def get_directory_as_archive_response(dir, name):
    if not dir:
        raise Exception("Expected log directory is empty.")
    if not os.path.isdir(dir):
        raise Exception("Expected log directory %s found." % dir)

    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w:gz") as tar:
        tar.add(dir, arcname=os.path.basename(dir))
    buffer.seek(0)

    response = HttpResponse(buffer.getvalue(), content_type="application/gzip")
    response["Content-Disposition"] = 'attachment; filename="%s.tar.gz"' % name
    response["Content-Length"] = str(buffer.getbuffer().nbytes)

    return response
