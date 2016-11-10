from __future__ import unicode_literals

from io import BytesIO

from django.conf import settings
from django.core.files.uploadhandler import FileUploadHandler, StopFutureHandlers
from django_extention.uploadedfile import (InMemoryUploadedFile, TemporaryUploadedFile)


class RelativePathTemporaryFileUploadHandler(FileUploadHandler):
    """
    Upload handler that streams data into a temporary file.
    """
    def __init__(self, *args, **kwargs):
        super(RelativePathTemporaryFileUploadHandler, self).__init__(*args, **kwargs)

    def new_file(self, *args, **kwargs):
        """
        Create the file object to append to as data is coming in.
        """
        super(RelativePathTemporaryFileUploadHandler, self).new_file(*args, **kwargs)
        self.file = TemporaryUploadedFile(self.file_name, self.content_type, 0, self.charset, self.content_type_extra)

    def receive_data_chunk(self, raw_data, start):
        self.file.write(raw_data)

    def file_complete(self, file_size):
        self.file.seek(0)
        self.file.size = file_size
        return self.file


class RelativePathMemoryFileUploadHandler(FileUploadHandler):
    """
    File upload handler to stream uploads into memory (used for small files).
    """

    def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
        """
        Use the content_length to signal whether or not this handler should be in use.
        """
        # Check the content-length header to see if we should
        # If the post is too large, we cannot use the Memory handler.
        if content_length > settings.FILE_UPLOAD_MAX_MEMORY_SIZE:
            self.activated = False
        else:
            self.activated = True

    def new_file(self, *args, **kwargs):
        super(RelativePathMemoryFileUploadHandler, self).new_file(*args, **kwargs)
        if self.activated:
            self.file = BytesIO()
            raise StopFutureHandlers()

    def receive_data_chunk(self, raw_data, start):
        """
        Add the data to the BytesIO file.
        """
        if self.activated:
            self.file.write(raw_data)
        else:
            return raw_data

    def file_complete(self, file_size):
        """
        Return a file object if we're activated.
        """
        if not self.activated:
            return

        self.file.seek(0)
        return InMemoryUploadedFile(
            file=self.file,
            field_name=self.field_name,
            name=self.file_name,
            content_type=self.content_type,
            size=file_size,
            charset=self.charset,
            content_type_extra=self.content_type_extra
        )
