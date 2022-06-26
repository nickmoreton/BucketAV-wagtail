from django import template

register = template.Library()


@register.filter
def concat_image_filename(image, part="original_images/", replace=".../"):
    file_path = str(image.file)
    return file_path.replace(part, replace)
