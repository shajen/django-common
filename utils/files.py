from django.http import HttpResponse, HttpResponseServerError
import io
import os
import tarfile


def get_directory_as_archive_response(dirs, archive_name):
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w:gz") as tar:
        for dir in dirs:
            if type(dir) is tuple:
                dir, name = dir
                dir = dir.removesuffix("/")
            else:
                dir = dir.removesuffix("/")
                name = os.path.basename(dir)
            if not os.path.isdir(dir):
                raise Exception("Expected log directory %s found." % dir)
            tar.add(dir, name)
    buffer.seek(0)

    response = HttpResponse(buffer.getvalue(), content_type="application/gzip")
    response["Content-Disposition"] = 'attachment; filename="%s.tar.gz"' % archive_name
    response["Content-Length"] = str(buffer.getbuffer().nbytes)

    return response
