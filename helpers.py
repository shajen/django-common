from django.http import FileResponse, HttpResponse
import mimetypes
import os


def file_response(filename, download_filename=None, remove=True):
    mime = mimetypes.MimeTypes()
    content_type = mime.guess_type(filename)[0]
    if not download_filename:
        download_filename = filename
    response = FileResponse(open(filename, "rb"), content_type=content_type, filename=download_filename)
    if remove:
        os.remove(filename)
    return response


def redirect_file_response(url, filename):
    response = HttpResponse()
    response["Content-Type"] = "application/octet-stream"
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    response["X-Accel-Redirect"] = url
    return response


def is_json_request(request):
    return "application/json" in request.headers.get("Accept", "")
