from django.http import FileResponse
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
