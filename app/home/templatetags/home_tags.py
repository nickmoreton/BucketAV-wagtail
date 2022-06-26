from django import template

register = template.Library()


@register.filter
def parse_image_filename(image, part="original_images/", replace=".../"):
    file_path = str(image.file)
    return file_path.replace(part, replace)


@register.filter
def parse_document_filename(document, part="documents/", replace=".../"):
    file_path = str(document.file)
    return file_path.replace(part, replace)
